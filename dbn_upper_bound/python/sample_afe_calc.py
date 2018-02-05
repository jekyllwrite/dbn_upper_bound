import csv
from mpmath import mp
from mputility import *

def append_data(filename,rows):
    with open(filename, 'a', newline='') as csvfile:
         writer = csv.writer(csvfile, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
         writer.writerows(rows)

def sign_change(x, y):
    if x*y < 0: return 1
    else: return 0

mp.dps=40
t=0.0
evalfilename = "Ht_eval_vlargez"+str(t)+".csv"
Htrootfilename = "Ht_roots_vlargez_"+str(t)+".csv"
evalrows = []
htroots = []
step_size = 0.01
prev_eval = 0.0
rootcount = 0
z=25.0
for i in range(1,5000000001):
    z += step_size
    curr_eval = (Ht_AFE(z,t).real)*mp.exp(mp.pi()*z/8)
    root_check = sign_change(curr_eval,prev_eval)
    if root_check==1: approx_root=z-step_size/2; print(approx_root); rootcount+=1; htroots.append([t,rootcount,approx_root])
    evalrows.append([t,z,curr_eval,root_check])
    prev_eval = curr_eval
    if i%10000==0: append_data(evalfilename, evalrows); evalrows=[]
    if rootcount%100==0: append_data(Htrootfilename, htroots); htroots=[]


append_data(evalfilename, evalrows)
append_data(Htrootfilename, htroots) 
