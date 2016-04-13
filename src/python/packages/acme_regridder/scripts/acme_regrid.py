#!/usr/bin/env python

# Import regrid2 package for regridder functions
import cdms2
import sys
import os
import numpy
import MV2
import argparse
import metrics
import metrics.packages.acme_regridder._regrid
import cdutil
import datetime
import time
from metrics.common import store_provenance
import cdat_info
try:
    print "TRYING T IMPORT"
    import mpi4py
    has_mpi = True
    sz = mpi4py.MPI.COMM_WORLD.Get_size()
    rk = mpi4py.MPI.COMM_WORLD.Get_rank()
except:
    has_mpi = False
    sz = 1
    rk = 0

print "MPI:",has_mpi

class WeightFileRegridder:
    def __init__(self, weightFile, toRegularGrid=True, fix_bounds=False):
        if isinstance(weightFile, str):
            if not os.path.exists(weightFile):
                raise Exception("WeightFile %s does not exists" % weightFile)
            print rk,"trying to open:",weightFile
            wFile = cdms2.open(weightFile)
        else:
            wFile = weightFile
        print "OPENED IT"
        self.S = wFile("S").filled()
        self.row = wFile("row").filled()-1
        self.col = wFile("col").filled()-1
        self.mask_b = wFile("mask_b")
        self.nb = self.mask_b.shape[0]
        if self.mask_b.min() == 1 and self.mask_b.max() == 1:
            print "No need to maks after"
            self.mask_b = False
        else:
            print "MX MIN:", self.mask_b.max(), self.mask_b.min()
            self.mask_b = numpy.logical_not(wFile("mask_b").filled())
        self.n_s = self.S.shape[0]
        self.method = wFile.map_method
        self.regular = toRegularGrid
        if toRegularGrid:
            self.lats = cdms2.createAxis(sorted(set(wFile("yc_b").tolist())))
            self.lats.designateLatitude()
            self.lats.units = "degrees_north"
            bnds = numpy.array(sorted(set(wFile("yv_b").ravel().tolist())))
            self.lats.setBounds(bnds)
            self.lats.id = "lat"
            self.lons = cdms2.createAxis(sorted(set(wFile("xc_b").tolist())))
            bnds = numpy.array(sorted(set(wFile("xv_b").ravel().tolist())))
            self.lons.designateLongitude()
            self.lons.units = "degrees_east"
            if fix_bounds:
              self.lons.setBounds(None)
            else:
              self.lons.setBounds(bnds)
            self.lons.id = "lon"
        else:
            self.yc_b = wFile("yc_b")
            self.xc_b = wFile("xc_b")
            self.yv_b = wFile("yv_b")
            self.xv_b = wFile("xv_b")

        if isinstance(weightFile, str):
            wFile.close()

    def regrid(self, input):
        axes = input.getAxisList()
        input_id = input.id
        M = input.getMissing()
        if input.mask is numpy.ma.nomask:
            isMasked = False
            input = input.data
        else:
            isMasked = True
            input = input.filled(float(M))
        sh = input.shape
        if isMasked:
            dest_field = \
                metrics.packages.acme_regridder._regrid.apply_weights_masked(
                    input, self.S, self.row, self.col, self.nb, float(M))
        else:
            dest_field = metrics.packages.acme_regridder._regrid.apply_weights(
                input, self.S, self.row, self.col, self.nb)
        if self.mask_b is not False:
            print "Applying mask_b"
            dest_field = numpy.ma.masked_where(self.mask_b, dest_field)
        if self.regular:
            sh2 = list(sh[:-1])
            sh2.append(len(self.lats))
            sh2.append(len(self.lons))
            dest_field.shape = sh2
            dest_field = MV2.array(dest_field, id=input_id)
            dest_field.setAxis(-1, self.lons)
            dest_field.setAxis(-2, self.lats)
            for i in range(len(sh2)-2):
                dest_field.setAxis(i, axes[i])
            if isMasked:
                dest_field.setMissing(M)
        return dest_field


