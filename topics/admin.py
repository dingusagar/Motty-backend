from django.contrib import admin

# Register your models here.
from topics.models import Topic, Celebrity

admin.site.register(Topic)
admin.site.register(Celebrity)
