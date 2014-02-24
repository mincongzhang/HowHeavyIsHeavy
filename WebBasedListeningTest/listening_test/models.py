from django.db import models

class Mp3(models.Model):
	filename = models.CharField(max_length=200)
	source   = models.CharField(max_length=200)
	weight  = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.filename
		
	
class WebUser(models.Model):
	userMail = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	isEvaluate = models.CharField(max_length=50)
	evaluate = models.TextField()
	
	def __unicode__(self):
		return self.userMail
		
class Pair(models.Model):
	user = models.ForeignKey(WebUser)
	value = models.CharField(max_length=255)
	
	def __unicode__(self):
		return self.value