from django.db import models

# Create your models here.


class Header(models.Model):
    titre = models.CharField(max_length=100)
    image = models.ImageField(upload_to='header_images/')
    texte = models.TextField()


    def __str__(self):
        return self.titre
    
class PetitModel(models.Model):
    image = models.ImageField(upload_to='PetitModel_images/')
    sujet = models.CharField(max_length=100)
    texte = models.TextField()

    def __str__(self):
        return self.sujet

class RowGx70(models.Model):
    image = models.ImageField(upload_to='row_gx_70/')
    texte = models.TextField()
    photo_profil = models.ImageField(upload_to='row_gx_70/')
    nom = models.CharField(max_length=70)
    fonction = models.CharField(max_length=70)

    def __str__(self):
        return self.nom
    
class Partenaires(models.Model):
    texte = models.CharField(max_length=200)
    image = models.ImageField(upload_to='partenaire_images/')

    def __str__(self):
        return self.texte
    
class Section(models.Model):
    titre = models.CharField(max_length=100)
    texte = models.TextField()
    image = models.ImageField(upload_to='section_image/')

    def __str__(self):
        return self.titre
    
class Professeur(models.Model):
    nom = models.CharField(max_length=100)
    matiere = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='professeurs_image/')

    def __str__(self):
        return self.nom
    

class Base(models.Model):
    telephone = models.IntegerField
    email = models.EmailField
    logo = models.ImageField(upload_to='base_image/')

    def __str__(self):
        return self.email