#pylint: skip-file
#type-ignore

import os
import time
import sys
import subprocess

def check_untracked():
    print("untracked files: ")
    proc = subprocess.run(["git", "ls-files", "-o"], stdout=subprocess.PIPE, text=True)

    lst = list()
    start_val = 1
    for i,j in enumerate(proc.stdout.splitlines(), start=start_val):
        print(i, j)
        lst.append(j)
    
    proc2 = subprocess.run(["git", "diff", "--name-only"], text=True, stdout=subprocess.PIPE)

    for i,j in enumerate(proc2.stdout.splitlines(), start=(start_val+1)):
        print(i, j)
        lst.append(j)
    
    print(lst)

check_untracked()

def diff_check():
    print("diff check: ")
    a = subprocess.run(["git", "diff", "--name-only"], text=True, check=False)

