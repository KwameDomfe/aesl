from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.urls import reverse


""" Categories and Sub Categories Start"""
# Categories Model
class Category(models.Model):
    id=models.AutoField(
        primary_key=True)

    name=models.CharField(
        max_length =128)

    slug=models.SlugField(
        blank=True,
        null=True )

    description=models.TextField(
        max_length=512,
        blank=True,
        null=True )

    thumbnail=models.FileField(
        blank=True,
        )

    is_active=models.BooleanField(
        default=True)

    created=models.DateTimeField(
        auto_now_add=True)

    updated=models.DateTimeField(
        auto_now=True)

    class Meta:
        verbose_name_plural = 'Project Categories'
        ordering = ['-created','updated','name',]
        
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug=slugify(self.name)
        super().save(*args, **kwargs)

def category_pre_save(sender, instance, *args, **kwargs):
    print('pre_save')
    if instance.slug is None:
        instance.slug = slugify(instance.name)

pre_save.connect(category_pre_save, sender = Category)

def category_post_save(sender, instance, created, *args, **kwargs):
    print('post_save')
    if created:
        instance.slug = slugify(instance.name)
        instance.save()

post_save.connect(category_post_save, sender = Category)

# Sub Categories Model
class SubCategory(models.Model):
    id=models.AutoField(
        primary_key=True)

    category=models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True)

    name=models.CharField(
        'Sub Category Name',
        max_length=128)

    slug=models.SlugField(
        blank=True,
        null=True )

    description=models.TextField(
        'Sub Category Description',
        max_length=512,
        null=True)

    thumbnail=models.FileField(
        blank=True)

    pub_date=models.DateField(
        'Date Published', 
        auto_now=True,
        blank= True, 
        null=True)

    is_active=models.BooleanField(
        default=True)

    created_at=models.DateTimeField(
        'Date Created',
        auto_now_add=True,
        blank= True, 
        null=True)

    class Meta:
        verbose_name_plural = 'Sub Categories'
        ordering = ['id']

    def __str__(self):
        return self.name

    def save(self, *arg, **kwarg):
        if self.slug is None:
            self.slug=slugify(self.name)
        super().save(*arg, **kwarg)

""" Categories and Sub Categories End"""

""" Personal Information Starts """
# Title Model
class Title(models.Model):
    id=models.AutoField(
        primary_key=True)

    name=models.CharField(
        max_length=128)

    description=models.CharField(
        max_length=128)
    
    def __str__(self):
        return self.name

# Profession
class Profession(models.Model):
    id=models.AutoField(
        primary_key=True)

    name=models.CharField(
        max_length=64)

    description=models.TextField(
        max_length=512, 
        blank=False,
        default='Give a brief description of Profession here')

    def __str__(self):
        return self.name

# Gender Model
class Gender(models.Model):
    id=models.AutoField(
        primary_key=True)

    name=models.CharField(
        max_length=16)

    class Meta:
        verbose_name_plural = 'Gender'
    
    def __str__(self):
        return self.name

class Region(models.Model):
    id=models.AutoField(
        primary_key=True)

    name=models.CharField(
        max_length =128)

    def __str__(self):
        return self.name

class Office(models.Model):
    id=models.AutoField(
        primary_key=True)

    name=models.CharField(
        max_length =128)

    region=models.ForeignKey(
        Region,
        on_delete=models.SET_NULL,
        null=True)
    
    def __str__(self):
        return self.name


# Person Model
class Person(models.Model):
    id=models.AutoField(
        primary_key=True)
        
    surname=models.CharField(
        'Surname',
        max_length =128, 
        null=True)

    lastname=models.CharField(
        'Lastname',
        max_length =128, 
        null=True)

    othername=models.CharField(
        'Other Names',
        max_length =128, 
        null=False, 
        blank=True)

    description=models.TextField(
        'Description',
        max_length=512, 
        blank=False)

    dob=models.DateField(
        'Date of Birth', 
        blank=True, 
        null=True)

    title=models.ForeignKey(
        Title, 
        on_delete=models.SET_NULL, 
        null=True)

    gender=models.ForeignKey(
        Gender, 
        on_delete=models.SET_NULL, 
        null=True)

    mobile_1=models.CharField(
        max_length= 14, 
        blank=True )

    mobile_2=models.CharField(
        max_length= 14, 
        blank=True )

    email_1=models.EmailField(
        max_length= 64, 
        blank=True )

    email_2=models.EmailField(
        max_length= 64, 
        blank=True )
    
    def __str__(self):
        return self.description

