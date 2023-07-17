from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
from django.urls import reverse
class Snack(models.Model):
    title  = models.CharField(max_length=255 , help_text='snack name')
    description  = models.CharField(max_length=255 , help_text='snack description')
    purchaser = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('snacks_detail',args=[self.id])