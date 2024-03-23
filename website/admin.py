from django.contrib import admin
from .models import Record

# Register your models here.

class ListRecord(admin.ModelAdmin):

    list_display = ( 'id', 'first_name', 'last_name',  'created_at' )

admin.site.register(Record, ListRecord)
