from django.db import models
from accounts.models  import CustomUser
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from datetime import datetime, date
# from django.core.urlresolvers import reverse

class Post(models.Model):
    title = models.CharField(max_length=255,verbose_name= 'Antraštė')
    title_tag = models.CharField(max_length=255,blank=True, verbose_name= 'Antraštės trumpinys')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name= 'Autorius')
    body = models.TextField(verbose_name= 'Tekstas',default='Tekstas')
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        # print (reverse(str(self.id)))
        return reverse('article-detail', kwargs={"pk": str(self.pk)})
        # return reverse('blogas')
        # return reverse('article-detail', [self.id,])


      # def get_absolute_url(self):
      # return reverse('Main', kwargs={'pk': self.pk, 'slug': self.slug })