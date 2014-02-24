#coding=utf-8
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render_to_response,redirect

import random
from mycollections import Counter
import toolbox
from models import Mp3,WebUser,Pair

import os

txtpath = os.path.join(os.path.dirname(__file__),'static/txt/')


mailname='283539948@qq.com'
mailpass='xxx'


s1_total = set()
s2_total = set()

def GenerateMetalPW():
	password=random.choice(["Metallica","Pantera","Kreator", "Slayer","Kiss","Angra", "Machinehead", "LedZeppelin","BlackSabbath","IronMaiden","Megadeth","DeepPurple","Burzum","Nightwish","Emperor"]) 
        number=str(random.randint(0,9))+str(random.randint(0,9))
	return password+number

def homepage(request):
	uname = request.session.get("username","")
	vars = {}
	vars["uname"] = uname
	return render_to_response('homepage.html',vars)

def info_collection(request):
	uname = request.session.get("username","")
	if uname == "":
		return redirect("/register/")
	vars = {}
	vars["uname"] = uname
	if request.method == "POST":
		question = request.POST.get("questionSelect",'')
		user = WebUser.objects.filter(userMail=uname).update(isEvaluate=question)
		f = open(txtpath+"%s.txt"%uname,"w+")
		f.write(uname+","+question+"\n")
		f.close()
		return redirect("/question/plus/1")
	user = WebUser.objects.filter(userMail=uname)	
	isEvaluate = user.values()[0]["isEvaluate"]
	if isEvaluate == "":
		return render_to_response('info_collection.html',vars)
	else:
		return redirect("/question/plus/1")

