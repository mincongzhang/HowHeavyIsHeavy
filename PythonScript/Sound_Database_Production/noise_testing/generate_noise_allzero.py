import random
import os,sys

renderpat="E:/Zhang-Mincong"
newpat="E:/Zhang-Mincong/noises"
render="xxx.wav"

def render_and_rename(renderpath,newpath,rendername,newname):
 RPR_Main_OnCommand(41823,0) #add project to render queue, using the most recent render settings
 RPR_Main_OnCommand(41207,0) #render all queued renders
 if new not in os.listdir(newpat):
  os.renames(renderpath + os.sep + rendername,newpath + os.sep + newname)
 if new in os.listdir(newpat):
  RPR_ShowConsoleMsg("\n\n"+new+" is generated in "+newpat+"\n") 

tr1 = RPR_GetTrack(0,0)
RPR_TrackFX_SetParam(tr1, 0, 3, 0)
RPR_TrackFX_SetParam(tr1, 0, 4, 0)
RPR_TrackFX_SetParam(tr1, 0, 5, 0)
RPR_TrackFX_SetParam(tr1, 0, 6, 0)

tr2 = RPR_GetTrack(0,0)

val1 = RPR_TrackFX_GetParam(tr2, 0, 3, 0, 1)[0]
val2 = RPR_TrackFX_GetParam(tr2, 0, 4, 0, 1)[0]
val3 = RPR_TrackFX_GetParam(tr2, 0, 5, 0, 1)[0]
val4 = RPR_TrackFX_GetParam(tr2, 0, 6, 0, 1)[0]
RPR_ShowConsoleMsg("drive:"+str(val1)[:4] +"\n")
RPR_ShowConsoleMsg("bass:"+str(val2)[:4] +"\n")
RPR_ShowConsoleMsg("mid:"+str(val3)[:4] +"\n")
RPR_ShowConsoleMsg("treble:"+str(val4)[:4] +"\n")

new="b0m0t0"+".wav"
render_and_rename(renderpat,newpat,render,new)