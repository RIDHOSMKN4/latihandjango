from django.contrib import admin
from polls.models import Question, Choice

# Register your models here.
class ChoisInline(admin.TabularInline):
     model = Choice
     extra = 3

class QuestionAdmin(admin.ModelAdmin):
     inlines = [ChoisInline]
     list_filter = ["pub_date"]
     searc_field = ["question_text"]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)