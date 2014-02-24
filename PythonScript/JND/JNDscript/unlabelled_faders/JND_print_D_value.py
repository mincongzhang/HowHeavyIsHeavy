import os,sys

data_path="E:/Zhang-Mincong/JND_unlabelled_reference_audios/subject1/data/"
data_filename="Ddata.txt"

def print_data(path,filename,content):
	f = open(path + os.sep + filename, "a+")
	f.write(content)
	f.close()

tr = RPR_GetTrack(0,0)

#treble 6
val = RPR_TrackFX_GetParam(tr, 0, 6, 0, 1)[0]
RPR_ShowConsoleMsg("Current D value is recorded.\n\n")
data_content="Recorded D value is "+str(val)[:4]+ ".\r\n\r\n"
print_data(data_path,data_filename,data_content)