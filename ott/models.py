from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.conf import settings
from multiselectfield import MultiSelectField
from django.utils.text import slugify
from django.db.models.signals import pre_save
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
class viewer(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    mobile = models.BigIntegerField()
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
        return str(self.age)
class Parental_Guidance(models.Model):
    name = models.CharField(max_length=500)
    def __str__(self):
        return self.name
MY_Genre = (('Drama', 'Drama'),
              ('Comedy', 'Comedy'),
              ('Action', 'Action'),
              ('Horror', 'Horror'),
              ('Family', 'Family'),
              ('Thriller','Thriller'),
              ('Adventures', 'Adventures'),
              ('ScienceFiction', 'ScienceFiction'))
Parental = (('Language', 'Language'),
              ('Nudity', 'Nudity'),
              ('Voilence', 'Voilence'))

class Movies(models.Model):
    title = models.CharField(max_length=500)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,blank=True,null=True)
    plot = models.TextField()
    slug = models.SlugField(unique=True)
    thumbnail_image = models.ImageField(blank=True,null=True)
    banner_image = models.ImageField(blank=True,null=True)
    upload_video = models.FileField()
    price = models.FloatField()
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="likes", blank=True)
    bookmarks = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name="bookmarks",blank=True)
    language = models.ForeignKey(Languages,on_delete=models.SET_NULL,blank=True,null=True)
    genre = MultiSelectField(choices=MY_Genre,blank=True,null=True)
    age_restrication = models.ForeignKey(Age,on_delete=models.SET_NULL,blank=True,null=True)
    parental_guidance = MultiSelectField(choices=Parental,blank=True,null=True)
    draft = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    hit_count_generic = GenericRelation(HitCount, object_id_field='object_pk',
     related_query_name='hit_count_generic_relation')
    def __str__(self):
        return self.title
    def total_likes(self):
        return self.likes.count()
def create_slug(instance,new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Movies.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug,qs.first().id)
        return create_slug(instance,new_slug=new_slug)
    return slug 
def pre_save_post_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
pre_save.connect(pre_save_post_receiver,sender=Movies)
class Crew(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,blank=True,null=True)
    movie = models.ForeignKey(Movies,on_delete=models.SET_NULL,blank=True,null=True)
    name = models.CharField(max_length=300,blank=True,null=True)
    photo = models.ImageField(blank=True,null=True)
    role = models.CharField(max_length=300,blank=True,null=True)
    about = models.TextField(blank=True,null=True)
class Banner_images(models.Model):
    banner_image1 = models.ImageField(blank=True,null=True)
    banner_image1_link = models.CharField(max_length=3000)
    banner_image2 = models.ImageField(blank=True,null=True)
    banner_image2_link = models.CharField(max_length=3000)
    banner_image3 = models.ImageField(blank=True,null=True)
    banner_image3_link = models.CharField(max_length=3000)
