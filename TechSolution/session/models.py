from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    BLOOD_GROUP = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    )

    CATEGORY = (
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')  # ✅ related_name fixed
    birth_date = models.DateField(null=True, blank=True)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)
    address = models.CharField(max_length=150)
    phone = models.CharField(max_length=13)
    nationality = models.CharField(max_length=30)
    religion = models.CharField(max_length=50)
    biodata = models.TextField()
    profession = models.CharField(max_length=50, choices=CATEGORY, null=True)
    image = models.ImageField(default='default.jpg', upload_to='session/images')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

# ✅ Signals to create and save profile automatically
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()
