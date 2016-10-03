from django.contrib import admin
#from . import models
from .models import Question, Choice

# Register your models here.

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3
    
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('pub_date','question_text', 'was_published_recently')
    #fields = ['pub_date','question_text']
    fieldsets = [
                 (None,   {'fields' : ['question_text']}),
                 ('Date Information', {'fields' : ['pub_date'], 'classes' : ['collapse']}),
                 ]
    inlines = [ChoiceInLine]
    list_filter = ['pub_date']
    search_fields = ['question_text']

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text',) 
   
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)