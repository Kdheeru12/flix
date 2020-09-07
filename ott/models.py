from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class viewer(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    mobile = models.IntegerField()
class Languages(models.Model):
    language=models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.language
class Genre(models.Model):
    geners=models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.geners
class Age(models.Model):
    age = models.IntegerField(unique=True)
    def __str__(self):
        return self.age
class Parental_Guidance(models.Model):
    name = models.CharField(max_length=500)
    def __str__(self):
        return self.name
class Movies(models.Model):
      title = models.CharField(max_length=500)
      creator = models.ForeignKey(viewer,on_delete=models.SET_NULL,blank=True,null=True)
      plot = models.TextField()
      thumbnail_image = models.ImageField(blank=True,null=True)
      banner_image = models.ImageField(blank=True,null=True)
      upload_video = models.FileField()
      price = models.FloatField()
      language = models.ForeignKey(Languages,on_delete=models.SET_NULL,blank=True,null=True)
      genre = models.ForeignKey(Genre,on_delete=models.SET_NULL,blank=True,null=True)
      age_restrication = models.ForeignKey(Age,on_delete=models.SET_NULL,blank=True,null=True)
      def __str__(self):
          return self.title
class crew(models.Model):
    creator = models.ForeignKey(viewer,on_delete=models.SET_NULL,blank=True,null=True)
    movie = models.ForeignKey(Movies,on_delete=models.SET_NULL,blank=True,null=True)
    name = models.CharField(max_length=300,blank=True,null=True)
    photo = models.IntegerField(blank=True,null=True)
    role = models.TextField()
    about = models.IntegerField(blank=True,null=True)
    
