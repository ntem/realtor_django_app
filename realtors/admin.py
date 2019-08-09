from django.contrib import admin
from .models import Realtor


# Register your models here.
class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'is_mvp')
    list_editable = ('is_mvp',)


admin.site.register(Realtor, RealtorAdmin)