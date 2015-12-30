import subprocess, pdb, time
SBATCH_EXEC = 'sbatch --nodes=1 --ntasks-per-node=6 diag.sh'
proc=subprocess.Popen([SBATCH_EXEC], shell=True, stdout=subprocess.PIPE)
time.sleep(30)
#pdb.set_trace()
#subprocess.Popen.wait(proc) #x.wait()
#retrieve jobid and create the slurm file name
msg = proc.communicate()[0]
msg = msg.split()
jobid = msg[-1]
slurmFile = 'slurm-'+jobid+'.out'
print slurmFile

f=open(slurmFile)
for line in f.readlines():
    if 'time =' in line:
        print line
        break
#retrieve run time
t=line.split()[2]
time = float(t)
print time