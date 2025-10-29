import os
import sys
import subprocess

def getStatus():
  proc = os.system("git status")
  print("\nos.system exec: ", proc)
  proc2 = subprocess.run(["git", "diff", "--cached", "--exit-code"], text = True, check = False)
  print("sub process output: \n", proc2)

getStatus()
print("-"*70)
subprocess.run(["git", "diff", "--name-only"],stdout = True, text = True, check = False)
