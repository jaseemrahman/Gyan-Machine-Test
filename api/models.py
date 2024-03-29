from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.


class BaseModel(models.Model):
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# School
class School(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    district = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True) 
    pincode = models.CharField(max_length=10, null=True, blank=True) 

    def __str__(self):
        return self.name 

# Student
class Student(BaseModel):
    school = models.ForeignKey(School, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True) 
    phone = models.CharField(max_length=15)  

    def __str__(self):
        return self.name

# Gallery
class Gallery(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='gallery', null=True, blank=True,verbose_name='Image',
        help_text='Upload JPG or PNG only',
        validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png','webp'])])



