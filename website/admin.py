from django.contrib import admin
from .models import Candidate, ScoreEverything, Status, ScoreCard

# Register your models here.

class ListRecord(admin.ModelAdmin):

    list_display = ( 'id', 'first_name', 'last_name',  'created_at' )

class ReadId(admin.ModelAdmin):

    readonly_fields = ('id',)


admin.site.register(Candidate, ReadId)
admin.site.register(ScoreEverything)
admin.site.register(Status)
admin.site.register(ScoreCard)
