from django.db import models
from accounts.models  import CustomUser
from django.urls import reverse

class Technika(models.Model):
    title = models.CharField(max_length=255,verbose_name= 'Antraštė')
    title_tag = models.CharField(max_length=40,blank=True, verbose_name= 'Antraštės trumpinys')
    kategorija = models.CharField(max_length=100,verbose_name= 'Kategorija')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name= 'Autorius')
    operatorius = models.BooleanField(verbose_name= 'Ar su operatorium ?')
    body = models.TextField(verbose_name= 'Aprašymas',default='Aprašymas')
    post_date = models.DateField(auto_now_add=True)
    webpuslapis = models.URLField(blank=True)
    epastas = models.EmailField(blank=True)
<<<<<<< HEAD
    nuotrauka = models.ImageField(blank=True, null=True)
=======
    nuotrauka = models.ImageField(upload_to='technika/',blank=True)
>>>>>>> fae690f7f52be2d23b7c830fab17e71186b382c5
    kontaktas = models.CharField(max_length=50,verbose_name= 'Telefonas' )

    class Meta:
        verbose_name_plural = "Technika"

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):

        return reverse('technika_detaliau', kwargs={"pk": str(self.pk)})
        # return reverse('blogas')


