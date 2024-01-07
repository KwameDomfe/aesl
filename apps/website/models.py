from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify
from django.urls import reverse


""" Categories and Sub Categories Start"""
# Categories Model
class Category(models.Model):
    id          = models.AutoField(
        primary_key=True
    )

    name        = models.CharField(
        max_length =128
    )

    slug        = models.SlugField(
        blank=True,
        null=True 
    )

    description = models.TextField(
        max_length=256,
        blank=True,
        null=True
    )

    thumbnail   = models.FileField(
        blank=True,
    )

    is_active   = models.BooleanField(
        default=True
    )

    created     = models.DateTimeField(
        auto_now_add=True
    )

    updated     = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name_plural = 'Project Categories'
        ordering = ['created','updated','name',]
        
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug=slugify(self.name)
        super().save(*args, **kwargs)

def category_pre_save(
        sender, 
        instance, 
        *args, 
        **kwargs
    ):
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
    id          = models.AutoField(
        primary_key=True)

    category    = models.ForeignKey(
        Category, 
        on_delete = models.SET_NULL, 
        null=True)

    name        = models.CharField(
        'Sub Category Name',
        max_length=128)

    slug        = models.SlugField(
        blank=True,
        null=True )

    description = models.TextField(
        'Sub Category Description',
        max_length=256,
        null=True)

    thumbnail   = models.FileField(
        blank=True)

    pub_date    = models.DateField(
        'Date Published', 
        auto_now=True,
        blank= True, 
        null=True)

    is_active   = models.BooleanField(
        default=True)

    created_at  = models.DateTimeField(
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
    id          = models.AutoField(
        primary_key=True)

    name        = models.CharField(
        max_length=128)

    description = models.CharField(
        max_length=128)
    
    class Meta:
        verbose_name='Title'
        verbose_name_plural = 'Titles'
        ordering = ['name',]

    def __str__(self):
        return self.name

# Profession
class Profession(models.Model):
    id          = models.AutoField(
        primary_key=True)

    name        = models.CharField(
        max_length=64)

    description = models.TextField(
        max_length=512, 
        blank=False,
        default='Give a brief description of Profession here')

    def __str__(self):
        return self.name

# Gender Model
class Gender(models.Model):
    id          = models.AutoField(
        primary_key=True)

    name        = models.CharField(
        max_length=16)

    class Meta:
        verbose_name_plural = 'Gender'
    
    def __str__(self):
        return self.name

class Region(models.Model):
    id          = models.AutoField(
        primary_key=True)

    name        = models.CharField(
        max_length =128)

    def __str__(self):
        return self.name


# Person Model
class Person(models.Model):
    id          = models.AutoField(
        primary_key=True)
        
    surname     = models.CharField(
        'Surname',
        max_length =128, 
        null=True)

    lastname    = models.CharField(
        'Lastname',
        max_length =128, 
        null=True)

    othername   = models.CharField(
        'Other Names',
        max_length =128, 
        null=False, 
        blank=True)

    title       = models.ForeignKey(
        Title, 
        on_delete = models.SET_NULL, 
        null=True)
    
    description = models.TextField(
        'Description',
        max_length=512, 
        blank=False)

    dob         = models.DateField(
        'Date of Birth', 
        blank=True, 
        null=True)

    gender      = models.ForeignKey(
        Gender, 
        on_delete = models.SET_NULL, 
        null=True)

    mobile      = models.CharField(
        max_length= 14, 
        blank=True )

    alt_mobile  = models.CharField(
        max_length= 14, 
        blank=True )

    email       = models.EmailField(
        max_length= 64, 
        blank=True )

    alt_email   = models.EmailField(
        max_length= 64, 
        blank=True )
    
    class Meta:
        verbose_name='Person'
        verbose_name_plural = 'Persons'
        ordering = ['title','surname','lastname']
    
    def __str__(self):
        return self.description

""" Personal Information Ends """

""" Practice """

class Section(models.Model):
    id          = models.AutoField(
        primary_key=True)

    name        = models.CharField(
        max_length =128)

    description = models.TextField(
        max_length=512, 
        blank=False,
        default='Give a brief description of Section here')

    def __str__(self):         
        return self.name

class Office(models.Model):
    id          = models.AutoField(
        primary_key=True)

    name        = models.CharField(
        max_length =128)
    
    address     = models.CharField(
        max_length=256,
        null = True,
        blank = True
    )
    
    city        = models.CharField(
        max_length=128,
        null = True,
        blank = True)
    
    phone       = models.CharField(
        max_length=36,
        null = True,
        blank = True
    )
    
    region      = models.ForeignKey(
        Region,
        on_delete = models.SET_NULL,
        null = True,
        blank = True)
    
    def __str__(self):
        return self.name


""" Practice """
class Department(models.Model):
    section     = models.ForeignKey(
        Section,
        on_delete = models.SET_NULL, 
        null=True,
        blank = True)

    id          = models.AutoField(
        primary_key=True)

    name        = models.CharField(
        max_length =128)

    description = models.TextField(
        max_length=512, 
        blank=False,
        default='Give a brief description of Department here')

    def __str__(self):
        return self.name

class Service(models.Model):
    id          = models.AutoField(
        primary_key=True)

    department  = models.ForeignKey(
        Department,
        on_delete = models.SET_NULL,
        null=True)
    
    name        = models.CharField(
        max_length=64)

    description = models.TextField(
        max_length=512, 
        blank=False,
        default='Give a brief description of Services here')

    def __str__(self):
        return self.name

# Positions and Ranks
class Position(models.Model):
    id          = models.AutoField(
        primary_key=True)

    name        = models.CharField(
        max_length=64)

    description = models.TextField(
        max_length=512, 
        blank=False,
        default='type something here')

    def __str__(self):
        return self.name

class Rank(models.Model):
    id          = models.AutoField(
        primary_key=True)

    name        = models.CharField(
        max_length=64)

    slug        = models.SlugField(
        blank=True,
        null=True)

    description = models.TextField(
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
    id          = models.AutoField(
        primary_key=True)
    
    person      = models.ForeignKey(
        Person, 
        on_delete = models.SET_NULL, 
        null=True)
    
    position    = models.ForeignKey(
        Position, 
        on_delete = models.SET_NULL, 
        null=True)
    
    description = models.TextField(
        max_length=512)
    
    cv          = models.FileField(
        null=True,
        blank=True
    )
    
    dateOfFirstAppointment = models.DateField(
        'date of First Appointment',
        null=True, 
        blank=True)
   
    dateOfLasttAppointment = models.DateField(
        'date of Last Appointment',
        null=True, 
        blank=True)
   
    def __str__(self):
        return self.description

# Staff Model
class Staff(models.Model):
    id          = models.AutoField(primary_key=True)

    staff_number = models.CharField(
        max_length=32,
        default='QW23')
    
    person      = models.ForeignKey(
        Person, 
        on_delete = models.SET_NULL, 
        null=True)

    profession  = models.ForeignKey(
        Profession, 
        on_delete = models.SET_NULL, 
        null=True,
        blank=True)

    rank        = models.ForeignKey(
        Rank, 
        on_delete = models.SET_NULL, 
        null=True)

    department  = models.ForeignKey(
        Department, 
        on_delete = models.SET_NULL,
        blank=True,
        null=True)

    description = models.TextField(
        max_length=512)
    
    dateOfFirstAppointment = models.DateField(
        'date of First Appointment', 
        blank= True, 
        null=True)

    office      = models.ForeignKey(
        Office,
        on_delete = models.SET_NULL,
        blank=True,
        null=True
    )  
    
    portrait_picture = models.ImageField(
        upload_to=None, 
        height_field=None, 
        width_field=None, 
        max_length=None,
        blank=True,
        null=True )
    class Meta:
        verbose_name='Staff'
        verbose_name_plural = 'Staff'
        ordering = ['description']

    def __str__(self):
        return self.description

# Management Model
class Management(models.Model):
    id          = models.AutoField(primary_key=True)
    
    staff       = models.ForeignKey(
        Staff, 
        on_delete = models.SET_NULL, 
        null=True)
    
    position    = models.ForeignKey(
        Position, 
        on_delete = models.SET_NULL, 
        null=True)
    
    department  = models.ForeignKey(
        Department, 
        on_delete = models.SET_NULL,
        blank=True,
        null=True)
    
    office      = models.ForeignKey(
        Office,
        on_delete = models.SET_NULL,
        blank=True,
        null=True
    )
    
    slug        = models.SlugField(
        blank=True,
        null=True 
    )
    
    description = models.TextField(
        max_length=512)
    
    date_of_first_appointment = models.DateField(
        'date of First Appointment', 
        blank= True, 
        null=True)
    
    dateOfLasttAppointment = models.DateField(
        'date of Last Appointment',
        null=True, 
        blank=True)
    
    cv          = models.FileField(
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name_plural = 'Management'
        ordering = ['description']
        
    def __str__(self):
        return self.description
    
    def save(self, *arg, **kwarg):
        if self.slug is None:
            self.slug=slugify(self.description)
        super().save(*arg, **kwarg)

# Clients Model
class Client(models.Model):
    id              = models.AutoField(primary_key=True)
    
    name            = models.CharField(
        'Client Name',
        max_length = 128,
    )
    
    logo            = models.FileField(
        null=True,
        blank=True
    )
    
    postal_address  = models.CharField(
        'Postal Address',
        max_length = 128
    )
    
    website         = models.CharField(
        'Website', 
        max_length=50)
    
    def __str__(self):
        return self.name

""" Projects Information Starts """
# Projects Model
class ProjectLead(models.Model):
    id          = models.AutoField(primary_key=True)
    
    staff       = models.ForeignKey(
        Staff, 
        on_delete = models.CASCADE,
        blank=True,
        null = True
        )
    
    class Meta:
        ordering = ['staff']
        verbose_name_plural = "Project Leads"
    
    def __str__(self):
        return self.staff.description

class ProjectCertification(models.Model):
    id          = models.AutoField(primary_key=True)
    
    name        = models.CharField(
        max_length=50)
    
    class Meta:
        ordering = ['name']
        verbose_name_plural = "Project Certifications"
    
    def __str__(self):
        return self.name

class Project(models.Model): 
    id              = models.AutoField(primary_key=True)
    
    name            = models.CharField(
        max_length =256
    )
    
    sub_category    = models.ForeignKey(
        SubCategory, 
        on_delete = models.SET_NULL, 
        null=True,
        blank=True
    )
    
    slug            = models.SlugField(
        blank=True,
        null=True)
    
    description     = models.TextField(
        null=True,
        blank=True
    )
    
    thumbnail       = models.ImageField(
        upload_to='images/projects/',
        default = '_images/placeholders/regular_images/square-01.png',
        null=True,
        blank=True) 
    
    location        = models.CharField(
        max_length=128, 
        null=True,
        blank=True)
    
    cost            = models.DecimalField(
        max_digits=9,
        decimal_places=2, 
        null=True,
        default=3400.00) 
    
    total_floor_area    = models.DecimalField(
        max_digits=9,
        decimal_places=2, 
        null=True,
        blank=True)
    
    jobsheet        = models.FileField( 
        blank=True,
        null=True)
    
    start_date      = models.DateField(
        blank=True, 
        null=True,
        )
    
    completed_date  = models.DateField(
        blank=True, 
        null=True,)  
    
    created         = models.DateField(
        blank=True, 
        null=True,
        auto_now_add=True)
    
    updated         = models.DateField(
        blank=True, 
        null=True,
        auto_now=True)  
    
    client          = models.ForeignKey(
        Client,
        on_delete   = models.SET_NULL,
        null=True,
        blank=True)
    
    coordinator     = models.ForeignKey(
        Staff,
        on_delete   = models.SET_NULL,
        null=True,
        blank=True)
    
    leads           = models.ManyToManyField(
        ProjectLead,
    )
    
    certifications  = models.ManyToManyField(
        ProjectCertification,
    )

    class Meta:
        verbose_name='Project'
        verbose_name_plural = 'Projects'
        ordering = ['name','-start_date',]
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse(
            "website:project-details", 
            kwargs={
                "slug": self.slug
            }
        )

    def save(self, *arg, **kwarg):
        if self.slug is None:
            self.slug=slugify(self.name)
        super().save(*arg, **kwarg) 

class ProjectOverview(models.Model):
    id          = models.AutoField(primary_key=True)
    
    project     = models.ForeignKey(
        Project,
        on_delete= models.CASCADE,
        null = True,
        blank = True)   
    
    overview    = models.TextField(
        max_length=512,
        default='Project Overview')
    
    created_at  = models.DateTimeField(
        auto_now_add=True)
    # Project Overview Methods
    def __str__(self):
        return self.project.name

class ProjectConcept(models.Model):
    id          = models.AutoField(primary_key=True)
    
    project     = models.ForeignKey(
        Project,
        on_delete= models.CASCADE,
        null = True,
        blank = True)   
    
    concept     = models.TextField(
        max_length=512,
        default='Project Concept...')
    
    created_at  = models.DateTimeField(
        auto_now_add=True)
    
    # Project Concept Methods
    def __str__(self):
        return self.concept
    
class ProjectDesign(models.Model):
    id          = models.AutoField(primary_key=True)
    
    project     = models.ForeignKey(
        Project,
        on_delete= models.CASCADE,
        null = True,
        blank = True)   
    
    design      = models.TextField(
        max_length=512,
        default='Project Design...')
    
    created_at  = models.DateTimeField(
        auto_now_add=True)
    
    # Project Design Methods
    def __str__(self):
        return self.design
    
class ProjectConstruction(models.Model):
    id          = models.AutoField(primary_key=True)
    
    project     = models.ForeignKey(
        Project,
        on_delete= models.CASCADE,
        null = True,
        blank = True)   
    
    construction = models.TextField(
        max_length=512,
        default='Project Construction...')
    
    created_at  = models.DateTimeField(
        auto_now_add=True)
    
    # Project Methods Concept
    def __str__(self):
        return self.project

class ProjectDetail(models.Model):
    id          = models.AutoField(primary_key=True)
    project     = models.OneToOneField(
        Project,
        parent_link= Project,
        on_delete= models.CASCADE,
        default= 'true')

    title       = models.CharField(
        max_length=256)
    
    title_details   = models.CharField(
        max_length=256)
    
    created_date    = models.DateField(
        blank=True, 
        null=True,
        auto_now=True)

class ProjectMedia(models.Model):
    id = models.AutoField(primary_key=True)
    
    project     = models.ForeignKey(
        Project, 
        on_delete = models.CASCADE,
        null=True)
    
    media_type_choice = (
        (1, 'Image'),
        (2,'Video'),)
        
    media_type  = models.CharField(
        max_length=256,)
    
    media_content   = models.FileField()
    
class ProjectTag(models.Model):
    id          = models.AutoField(primary_key=True)
    
    project     = models.ForeignKey(
        Project, 
        on_delete = models.SET_NULL,
        null=True)
    
    title       = models.CharField(
        max_length=256)
    
    created_at  = models.DateTimeField(
        auto_now_add=True)

""" Projects Information Ends """