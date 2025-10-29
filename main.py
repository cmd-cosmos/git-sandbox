import os
import sys
import subprocess

def getStatus():
  proc = os.system("git status")
  print("\nos.system exec: ", proc)
  proc2 = subprocess.run(["git", "status"], stdout = True, text = True, check = False)
  print("sub process output: \n", proc2)

getStatus()