def addAxes(f, axisList, store_bounds = False):
    axes = []
    for ax in axisList:
        if ax.id not in f.listdimension():
            print rk,"is adding axes:",ax.id
            A = f.createAxis(ax.id, ax[:])
            atts = ax.attributes
            if store_bounds and ax.isLatitude():
              atts["bounds"]="latitude_bounds"
            elif store_bounds and ax.isLongitude():
              atts["bounds"]="longitude_bounds"
            for att in atts:
                setattr(A, att, atts[att])
        else:
            A = f.getAxis(ax.id)
        axes.append(A)
    return axes


def addVariable(f, id, typecode, axes, attributes, store_bounds=False,createVariable = True):
    axes = addAxes(f, axes, store_bounds)
    if createVariable:
        print rk,"is  adding",id
        V = f.createVariable(id, typecode, axes)
        for att in attributes:
            setattr(V, att, attributes[att])

def preprocess_variable(V,axes3d,axes4d,axes4d_ilev,wgt,tim_bnds,createVariable):
        print rk,"prerocess",V.id,"create",createVariable
        if V is None:
            print "Will skip", V, "as it does NOT appear to be in file"
        elif V.id in ["lat", "lon", "area"]:
            print i, NVARS, "Will skip", V.id, "no longer needed or recomputed"
        elif "ncol" in V.getAxisIds():
            print i, NVARS, "Will process:", V.id
            if V.rank() == 2:
                if axes3d == []:
                    dat2 = cdms2.MV2.array(regdr.regrid(V()))
                    axes3d = dat2.getAxisList()
                addVariable(fo, V.id, V.typecode(), axes3d, V.attributes, store_bounds=args.store_bounds,createVariable=createVariable)
            elif V.rank() == 3:
                if "ilev" in V.getAxisIds(): # New CLUBB things
                    if axes4d_ilev == []:
                        dat2 = cdms2.MV2.array(regdr.regrid(V()))
                        axes4d_ilev = dat2.getAxisList()
                    addVariable(fo, V.id, V.typecode(), axes4d_ilev, V.attributes, store_bounds=args.store_bounds,createVariable=createVariable)
                else:
                    if axes4d == []:
                        dat2 = cdms2.MV2.array(regdr.regrid(V()))
                        axes4d = dat2.getAxisList()
                    addVariable(fo, V.id, V.typecode(), axes4d, V.attributes, store_bounds=args.store_bounds,createVariable=createVariable)
            if wgt is None:
                wgt = True
                addVariable(fo, "gw", "d", [dat2.getLatitude(), ], [],createVariable=createVariable)
                addVariable(fo, "area", "d",
                            [dat2.getLatitude(), dat2.getLongitude()],
                            {"units": "steradian",
                             "long_name": "solid angle subtended by grid cell",
                             "standard_name": "cell_area",
                             "cell_methods": "lat, lon: sum"}
                            ,createVariable=createVariable)
        else:
            print "Will rewrite as is", V.id
            addVariable(fo, V.id, V.typecode(), V.getAxisList(), V.attributes, store_bounds=args.store_bounds,createVariable=createVariable)
            if V.id == "time_bnds":
              tim_bnds = v
        return axes3d,axes4d,axes4d_ilev,wgt,tim_bnds