def question_ahead(request, offset):
	uname = request.session.get("username","")
	if uname == "":
		return render_to_response("register.html")
	if request.session.get("source1",""):
		source1 = request.session.get("source1")
	else:
		source1 = "source1"
	if request.session.get("source2",""):
		source2 = request.session.get("source2")
	else:
		source2 = "source2"
	mp3list_indb_source1 = Mp3.objects.filter(source=source1)
	mp3list_indb_source2 = Mp3.objects.filter(source=source2)
	
	if request.COOKIES.has_key("songselected"):
		songselected = request.COOKIES["songselected"]
		songselected = set(eval(songselected))
	else:
		songselected = set()
		
	if request.COOKIES.has_key("score"):
		d = request.COOKIES["score"]
		d = eval(d)
	else:
		d = {}
		
	temp_songs = set()
	for select in songselected:
		temp_songs.update(Mp3.objects.filter(filename=select))
	
	s1_total = set(mp3list_indb_source1)
	mp3list_indb_source1 = list(s1_total.difference(temp_songs))
	
	s2_total = set(mp3list_indb_source2)
	mp3list_indb_source2 = list(s2_total.difference(temp_songs))
	
	if request.method == "POST":
		firstsong = request.POST.get("firstsong","")
		secondsong=request.POST.get("secondsong","")
		songname1 = request.POST.get("songname1","")
		songname2 = request.POST.get("songname2","")
		songselect= request.POST.get("songselect","")
		try:
			offset = int(offset)
		except ValueError:
			raise Http404()
		if offset >21:
			offset = 21
		firstsong = int(firstsong)
		secondsong = int(secondsong)
		if songselect == songname1:
			if firstsong <= secondsong:
				d = {songselect:int(secondsong)+1}
			#if firstsong > secondsong:
			#	#d.update({offset-1:{songname1:int(firstsong),songname2:int(secondsong)}})
			#else:
			#	d.update({offset-1:{songname1:int(secondsong)+1,songname2:int(secondsong)}})		
		else:
			if secondsong <= firstsong:
				d = {songselect:int(firstsong)+1}
			#if secondsong > firstsong:
			#	d.update({offset-1:{songname1:int(firstsong),songname2:int(secondsong)}})
			#else:
			#	d.update({offset-1:{songname1:int(firstsong),songname2:int(firstsong)+1}})
			#d.update({offset-1:{songname1:firstsong,songname2:int(secondsong)+1}})
		[Mp3.objects.filter(filename=x).update(weight=int(y)) for x,y in d.items()]
		f = open(txtpath+"%s.txt"%uname,"a")
		f.write(songname1+","+songname2+","+songselect+"\n")
		f.close()
		next = offset + 1
		
		if offset <= 10:
			l = []
			for s1 in mp3list_indb_source1:
				l.append(s1.weight)
			c = Counter(l)
			sameWeight = []
			for count in c:
				if c[count] >= 2:
					sameWeight.append(count)
			if len(sameWeight) >0:
				mp3_choice = random.choice(sameWeight)
				#songs  = random.sample([item for item in mp3list_indb_source1 if item.weight == mp3_choice],2)
				song1  = random.choice([item for item in mp3list_indb_source1 if item.weight == mp3_choice])
				songselected.add(song1.filename)
				d1 = ",".join(song1.filename.split(".")[0][:-1]).split(",")
				#songleft = [item for item in mp3list_indb_source1 if item.weight == mp3_choice]
				songleft = set([item for item in mp3list_indb_source1 if item.weight == mp3_choice]).difference(set([song1]))
				#songleft.pop(songleft.index(song1))
				songleft_alpha = [",".join(s.filename.split(".")[0][:-1]).split(",") for s in songleft]
				maxDistance = [[toolbox.getDistance(d1,n),n] for n in songleft_alpha ]
				temp_list = []
				for temp in maxDistance:
					temp_list.append(temp[0])
				#song2 = "".join([n for n in maxDistance if n[0] == max(temp_list)][1])+song1.filename.split(".")[0][-1:]
				song2_list = ["".join(n[1]) for n in maxDistance if n[0] == max(temp_list)]
				#song2 may more than one
				if len(song2_list) >= 2 :
					song2_list = song2_list[0]
				else:
					song2_list = song2_list[0]
				song2_name = song2_list+ song1.filename.split(".")[0][-1:]+".mp3"
				song2 = [item for item in mp3list_indb_source1 if item.filename == song2_name][0]
				songselected.add(song2.filename)
				songs = [song1,song2]
				#uname begin
				user = WebUser.objects.get(userMail=uname)
				val = song1.filename.split(".")[0][:-1]+","+song2.filename.split(".")[0][:-1]
				pair = Pair(user=user,value=val)
				pair.save()
				#songselected.add(songs[0].filename)
				#songselected.add(songs[1].filename)
			else:
				songs = random.sample(mp3list_indb_source1,2)
				songselected.add(songs[0].filename)
				songselected.add(songs[1].filename)
		else:
			l = []
			for s2 in mp3list_indb_source2:
				l.append(s2.weight)
			c = Counter(l)
			sameWeight = []
			for count in c:
				if c[count] >= 2:
					sameWeight.append(count)
				pass
			if len(sameWeight) >0:
				mp3_choice = random.choice(sameWeight)
				#songs = random.sample(mp3list_indb_source2.filter(weight=mp3_choice),2)
				#songs  = random.sample([item for item in mp3list_indb_source2 if item.weight == mp3_choice],2)
				song1  = random.choice([item for item in mp3list_indb_source2 if item.weight == mp3_choice])
				#songselected.add(song1.filename)
				d1 = ",".join(song1.filename.split(".")[0][:-1]).split(",")
				#songleft = [item for item in mp3list_indb_source1 if item.weight == mp3_choice]
				songleft = set([item for item in mp3list_indb_source2 if item.weight == mp3_choice]).difference(set([song1]))
				#songleft.pop(songleft.index(song1))
				songleft_alpha = [",".join(s.filename.split(".")[0][:-1]).split(",") for s in songleft]
				maxDistance = [[toolbox.getDistance(d1,n),n] for n in songleft_alpha ]
				temp_list = []
				for temp in maxDistance:
					temp_list.append(temp[0])
				#song2 = "".join([n for n in maxDistance if n[0] == max(temp_list)][1])+song1.filename.split(".")[0][-1:]
				#song2_list = ["".join(n[1]) for n in maxDistance if n[0] == max(temp_list)]
				#song2 may more than one
				#if len(song2_list) >= 2 :
				#	song2_list = song2_list[0]
				#else:
				#	song2_list = song2_list[0]
				#song2_name = song2_list+ song1.filename.split(".")[0][-1:]+".mp3"
				#song2 = [item for item in mp3list_indb_source2 if item.filename == song2_name][0]
				#songselected.add(song2.filename)
				#songs = [song1,song2]
				
				user = WebUser.objects.get(userMail=uname)
				pairs = Pair.objects.filter(user=user)
				for pair in pairs:
					for distance in temp_list:
						song2_list = ["".join(n[1]) for n in maxDistance if n[0] == max(temp_list)]
						if len(song2_list) >= 2 :
							song2_list = song2_list[0]
						else:
							song2_list = song2_list[0]
						song2_name = song2_list+ song1.filename.split(".")[0][-1:]+".mp3"
						song2 = [item for item in mp3list_indb_source2 if item.filename == song2_name][0]
						#check the select in pair table
						
						#song1.filename.split(".")[0][:-1]+","+song2.filename.split(".")[0][:-1]
						temp_songname1 = song1.filename.split(".")[0][:-1]
						temp_songname2 = song2.filename.split(".")[0][:-1]
						print temp_songname1+","+temp_songname2+"="+pair.value
						if temp_songname1+","+temp_songname2 == pair.value or temp_songname2+","+temp_songname1 == pair.value:
							temp_list.remove(max(temp_list))
							print "in continue:",temp_list
							continue
						else:
							print "no match found!select song2"
							songselected.add(song1.filename)
							songselected.add(song2.filename)
							songs = [song1,song2]
				else:
					if "songs" not  in locals():
						songs = random.sample(mp3list_indb_source2,2)
						songselected.add(songs[0].filename)
						songselected.add(songs[1].filename)
					
				#songselected.add(songs[0].filename)
				#songselected.add(songs[1].filename)
			else:
				songs = random.sample(mp3list_indb_source2,2)
				songselected.add(songs[0].filename)
				songselected.add(songs[1].filename)
		#mp3list_indb = Mp3.objects.all()
		#mp3list = []
		#for mp3 in mp3list_indb:
		#	mp3list.append(mp3)
		#if len(mp3list) >= 2:
		#	songs = random.sample(mp3list,2)
		#else:
		#	songs = []
		vars = {}
		vars["question_offset"] = offset
		vars["next_question"] = next
		vars["songs"] = songs
		response = render_to_response('question_ahead.html', vars)
		response.set_cookie("offset",offset)
		response.set_cookie("score",str(d))
		response.set_cookie("songselected",list((mp3 for mp3 in songselected)))
		return response
		
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	if offset >21:
			offset = 21
	next = offset + 1
	
	if offset <= 10:
		l = []
		for s1 in mp3list_indb_source1:
			l.append(s1.weight)
		c = Counter(l)
		sameWeight = []
		for count in c:
			if c[count] >= 2:
				sameWeight.append(count)
			pass
		if len(sameWeight) >0:
			mp3_choice = random.choice(sameWeight)
			#songs = random.sample(mp3list_indb_source1.filter(weight=mp3_choice),2)
			#songs  = random.sample([item for item in mp3list_indb_source1 if item.weight == mp3_choice],2)
			song1  = random.choice([item for item in mp3list_indb_source1 if item.weight == mp3_choice])
			songselected.add(song1.filename)
			d1 = ",".join(song1.filename.split(".")[0][:-1]).split(",")
			#songleft = [item for item in mp3list_indb_source1 if item.weight == mp3_choice]
			songleft = set([item for item in mp3list_indb_source1 if item.weight == mp3_choice]).difference(set([song1]))
			#songleft.pop(songleft.index(song1))
			songleft_alpha = [",".join(s.filename.split(".")[0][:-1]).split(",") for s in songleft]
			maxDistance = [[toolbox.getDistance(d1,n),n] for n in songleft_alpha ]
			temp_list = []
			for temp in maxDistance:
				temp_list.append(temp[0])
			#song2 = "".join([n for n in maxDistance if n[0] == max(temp_list)][1])+song1.filename.split(".")[0][-1:]
			song2_list = ["".join(n[1]) for n in maxDistance if n[0] == max(temp_list)]
			#song2 may more than one
			if len(song2_list) >= 2 :
				song2_list = song2_list[0]
			else:
				song2_list = song2_list[0]
			song2_name = song2_list+ song1.filename.split(".")[0][-1:]+".mp3"
			song2 = [item for item in mp3list_indb_source1 if item.filename == song2_name][0]
			songselected.add(song2.filename)
			songs = [song1,song2]
			#uname
			user = WebUser.objects.get(userMail=uname)
			val = song1.filename.split(".")[0][:-1]+","+song2.filename.split(".")[0][:-1]
			pair = Pair(user=user,value=val)
			pair.save()
			#songselected.add(songs[0].filename)
			#songselected.add(songs[1].filename)
		else:
			songs = random.sample(mp3list_indb_source1,2)
			songselected.add(songs[0].filename)
			songselected.add(songs[1].filename)
			user = WebUser.objects.get(userMail=uname)
			val = songs[0].filename.split(".")[0][:-1]+","+songs[1].filename.split(".")[0][:-1]
			pair = Pair(user=user,value=val)
			pair.save()
	else:
		l = []
		for s2 in mp3list_indb_source2:
			l.append(s2.weight)
		c = Counter(l)
		sameWeight = []
		for count in c:
			if c[count] >= 2:
				sameWeight.append(count)
			pass
		if len(sameWeight) >0:
			mp3_choice = random.choice(sameWeight)
			#songs = random.sample(mp3list_indb_source2.filter(weight=mp3_choice),2)
			#songs  = random.sample([item for item in mp3list_indb_source2 if item.weight == mp3_choice],2)
			song1  = random.choice([item for item in mp3list_indb_source2 if item.weight == mp3_choice])
			
			d1 = ",".join(song1.filename.split(".")[0][:-1]).split(",")
			#songleft = [item for item in mp3list_indb_source1 if item.weight == mp3_choice]
			songleft = set([item for item in mp3list_indb_source2 if item.weight == mp3_choice]).difference(set([song1]))
			#songleft.pop(songleft.index(song1))
			songleft_alpha = [",".join(s.filename.split(".")[0][:-1]).split(",") for s in songleft]
			maxDistance = [[toolbox.getDistance(d1,n),n] for n in songleft_alpha ]
			temp_list = []
			for temp in maxDistance:
				temp_list.append(temp[0])
			#song2 = "".join([n for n in maxDistance if n[0] == max(temp_list)][1])+song1.filename.split(".")[0][-1:]
			
			#song2_list = ["".join(n[1]) for n in maxDistance if n[0] == max(temp_list)]
			#song2 may more than one
			#if len(song2_list) >= 2 :
			#	song2_list = song2_list[0]
			#else:
			#	song2_list = song2_list[0]
			#song2_name = song2_list+ song1.filename.split(".")[0][-1:]+".mp3"
			#song2 = [item for item in mp3list_indb_source2 if item.filename == song2_name][0]
			#songselected.add(song2.filename)
			#songs = [song1,song2]
			user = WebUser.objects.get(userMail=uname)
			pairs = Pair.objects.filter(user=user)
			for pair in pairs:
				for distance in temp_list:
					song2_list = ["".join(n[1]) for n in maxDistance if n[0] == max(temp_list)]
					if len(song2_list) >= 2 :
						song2_list = song2_list[0]
					else:
						song2_list = song2_list[0]
					song2_name = song2_list+ song1.filename.split(".")[0][-1:]+".mp3"
					song2 = [item for item in mp3list_indb_source2 if item.filename == song2_name][0]
					#check the select in pair table
					if song1.filename+","+song2.filename == pair.value or song2.filename+","+song1.filename == pair.value:
						temp_list.remove(max(temp_list))
						continue
					else:
						songselected.add(song1.filename)
						songselected.add(song2.filename)
						songs = [song1,song2]
			else:
				if "songs" not  in locals():
					songs = random.sample(mp3list_indb_source2,2)
					songselected.add(songs[0].filename)
					songselected.add(songs[1].filename)
		else:
			songs = random.sample(mp3list_indb_source2,2)
			songselected.add(songs[0].filename)
			songselected.add(songs[1].filename)
	#mp3list_indb = Mp3.objects.all()
	#mp3list = []
	#for mp3 in mp3list_indb:
	#	mp3list.append(mp3)
	#if len(mp3list) >= 2:
	#	songs = random.sample(mp3list,2)
	#else:
	#	songs = []
	vars = {}
	vars["question_offset"] = offset
	vars["next_question"] = next
	vars["songs"] = songs
	response = render_to_response('question_ahead.html', vars)
	response.set_cookie("offset",offset)
	response.set_cookie("score",str(d))
	response.set_cookie("songselected",list((mp3 for mp3 in songselected)))
	return response
	