""" Personal Information Ends """

""" Practice """

class Section(models.Model):
    id=models.AutoField(
        primary_key=True)

    name=models.CharField(
        max_length =128)

    description=models.TextField(
        max_length=512, 
        blank=False,
        default='Give a brief description of Section here')

    def __str__(self):         
        return self.name


""" Practice """
class Department(models.Model):
    section = models.ForeignKey(
        Section,
        on_delete=models.SET_NULL, 
        null=True,
        blank = True)

    id=models.AutoField(
        primary_key=True)

    name=models.CharField(
        max_length =128)

    description=models.TextField(
        max_length=512, 
        blank=False,
        default='Give a brief description of Department here')

    def __str__(self):
        return self.name

class Service(models.Model):
    id=models.AutoField(
        primary_key=True)

    department=models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True)
    
    name=models.CharField(
        max_length=64)

    description=models.TextField(
        max_length=512, 
        blank=False,
        default='Give a brief description of Services here')

    def __str__(self):
        return self.name

# Towns and Cities


# Positions
class Position(models.Model):
    id=models.AutoField(
        primary_key=True)

    name=models.CharField(
        max_length=64)

    description=models.TextField(
        max_length=512, 
        blank=False,
        default='type something here')

    def __str__(self):
        return self.name

class Rank(models.Model):
    id=models.AutoField(
        primary_key=True)

    name=models.CharField(
        max_length=64)

    slug=models.SlugField(
        blank=True,
        null=True)

    description=models.TextField(
        max_length=512, 
        blank=False,
        default='type something here')

    def __str__(self):
        return self.name

    def save(self, *arg, **kwarg):
        if self.slug is None:
            self.slug=slugify(self.name)
        super().save(*arg, **kwarg)

# Directors Model
class BoardOfDirector(models.Model):
    id=models.AutoField(
        primary_key=True)
    person=models.ForeignKey(
        Person, 
        on_delete=models.SET_NULL, 
        null=True)
    position=models.ForeignKey(
        Position, 
        on_delete=models.SET_NULL, 
        null=True)
    description=models.TextField(
        max_length=512)
    dateOfFirstAppointment=models.DateField(
        'date of First Appointment',
        null=True, 
        blank=True)
   
    def __str__(self):
        return self.description

# Staff Model
class Staff(models.Model):
    id=models.AutoField(primary_key=True)

    staff_number=models.CharField(
        max_length=32,
        default='QW23')
    
    person=models.ForeignKey(
        Person, 
        on_delete=models.SET_NULL, 
        null=True)

    profession=models.ForeignKey(
        Profession, 
        on_delete=models.SET_NULL, 
        null=True,
        blank=True)

    rank=models.ForeignKey(
        Rank, 
        on_delete=models.SET_NULL, 
        null=True)

    department=models.ForeignKey(
        Department, 
        on_delete=models.SET_NULL,
        blank=True,
        null=True)

    description=models.TextField(
        max_length=512)
    
    dateOfFirstAppointment=models.DateField(
        'date of First Appointment', 
        blank= True, 
        null=True)

    office = models.ForeignKey(
        Office,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )   
    def __str__(self):
        return self.description

