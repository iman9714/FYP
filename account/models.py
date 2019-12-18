from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user                    = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    ic                      = models.CharField(max_length=12, blank=True)
    personal_contact        = models.CharField(max_length=15,blank=True)
    office_contact          = models.CharField(max_length=15,blank=True)
    picture                 = models.ImageField(upload_to = 'account/profilePicture/', default = 'account/profilePicture/None/no-img.jpg',blank=True)
    home_address_line1      = models.CharField(max_length=100,blank=True)
    home_address_line2      = models.CharField(max_length=100,blank=True)
    home_zip_code           = models.CharField(max_length=10,blank=True)
    home_state              = models.CharField(max_length=100,blank=True)
    home_country            = models.CharField(max_length=100,blank=True)
    work_address_line1      = models.CharField(max_length=100,blank=True)
    work_address_line2      = models.CharField(max_length=100,blank=True)
    work_zip_code           = models.CharField(max_length=10,blank=True)
    work_state              = models.CharField(max_length=100,blank=True)
    work_country            = models.CharField(max_length=100,blank=True)
    job                     = models.CharField(max_length=100,blank=True)
    qualification           = models.CharField(max_length=100,blank=True)
    fee_type                = models.CharField(max_length=5,blank=True)
    skill                   = models.CharField(max_length=200,blank=True)#multivelue
    cause                   = models.CharField(max_length=200,blank=True)#multivelue


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Skill(models.Model):
    name = models.CharField(max_length=100,blank=True)

class Cause(models.Model):
    name = models.CharField(max_length=100,blank=True)