def login(request):
	vars = {}
	if request.session.get("username","") != '':
		return redirect("/info_collection")
	if request.method == "POST":
		msg = ''
		username = request.POST.get("username","")
		password = request.POST.get("password","")
		if username == "" or password == '':
			msg = "username or password null!"
			vars["msg"] = msg
			return render_to_response("login.html",vars)
		webusers = WebUser.objects.all()
		for user in webusers:
			if user.userMail == username and user.password == password:
				if request.COOKIES.has_key("offset"):
					offset = request.COOKIES["offset"]
				else:
					offset = 1
				request.session["username"] = username
				return redirect("/question/plus/%s"%offset)	
		msg = "username or password error"
		vars["msg"] = msg
	return render_to_response('login.html',vars)
	
def register(request):
	vars = {}
	if request.method == "POST":
		username = request.POST.get("username","")
		password = GenerateMetalPW()
		if username == '' or password == '':
			return render_to_response("register.html",vars)
		user = WebUser.objects.filter(userMail=username)
		if len(user) > 0:
			vars["msg"] = "user exist!"
			return render_to_response("register.html",vars)
		reg_user = WebUser(userMail=username,password=password,evaluate='')
		reg_user.save()
		request.session["username"] = username
		mail = toolbox.WebSMTP(mailname,mailpass)
		mail.sendmail(username,"Your account information in listening test","username:%s\npassword:%s\nplease use the password provided to login"%(username,password))
		return redirect("/info_collection")
	return render_to_response("register.html",vars)
	
