from django.contrib import admin
from .models import Category, Reason, Box, Activity

admin.site.register(Category)
admin.site.register(Box)
admin.site.register(Reason)
admin.site.register(Activity)
