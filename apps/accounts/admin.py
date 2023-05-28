from django.contrib import admin

from django.contrib import admin
from . import models


class AccountsAdminArea(admin.AdminSite):
    site_header = 'Pages Admin Area'

accounts_site = AccountsAdminArea(name='AccountsAdmin')  