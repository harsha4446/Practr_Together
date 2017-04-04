from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from time import timezone
import datetime

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, name, phoneno):
        if not email:
            raise ValueError("No username entered")
        email = self.normalize_email(email)
        new_user = self.model(email=email,name=name, phoneno=phoneno)
        new_user.set_password(password)
        new_user.is_staff=False
        new_user.save(using=self._db)
        return new_user

    def create_superuser(self, email, password, name, phoneno):
        if not email:
            raise ValueError("No username entered")
        email = self.normalize_email(email)
        new_user = self.model(email=email,name=name, phoneno=phoneno)
        new_user.set_password(password)
        new_user.is_staff = True
        new_user.is_superuser = True
        new_user.save(using=self._db)
        return new_user


def upload_loction(object, filename):
    return "%s/%s" %(object.email , filename)

class student(AbstractBaseUser):
    email = models.EmailField(max_length=100,unique=True)
    name=models.CharField(max_length=50)
    password=models.CharField(max_length=200)
    phoneno=models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    activated = models.BooleanField(default=False)
    judge = models.BooleanField(default=False)
    designation = models.CharField(max_length=100,default='')
    industry_exp = models.PositiveSmallIntegerField(default=0)
    about = models.CharField(max_length=500,default='')
    dob = models.DateField(default=datetime.date.today)
    experience = models.PositiveSmallIntegerField(default=0)
    location = models.CharField(max_length=500, default='')
    degree = models.CharField(max_length=100, default='')
    college = models.CharField(max_length=150, default='')
    year = models.CharField(max_length=10, choices=(('First', 'First'),
                                                    ('Second', 'Second'),
                                                    ('Third', 'Third')),
                            default='First')
    website = models.EmailField(default='dummy@dummy.com')
    profile_picture = models.ImageField(upload_to=upload_loction,null=True,blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','phoneno']
    objects=CustomUserManager()

    def get_absolute_url(self):
        return "/user/%s/" %self.email

    def get_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def get_phoneno(self):
        return self.phoneno

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def email_user(self,subject,message,from_mail=None):
        send_mail(subject,message,from_mail,[self.email])


class student_scores(models.Model):
    username=models.OneToOneField(student,on_delete=models.CASCADE)
    creativiy=models.IntegerField(default=0)
    presentation=models.IntegerField(default=0)
    overall=models.IntegerField(default=0)

    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.username


class colleges(models.Model):
    name = models.CharField(max_length=150,default='',unique=True)
    college_number = models.CharField(max_length=10)
    college_email = models.EmailField(default='')

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class clubs(models.Model):
    name = models.ForeignKey(colleges,on_delete=models.CASCADE,default='')
    club_name = models.CharField(max_length=100,default='')

    def __str__(self):
        return self.club_name

    def __unicode__(self):
        return self.club_name
