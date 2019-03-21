import subprocess

cmd = 'ls -a && df'
p = subprocess.Popen(cmd, stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE, shell=True)
out, err = p.communicate()
print(out, err)