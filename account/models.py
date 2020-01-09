from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user                    = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    picture                 = models.ImageField(upload_to = 'account/profilePicture/', default='account/profilePicture/none/no-img.jpg', blank=True)
    occupation              = models.CharField(max_length=100,blank=True)

class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='skill')
    skill = models.CharField(max_length=100,blank=True)

class Cause(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='cause')
    cause = models.CharField(max_length=100,blank=True)

class NGO(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='ngo')
    name = models.CharField(max_length=100,blank=True)

class Address(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='address')
    address = models.CharField(max_length=128,blank=True)
    zip_code = models.CharField(max_length=10,blank=True)
    state = models.CharField(max_length=20,blank=True)
    country = models.CharField(max_length=50,blank=True)
    office_address = models.CharField(max_length=128,blank=True)
    office_zip_code = models.CharField(max_length=10,blank=True)
    office_state = models.CharField(max_length=20,blank=True)
    office_country = models.CharField(max_length=50,blank=True)

class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='education')
    level = models.CharField(max_length=128,blank=True)
    description = models.CharField(max_length=128,blank=True)

class Contact(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='contact')
    office_contact = models.CharField(max_length=15,blank=True)
    personal_contact = models.CharField(max_length=15,blank=True)

class Experiance(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='experiance')
    detail = models.CharField(max_length=500,blank=True)

#profile
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



#profile detail
@receiver(post_save, sender=Profile)
def create_user_Skill(sender, instance, created, **kwargs):
    if created:
        Skill.objects.create(profile=instance)

@receiver(post_save, sender=Profile)
def create_user_Cause(sender, instance, created, **kwargs):
    if created:
        Cause.objects.create(profile=instance)

@receiver(post_save, sender=Profile)
def create_user_NGO(sender, instance, created, **kwargs):
    if created:
        NGO.objects.create(profile=instance)

@receiver(post_save, sender=Profile)
def create_user_Address(sender, instance, created, **kwargs):
    if created:
        Address.objects.create(profile=instance)

@receiver(post_save, sender=Profile)
def create_user_Education(sender, instance, created, **kwargs):
    if created:
        Education.objects.create(profile=instance)

@receiver(post_save, sender=Profile)
def create_user_Contact(sender, instance, created, **kwargs):
    if created:
        Contact.objects.create(profile=instance)

@receiver(post_save, sender=Profile)
def create_user_Experiance(sender, instance, created, **kwargs):
    if created:
        Experiance.objects.create(profile=instance)
