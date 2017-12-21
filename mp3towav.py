import os
import glob
import subprocess

path=os.getcwd()
files=glob.glob('*.mp3')

for file in files:
    mp=path+'/'+file
    wa=path+'/'+file.replace('mp3','wav')
    subprocess.call(['sox', mp, '-e', 'mu-law','-r', '16k', wa, 'remix', '1,2'])