def logout(request):
	try:
		del request.session["username"]
	except KeyError:
		pass
	return redirect("/")
	
def answer(request):
	if request.method == "POST":
		if request.COOKIES.has_key("score"):
			score = request.COOKIES["score"]
			score_dict = eval(score)
			if len(score_dict) <20:
				offset = list(set([i for i in xrange(1,21)]).difference(set(score_dict.keys())))[0]
				return redirect("/question/plus/%s"%offset)	
				#return HttpResponse("you have %s need to be answered"%(str(20-len(score_dict))))
			else:
				print "score:",score
				mp3_indb = Mp3.objects.all()
				mp3_array = []
				for _,val in score_dict.items():
					for mp3name,score in val.items():
						mp3_array.append([mp3name,score])
				[Mp3.objects.filter(filename=fn).update(weight=int(av)) for fn,av in mp3_array]
				#for item in mp3_indb:
				#	for ma in mp3_array:
				#		if item.filename == ma[0]:
				#			item.weight = int(item.weight)+int(ma[1])
				#			item.save()
				response = HttpResponse("answer successfull,thank your!<a href='/'>back to home</a>")
				response.delete_cookie('score')
				songselected.clear()
				return response
		else:
			return HttpResponse("score info not found!")
	return HttpResponse("not allowed!")
	
