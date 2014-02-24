#coding=utf8
import os
from django.conf import settings
import math

def getmp3info():
	static_dir = settings.STATICFILES_DIRS[0]
	mp3_source = os.listdir(static_dir+"/mp3")
	mp3_dict = {}
	for source in mp3_source:
		mp3_dict[source] = os.listdir(static_dir+"/mp3/"+source)
	return mp3_dict
	
def getDistance(d1,d2):
	return math.sqrt(math.pow(int(d1[0]) - int(d2[0]),2) + math.pow(int(d1[1])-int(d2[1]),2)+ math.pow(int(d1[2])-int(d2[2]),2)+ math.pow(int(d1[3])-int(d2[3]),2) )
	

from email.Header import Header
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from smtplib import SMTP

class WebSMTP:
	def __init__(self,user,pwd):
		self.msg = MIMEMultipart()
		self.smtp=SMTP("smtp.qq.com")
		#self.smtp.docmd("EHLO server")
		#self.smtp.starttls()
		self.smtp.ehlo()
		self.smtp.login(user,pwd)
		self.msg["From"]=user
	
	def sendmail(self,to,subject,txt,attach=None):
		self.msg["Accept-Language"] = "zh_CN"
		self.msg["Accept-Charset"]="ISO-8859-1,utf-8"
		txt=MIMEText(txt)
		txt.set_charset("utf-8")
		self.msg["To"]=to
		self.msg["Subject"]=subject
		self.msg.attach(txt)
		self.smtp.sendmail(self.msg["From"],self.msg["To"],self.msg.as_string())