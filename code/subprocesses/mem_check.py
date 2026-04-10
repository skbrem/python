import subprocess

mem = subprocess.check_output(["free", "-h"], text=True)

print(mem)
