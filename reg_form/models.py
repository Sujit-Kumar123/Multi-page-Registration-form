from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from django.core.exceptions import ValidationError

# Create your models here.
def validate_image1(image):
    file_size=image.file.size
    limit_mb=4
    if file_size>limit_mb*1024*1024:
        raise ValidationError("max size of file is 4MB")
def validate_multy(image):
    file_size=image.file.size
    limit_mb=10
    if file_size>limit_mb*1024*1024:
        raise ValidationError("max size of file is 10MB")
class Formone(models.Model):
    name=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50,blank=True)
    date_of_birth=models.DateField()
    email=models.EmailField(max_length=50)
    father_name=models.CharField(max_length=50)
    fathernamelast=models.CharField(max_length=50,blank=True)
    mother_name=models.CharField(max_length=50)
    mothernamelast=models.CharField(max_length=50,blank=True)
    gender=models.CharField(max_length=50)
    nationality=models.CharField(max_length=50)
    home_Address=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    country=CountryField()
    telephone_home=PhoneNumberField(unique = True,blank = True)
    telephone_mobile=PhoneNumberField(unique = True,null = False,blank = False)


class Education(models.Model):
    HSC_Institute_name=models.CharField(max_length=50)
    HSC_Board=models.CharField(max_length=20)
    score_in_HSC=models.FloatField(max_length=30)
    SSC_Institute_name=models.CharField(max_length=50)
    SSC_board=models.CharField(max_length=30)
    score_SSC=models.FloatField(max_length=30)
    Currently_pursuing=models.CharField(max_length=30,blank=True)
    Current_education_institution_name=models.CharField(max_length=30,blank=True)
    Overall_percentage=models.FloatField(max_length=30,blank=True,null=True)
    current_backlog=models.IntegerField(blank=True,null=True)


class UploadingDocument(models.Model):
    photo=models.ImageField('Image',upload_to='img', validators=[validate_image1])
    HSC_mark_sheet=models.FileField(upload_to='mark_hsc', validators=[validate_image1])
    SSC_mark_sheet=models.FileField(upload_to='mark_ssc', validators=[validate_image1])
    all_semesters_mark_sheet=models.FileField(upload_to='all_mark', validators=[validate_multy])