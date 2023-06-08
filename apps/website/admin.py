from unicodedata import name
from django.contrib import admin

# Register your models here.
from django.contrib import admin
# from . import models
from .models import (
    Category, 
        SubCategory,

    Person, 
        Title,
        Gender,  
        Region,

    Staff, 
        Profession,
        Rank,
        Department,
    BoardOfDirector,
    Management, 
        Position,
        Department,
        Service,
        Office,
    Project,
        ProjectDetail,
        ProjectLead,
        ProjectMedia,
        ProjectOverview,
        ProjectTag  
)
""" Imports End"""


# Models Admin Register

""" Categories Admin Start """
class SubCategoryInline(admin.StackedInline):
    model = SubCategory
    extra = 0

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [SubCategoryInline,]
    list_display = ['name','description']
    extra = 0
    list_per_page = 5
    readonly_fields = []
    search_fields = ['name','description']
    ordering = ['name',]
    # raw_id_fields = ['']

""" Categories Admin End """

""" Project Administration Start """
# class ProjectOverviewInline(admin.TabularInline):
#     model = ProjectOverview

# class ProjectDetailInline(admin.TabularInline):
#     model = ProjectDetail

class ProjectLeadInline(admin.TabularInline):     
    model = ProjectLead
    extra = 0

# class ProjectTagInline(admin.TabularInline):
#     model = ProjectTag

# class ProjectMediaInline(admin.TabularInline):
#     model = ProjectMedia


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [
        # ProjectOverviewInline,
        # ProjectDetailInline,
        ProjectLeadInline,
        # ProjectTagInline,
        # ProjectMediaInline

        ]
    list_display = ['name','description']
    extra = 0
    search_fields = ['name','description']
    ordering = ['name',]
    list_per_page = 5
""" Project Administration End """

class DepartmentInline(admin.StackedInline):
    model = Department
    extra = 0
"""  Models Register """

admin.site.register(Title)
admin.site.register(Gender)
admin.site.register(Region)
admin.site.register(Profession)
admin.site.register(Person)

admin.site.register(BoardOfDirector)
admin.site.register(Management)
admin.site.register(Position)

admin.site.register(Staff)
admin.site.register(Rank)
admin.site.register(Department)
admin.site.register(Office)
admin.site.register(Service)
