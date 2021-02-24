from django.db import models
from accounts.models  import CustomUser
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
from datetime import datetime, date
# from django.core.urlresolvers import reverse

class Klausimai(models.Model):
    klausimo_antraste = models.CharField(max_length=255,verbose_name= 'Antraštė')
    klausimo_santraupa = models.CharField(max_length=255,blank=True, verbose_name= 'Antraštės trumpinys')
    autorius = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name= 'Autorius')
    tekstas = models.TextField(verbose_name= 'Tekstas',default='Tekstas')
    teksto_data = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Klausimai"

    def __str__(self):
        return self.klausimo_antraste + ' | ' + str(self.autorius)

    def get_absolute_url(self):
        # print (reverse(str(self.id)))
        return reverse('oro_temperatura', kwargs={"pk": str(self.pk)})
        # return reverse('blogas')
        # return reverse('article-detail', [self.id,])