def back(request):
	#songselected.clear()
	response = HttpResponseRedirect("/")
	response.delete_cookie('songselected')
	response.delete_cookie('offset')
	uname = request.session.get("username","")
	if uname != '':
		user = WebUser.objects.get(userMail=uname)
		pairs = Pair.objects.filter(user=user)
		pairs.delete()
	return response
	
def mp3(request):
	mp3_dict = toolbox.getmp3info()
	source_list = []
	for key in mp3_dict.keys():
		source_list.append(key)
	request.session["source1"] = source_list[0]
	request.session["source2"] = source_list[1]
	mp3_list = []
	for val in mp3_dict.values():
		for v in val:
			mp3_list.append(v)
	mp3_indb = Mp3.objects.all()
	mp3_set = set(mp3_list)
	mp3d_set = set()
	for item in mp3_indb:
		mp3d_set.add(item.filename)
	new_set = mp3_set.difference(mp3d_set)
	if len(new_set) != 0:
		for key,val in mp3_dict.items():
			for fn in list(new_set):
				if fn in val:
					m = Mp3(filename=fn,weight=0,source=key)
					m.save()
	#if len(new_set) != 0:
	#	for music in new_set:
	#		m = Mp3(filename=music,weight=0)
	#		m.save()
		return HttpResponse("Audios scanning finished! <a href='/'>Home</a>")
	return HttpResponse("No new audios! <a href='/'>Home</a>")
