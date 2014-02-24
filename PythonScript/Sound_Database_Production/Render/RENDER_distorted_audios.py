# ------------------------------------------
# ReaScript Render
# Author : Mincong ZHANG
#
# This file script a Render from ReaScript 
# (1)It can automatically change the parameters of any VST plugins
# (2)It can specify the output filename and settings in the script, and perform the render without user intervention 
# 
# ------------------------------------------

import os,sys

renderpath="E:/Zhang-Mincong"
newpath="E:/Zhang-Mincong/Final_samples/source2"
rendername="xxx.mp3"
#newname="yyy.wav"


#----------------reset parameters(bass,mid,treble) to zero-------------
tr = RPR_GetTrack(0,0)
RPR_ShowConsoleMsg("resetting drive bass mid treble to 0.1 \n")
for i in range(3,7):
 RPR_TrackFX_SetParam(tr, 0, i, 0.1);
RPR_ShowConsoleMsg("START \n")


#----------------define render function--------------------------------
def render_and_rename(renderpath,newpath,rendername,newname):
 filenames=os.listdir(newpath)
 if newname not in os.listdir(newpath):  #avoid overwriting
  RPR_Main_OnCommand(41823,0)  #add project to render queue, using the most recent render settings
  RPR_Main_OnCommand(41207,0)  #render all queued renders
  os.renames(renderpath + os.sep + rendername,newpath + os.sep + newname)

#----------------define function for printing 4 values--------------------------------
def print_values():
 tr = RPR_GetTrack(0,0)
 val1 = RPR_TrackFX_GetParam(tr, 0, 3, 0, 1)[0]
 val2 = RPR_TrackFX_GetParam(tr, 0, 4, 0, 1)[0]
 val3 = RPR_TrackFX_GetParam(tr, 0, 5, 0, 1)[0]
 val4 = RPR_TrackFX_GetParam(tr, 0, 6, 0, 1)[0]
 RPR_ShowConsoleMsg("drive:"+str(val1)[:4] +" ")
 RPR_ShowConsoleMsg("bass:"+str(val2)[:4] +" ")
 RPR_ShowConsoleMsg("mid:"+str(val3)[:4] +" ")
 RPR_ShowConsoleMsg("treble:"+str(val4)[:4] +" \n")

#----------------define function for new file name--------------------------------
def newname():
 name=str(d*10)[:1]+str(b*10)[:1]+str(m*10)[:1]+str(t*10)[:1]+"b.mp3"
 return name


#----------------genetare audios----------------------------------
D=[0.1, 0.3, 0.5, 0.8]
B=[0.1, 0.3, 0.5, 0.7, 0.9]
M=[0.1, 0.3, 0.5, 0.7, 0.9]
T=[0.1, 0.3, 0.5, 0.7, 0.9]

#setting positions
drive=3
bass=4
mid=5
treble=6

#initial settings
d=0.1
b=0.1
m=0.1
t=0.1

tr = RPR_GetTrack(0,0)

for d in D:
 RPR_TrackFX_SetParam(tr, 0, drive, d);
 render_and_rename(renderpath,newpath,rendername,newname())
 print_values()

 for b in B: 
  RPR_TrackFX_SetParam(tr, 0, bass, b);
  render_and_rename(renderpath,newpath,rendername,newname())
  print_values()

  for m in M: 
   RPR_TrackFX_SetParam(tr, 0, mid, m);
   render_and_rename(renderpath,newpath,rendername,newname())
   print_values()

   for t in T: 
    RPR_TrackFX_SetParam(tr, 0, treble, t);
    render_and_rename(renderpath,newpath,rendername,newname())
    print_values()