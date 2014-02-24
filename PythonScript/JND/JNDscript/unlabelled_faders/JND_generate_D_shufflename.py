#this function will randomly set 3 parameters(drive,mid,treble)
#and generate five audios that have treble value 0.1 0.3 0.5 0.7 0.9 respectively as reference audios

import random
import os,sys

renderpat="E:/Zhang-Mincong"
newpat="E:/Zhang-Mincong/JND_unlabelled_reference_audios/subject1/D"
render="xxx.wav"

data_path="E:/Zhang-Mincong/JND_unlabelled_reference_audios/subject1/data/"
data_filename="Ddata.txt"

def print_data(path,filename,content):
	f = open(path + os.sep + filename, "a+")
	f.write(content)
	f.close()

def render_and_rename(renderpath,newpath,rendername,newname):
 RPR_Main_OnCommand(41823,0) #add project to render queue, using the most recent render settings
 RPR_Main_OnCommand(41207,0) #render all queued renders
 if new not in os.listdir(newpat):
  os.renames(renderpath + os.sep + rendername,newpath + os.sep + newname)
 if new in os.listdir(newpat):
  RPR_ShowConsoleMsg(new+" is generated in "+newpat+"\n\n") 

def gaussian_random():
 running = True
 while running:
  y=random.gauss(0.5, 0.25)
  if (y >= 0 and y <= 1):
   return y
   running = False

RPR_ShowConsoleMsg( "randomly set 3 parameters \n" )

tr1 = RPR_GetTrack(0,0)
#reset drive, bass, treble (position: 3 5 6) to some value 
RPR_TrackFX_SetParam(tr1, 0, 3, gaussian_random())
RPR_TrackFX_SetParam(tr1, 0, 4, gaussian_random())
RPR_TrackFX_SetParam(tr1, 0, 5, gaussian_random())
#RPR_TrackFX_SetParam(tr1, 0, 6, gaussian_random())

#get and print new settings
tr2 = RPR_GetTrack(0,0)

val3 = RPR_TrackFX_GetParam(tr2, 0, 3, 0, 1)[0]
data_content="drive:"+str(val3)[:4] +"\n"
print_data(data_path,data_filename,data_content)

val4 = RPR_TrackFX_GetParam(tr2, 0, 4, 0, 1)[0]
data_content="bass:"+str(val4)[:4] +"\n"
print_data(data_path,data_filename,data_content)

val5 = RPR_TrackFX_GetParam(tr2, 0, 5, 0, 1)[0]
data_content="mid:"+str(val5)[:4] +"\n"
print_data(data_path,data_filename,data_content)

#val6 = RPR_TrackFX_GetParam(tr2, 0, 6, 0, 1)[0]
#RPR_ShowConsoleMsg("treble:"+str(val6)[:4] +"\n")

RPR_ShowConsoleMsg("\n Generating reference audios:\n")

namelist = [0,1,2,3,4]
random.shuffle(namelist)

#mid 0.1 0.3 0.5 0.7 0.9
for i in range(1,6): 
 RPR_TrackFX_SetParam(tr2, 0, 6, (i*0.2-0.1))
 tr3 = RPR_GetTrack(0,0)
 new="D"+str(namelist[i-1])+".wav"
 render_and_rename(renderpat,newpat,render,new)
 mid_val = RPR_TrackFX_GetParam(tr3, 0, 6, 0, 1)[0]
 data_content=new+" treble value:"+str(mid_val)[:4]+"\n\n"
 print_data(data_path,data_filename,data_content)
