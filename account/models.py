from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user                    = models.OneToOneField(User, on_delete=models.CASCADE,null=True, related_name='profile')
    picture                 = models.ImageField(upload_to = 'account/profilePicture/', default='account/profilePicture/none/no-img.jpg', blank=True)
    occupation              = models.CharField(max_length=100)

    def __str__(self):
       return self.user.username

class Skill(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='skill')
    skill = models.CharField(max_length=100)

    def __str__(self):
       return self.skill


class Cause(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='cause')
    cause = models.CharField(max_length=100)

    def __str__(self):
       return self.cause

class NGO(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='ngo')
    name = models.CharField(max_length=100)

    def __str__(self):
       return self.name

class Address(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='address')
    address = models.CharField(max_length=128)
    zip_code = models.CharField(max_length=10)
    state = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    office_address = models.CharField(max_length=128)
    office_zip_code = models.CharField(max_length=10)
    office_state = models.CharField(max_length=20)
    office_country = models.CharField(max_length=50)

    def __str__(self):
       return self.address+' '+self.zip_code+' '+self.state+' '+self.office_address+' '+self.office_zip_code+' '+self.office_state

class Education(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='education')
    level = models.CharField(max_length=128,blank=True)
    description = models.CharField(max_length=128,blank=True)

    def __str__(self):
       return self.level+' '+self.description

class Contact(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='contact')
    office_contact = models.CharField(max_length=15,blank=True)
    personal_contact = models.CharField(max_length=15,blank=True)

    def __str__(self):
       return self.office_contact+' '+self.personal_contact

class Experiance(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='experiance')
    detail = models.CharField(max_length=500,blank=True)

    def __str__(self):
       return self.detail



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