if __name__ == "__main__":
    cdms2.setNetcdfClassicFlag(0)
    #cdms2.setNetcdf4Flag(1)
    cdms2.setNetcdfUseNCSwitchModeFlag(0)
    cdms2.setNetcdfShuffleFlag(0)
    cdms2.setNetcdfDeflateFlag(0)
    cdms2.setNetcdfDeflateLevelFlag(0)
    print "FLAGGED"

    # Create the parser for user input
    parser = argparse.ArgumentParser(
        description='Regrid variables in a file using a weight file')
    parser.add_argument("--input", "-i",
                        "-f", "--file",
                        dest="file",
                        help="input file to process",
                        required=True)
    parser.add_argument("--weight-file", "-w",
                        dest="weights",
                        help="path to weight file",
                        required=True)
    parser.add_argument("--output", "-o", dest="out", help="output file")
    parser.add_argument("--var", "-v",
                        dest="var",
                        nargs="*",
                        help="variable to process\
                            (default is all variable with 'ncol' dimension")
    parser.add_argument("--store-bounds",dest="store_bounds",action="store_true",default=False,help="store lat/lon bounds information")
    parser.add_argument("--fix-esmf-bounds",dest="fix_bounds",action="store_true",default=False,help="fix esmf first and last longitudes being half width")

    args = parser.parse_args(sys.argv[1:])
    print "AERGS:",args

    # Read the weights file
    regdr = WeightFileRegridder(args.weights,True,fix_bounds=args.fix_bounds)
    print "WEIGHT THINGY"

    f = cdms2.open(args.file)
    fw = cdms2.open(args.weights)

    cdms2.setNetcdfUseParallelFlag(1)
    if args.out is None:
        onm = ".".join(args.file.split(".")[:-1])+"_regrid.nc"
    else:
        onm = args.out
    print "Output file:", onm
    if has_mpi:
        # Need to make sure file is gone
        if rk==0:
            if os.path.exists(onm):
                os.remove(onm)
        mpi4py.MPI.COMM_WORLD.Barrier()
    print rk,"opening",onm
    fo = cdms2.open(onm, "w")
    if has_mpi:
        mpi4py.MPI.COMM_WORLD.Barrier()
    store_provenance(fo,script_file_name=__file__)
    if has_mpi:
        mpi4py.MPI.COMM_WORLD.Barrier()
    history = ""
    # Ok now let's start by copying the attributes back onto the new file
    for a in f.attributes:
        if a != "history":
            setattr(fo, a, getattr(f, a))
    history = fo.history+"\n"
    history += "%s: weights applied via acme_regrid (git commit: %s), " % (
                    str(datetime.datetime.utcnow()), metrics.git.commit,
                    )
                    
    fo.history = history
    if has_mpi:
        mpi4py.MPI.COMM_WORLD.Barrier()
    dirnm = os.path.dirname(args.file)
    basenm = os.path.basename(args.file)
    if dirnm == '':  # no dirname using current dir
        dirnm = os.getcwd()
    elif dirnm[0] != os.path.sep:
        dirnm = os.path.join(os.getcwd(), dirnm)
    fo.input_file = os.path.join(dirnm, basenm)
    if has_mpi:
        mpi4py.MPI.COMM_WORLD.Barrier()

    dirnm = os.path.dirname(args.weights)
    basenm = os.path.basename(args.weights)
    if dirnm == '':  # no dirname using current dir
        dirnm = os.getcwd()
    elif dirnm[0] != os.path.sep:
        dirnm = os.path.join(os.getcwd(), dirnm)
    fo.map_file = os.path.join(dirnm, basenm)
    if has_mpi:
        mpi4py.MPI.COMM_WORLD.Barrier()

    wgt = None
    if args.var is not None:
        vars = args.var
    else:
        vars = f.variables.keys()
    axes3d = []
    axes4d = []
    axes4d_ilev = []
    wgts = None
    area = None
    NVARS = len(vars)
    tim_bnds = None
    if "time_bnds" in vars:
        vars.remove("time_bnds")
        vars.insert(0,"time_bnds")
    for i, v in enumerate(vars):
        print rk,i,v
        V = f[v]
        axes3d,axes4d,axes4_ilev,wgt,tim_bnds = preprocess_variable(V,axes3d,axes4d,axes4d_ilev,wgt,tim_bnds,False)
        if has_mpi:
            mpi4py.MPI.COMM_WORLD.Barrier()
    wgt = None
    axes3d = []
    axes4d = []
    axes4d_ilev = []
    for i, v in enumerate(vars):
        print rk,i,v
        V = f[v]
        axes3d,axes4d,axes4_ilev,wgt,tim_bnds = preprocess_variable(V,axes3d,axes4d,axes4d_ilev,wgt,tim_bnds,True)
        if has_mpi:
            mpi4py.MPI.COMM_WORLD.Barrier()
    print "OK rk %i is done defing" % rk
    if has_mpi:
        mpi4py.MPI.COMM_WORLD.Barrier()
    # latitude and longitude bounds
    if args.store_bounds:
      addVariable(fo, "latitude_bounds", "d", [regdr.lats, tim_bnds], {}, store_bounds=args.store_bounds)
      addVariable(fo, "longitude_bounds", "d", [regdr.lons, tim_bnds], {}, store_bounds=args.store_bounds)

    if has_mpi:
        mpi4py.MPI.COMM_WORLD.Barrier()

    print "OK rk %i is really done defing" % rk
    tim_bnds =  f[tim_bnds].getAxisList()[-1]
    if has_mpi:
        mpi4py.MPI.COMM_WORLD.Barrier()
    print "Time bounds done"
    wgts = None
    for i, v in enumerate(vars):
        if i % sz != rk:
            continue
        V = f[v]
        if V is None:
            print "Skipping", V, "as it does NOT appear to be in file"
        elif V.id in ["lat", "lon", "area"]:
            print i, NVARS, "Skipping", V.id, "no longer needed or recomputed"
        elif "ncol" in V.getAxisIds():
            print i, NVARS, "Processing:", V.id
            V2 = fo[V.id]
            print rk,"recovered",V.id
            dat2 = cdms2.MV2.array(regdr.regrid(V()))
            V2[:] = dat2[:].astype(V.typecode())
            print rk,"saved",V.id
            if wgts is None:
                print "trying to get weights"
                wgts = [numpy.sin(x[1]*numpy.pi/180.) -
                        numpy.sin(x[0]*numpy.pi/180.)
                        for x in dat2.getLatitude().getBounds()]
                V2 = fo["gw"]
                V2[:] = wgts[:]
                if dat2.ndim > 3:
                    dat2 = dat2[0, 0]
                else:
                    dat2 = dat2[0]
                print "Computing area weights"
                area = fw("area_b")
                #fw.close()
                if numpy.allclose(area,0.):
                  print "area is all zeroes computing it for you"
                  area = cdutil.area_weights(dat2)*numpy.pi*4.
                area = MV2.reshape(area, dat2.shape[-2:])
                V2 = fo["area"]
                V2[:] = area[:]
        else:
            print i, NVARS, "Rewriting as is:", V.id
            try:
                V2 = fo[V.id]
                if V2.rank() == 0:
                    V2[:] = V.getValue()
                elif V2.id == "time_written":
                    d = datetime.datetime.utcnow()
                    time_written = "%.2i:%.2i:%.2i" % \
                                   (d.hour, d.minute, d.second)
                    V2[:] = numpy.array([x for x in time_written])
                elif V2.id == "date_written":
                    d = datetime.datetime.utcnow()
                    date_written = "%.2i/%.2i/%s" % \
                                   (d.month, d.day, str(d.year)[-2:])
                    V2[:] = numpy.array([x for x in date_written])
                else:
                    V2[:] = V[:]
            except Exception, err:
                print "Variable %s falied with error: %s" % (V2.id, err)
        if has_mpi:
            mpi4py.MPI.COMM_WORLD.Barrier()
    # latitude and longitude bounds
    if args.store_bounds:
      fo["latitude_bounds"][:]=regdr.lats.getBounds()
      fo["longitude_bounds"][:]=regdr.lons.getBounds()
    if has_mpi:
        mpi4py.MPI.COMM_WORLD.Barrier()
    fo.close()
