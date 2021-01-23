from django.db import models

# Create your models here.

class Zanr(models.Model):
    nazev_zanru = models.CharField(max_length=80)

    def __str__(self):
        return "Nazev_zanru: {}".format(self.nazev_zanru)

    class Meta:
        verbose_name="Zanr"
        verbose_name_plural = "Žánry"

class Film(models.Model):
    nazev = models.CharField(max_length=200)
    rezie = models.CharField(max_length=180)
    zanr = models.ForeignKey(Zanr, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Název: {self.nazev} / Režie: {self.rezie}"

    class Meta:
        verbose_name= "Film"
        verbose_name_plural= "Filmy"