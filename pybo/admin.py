from django.contrib import admin

# Register your models here.

from .models import Question, Answer

#######  검색 코드 #######
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']
class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['Answer']


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)