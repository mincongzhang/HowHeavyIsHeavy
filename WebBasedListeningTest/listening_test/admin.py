from django.contrib import admin
from models import Mp3,WebUser,Pair


class Mp3Admin(admin.ModelAdmin):
	list_display = ('filename', 'source','weight')
	search_fields = ['weight']
	list_filter = ['weight']
	ordering = ['source','-weight']
	
	class Meta:
		pass
		
class WebUserAdmin(admin.ModelAdmin):
	fields = ('userMail', 'isEvaluate')
	list_display = ('userMail', 'isEvaluate')
	
class PairAdmin(admin.ModelAdmin):
	pass
	
admin.site.register(Mp3,Mp3Admin)
admin.site.register(WebUser,WebUserAdmin)
admin.site.register(Pair,PairAdmin)