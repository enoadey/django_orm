from django.contrib import admin
from .models import immo_bienny
from .models import Contact
# # Register your models here.

# # Register your models here.
class Department(admin.ModelAdmin):
    list_display = ('ville', 'departement')
    list_filter = ('departement',)
    search_fields = ['ville']
    

admin.site.register(immo_bienny, Department)
admin.site.register(Contact)
