from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Writing)
class WritingAdmin(admin.ModelAdmin):
    pass
