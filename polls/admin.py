from django.contrib import admin
from .models import Question, Choice

# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    # field = ['pub_date', 'question_text']
    list_filter = ['pub_date']
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None, {"fields" : ['question_text']}),
        ('Date information', {'fields':['pub_date']})
    ]
    inlines = [ChoiceInline]

admin.site.register(Question,QuestionAdmin)
# admin.site.register(Choice)