#pylint: skip-file
#type-ignore

import os
import time
import sys
import subprocess

print("untracked files: ")
proc = subprocess.run(["git", "ls-files", "-o"], stdout=subprocess.PIPE, text=True)

for i,j in enumerate(proc.stdout.splitlines(), start=1):
    print(i, j)
    os.system(f"git add {j}")

time.sleep(3)
for f in (proc.stdout.splitlines()):
    os.system(f"git restore --staged {f}")

print("diff check: ")
a = subprocess.run(["git", "diff", "--name-only"], text=True, check=False)