# Management Model
class Management(models.Model):
    id = models.AutoField(primary_key=True)
    staff=models.ForeignKey(
        Staff, 
        on_delete=models.SET_NULL, 
        null=True)
    position=models.ForeignKey(
        Position, 
        on_delete=models.SET_NULL, 
        null=True)
    department=models.ForeignKey(
        Department, 
        on_delete=models.SET_NULL,
        blank=True,
        null=True)
    office = models.ForeignKey(
        Office,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    slug=models.SlugField(
        blank=True,
        null=True 
    )
    description=models.TextField(
        max_length=512)

    date_of_first_appointment=models.DateField(
        'date of First Appointment', 
        blank= True, 
        null=True)
    
    class Meta:
        verbose_name_plural = 'Management'
        ordering = ['description']
        
    def __str__(self):
        return self.description
    
    def save(self, *arg, **kwarg):
        if self.slug is None:
            self.slug=slugify(self.description)
        super().save(*arg, **kwarg)



""" Projects Information Starts """
# Projects Model
class Project(models.Model): 
    id=models.AutoField(primary_key=True)
    
    sub_category=models.ForeignKey(
        SubCategory, 
        on_delete=models.SET_NULL, 
        null=True,
        blank=True)
    name=models.CharField(
        max_length =256)
    slug=models.SlugField(
        blank=True,
        null=True)
    description=models.TextField(
        null=True,
        blank=True
    )
    thumbnail= models.ImageField(
        upload_to='images/projects/',
        default = '_images/placeholders/regular_images/square-01.png',
        null=True,
        blank=True) 
    location= models.CharField(
        max_length=128, 
        null=True,
        blank=True)
    cost=models.CharField(
        max_length=128, 
        null=True,
        default='GHC 5 million') 
    client=models.CharField(
        max_length=128, 
        null=True,
        blank=True)
    total_floor_area=models.DecimalField(
        max_digits=9,
        decimal_places=2, 
        null=True,
        blank=True)
    coordinator=models.ForeignKey(
        Staff,
        on_delete=models.SET_NULL,
        null=True,
        blank=True)
    jobsheet=models.FileField( 
        blank=True,
        null=True)
    start_date=models.DateField(
        blank=True, 
        null=True,
        auto_now_add=True)
    completed_date=models.DateField(
        blank=True, 
        null=True,
        auto_now_add=True)  
    
    class Meta:
        verbose_name='Project'
        verbose_name_plural = 'Projects'
        ordering = ['name','-start_date',]
    
    def get_absolute_url(self):
        return reverse(
            "website:project-details", 
            kwargs={"slug": self.slug}
            ) 
        
    def __str__(self):
        return self.name

    def save(self, *arg, **kwarg):
        if self.slug is None:
            self.slug=slugify(self.name)
        super().save(*arg, **kwarg) 

class ProjectLead(models.Model):
    id=models.AutoField(primary_key=True)
    project = models.ForeignKey(
        Project,
        on_delete= models.CASCADE,
        null = True,
        blank = True)

    slug=models.SlugField(
        blank=True,
        null=True)

    staff=models.ForeignKey(
        Staff, 
        on_delete=models.CASCADE,
        null=True,
        blank=True)

    description = models.CharField(
        max_length=128, 
        null=True,
        blank=True)
        
    def __str__(self):
        return self.description
        
    def save(self, *arg, **kwarg):
        if self.slug is None:
            self.slug=slugify(self.description)
        super().save(*arg, **kwarg) 

class ProjectDetail(models.Model):
    id=models.AutoField(primary_key=True)
    
    project = models.OneToOneField(
        Project,
        parent_link= Project,
        on_delete= models.CASCADE,
        default= 'true')

    title=models.CharField(
        max_length=256)
    
    title_details=models.CharField(
        max_length=256)
    
    created_date=models.DateField(
        blank=True, 
        null=True,
        auto_now=True)

class ProjectMedia(models.Model):
    id=models.AutoField(primary_key=True)
    project=models.ForeignKey(
        Project, 
        on_delete=models.CASCADE,
        null=True)
    media_type_choice = (
        (1, 'Image'),
        (2,'Video'),)
        
    media_type = models.CharField(
        max_length=256,)
    
    media_content = models.FileField()
    
class ProjectOverview(models.Model):
    id=models.AutoField(primary_key=True)
    project= models.ForeignKey(
        Project,
        on_delete= models.CASCADE,
        null = True,
        blank = True)   
    description=models.TextField(
        max_length=256,
        default='Project Overview')
    created_at=models.DateTimeField(
        auto_now_add=True)

class ProjectTag(models.Model):
    id=models.AutoField(primary_key=True)
    project=models.ForeignKey(
        Project, 
        on_delete=models.SET_NULL,
        null=True)
    title=models.CharField(
        max_length=256)
    created_at=models.DateTimeField(
        auto_now_add=True)
""" Projects Information Ends """