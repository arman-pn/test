from django.contrib import admin
from .models import User,TimeEntry,Project

admin.site.register(User)
admin.site.register(TimeEntry)
admin.site.register(Project)
# Register your models here.
