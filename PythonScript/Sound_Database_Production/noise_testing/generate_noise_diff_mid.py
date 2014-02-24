import random
import os,sys

renderpat="E:/Zhang-Mincong"
newpat="E:/Zhang-Mincong/noises/mid"
render="xxx.wav"

def render_and_rename(renderpath,newpath,rendername,newname):
 RPR_Main_OnCommand(41823,0) #add project to render queue, using the most recent render settings
 RPR_Main_OnCommand(41207,0) #render all queued renders
 if new not in os.listdir(newpat):
  os.renames(renderpath + os.sep + rendername,newpath + os.sep + newname)
 if new in os.listdir(newpat):
  RPR_ShowConsoleMsg("\n\n"+new+" is generated in "+newpat+"\n") 

RPR_ShowConsoleMsg( "reset drive(3) to 0;bass, mid, treble (position: 4 5 6) to 0.5\n" )

tr1 = RPR_GetTrack(0,0)
RPR_TrackFX_SetParam(tr1, 0, 3, 0)
RPR_TrackFX_SetParam(tr1, 0, 4, 0.5)
RPR_TrackFX_SetParam(tr1, 0, 5, 0.5)
RPR_TrackFX_SetParam(tr1, 0, 6, 0.5)

tr2 = RPR_GetTrack(0,0)

for i in range(0,11): 
 RPR_TrackFX_SetParam(tr2, 0, 5, i*0.1)
 new="b5"+"m"+str(i)+"t5"+".wav"
 render_and_rename(renderpat,newpat,render,new)
 tr3 = RPR_GetTrack(0,0)
 val1 = RPR_TrackFX_GetParam(tr3, 0, 3, 0, 1)[0]
 val2 = RPR_TrackFX_GetParam(tr3, 0, 4, 0, 1)[0]
 val3 = RPR_TrackFX_GetParam(tr3, 0, 5, 0, 1)[0]
 val4 = RPR_TrackFX_GetParam(tr3, 0, 6, 0, 1)[0]
 RPR_ShowConsoleMsg("drive:"+str(val1)[:4] +"\n")
 RPR_ShowConsoleMsg("bass:"+str(val2)[:4] +"\n")
 RPR_ShowConsoleMsg("mid:"+str(val3)[:4] +"\n")
 RPR_ShowConsoleMsg("treble:"+str(val4)[:4] +"\n")