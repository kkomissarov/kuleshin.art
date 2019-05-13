from django.contrib import admin
from .models import Work



class WorkAdmin(admin.ModelAdmin):
    list_display = ('id',)


admin.site.register(Work, WorkAdmin)



