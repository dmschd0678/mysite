import datetime
from django.contrib import admin
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?'
    )
    
    def was_published_recently(self):
        now = timezone.now()
        # return self.pub_date >= timezone.now() - timezone.timedelta(days = 1)
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    # was_published_recently.admin_order_field = 'pub_date'
    # was_published_recently.boolean = True
    # was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text