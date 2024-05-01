from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import Profile

# Register your models here.
# admin.site.register(Group)

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline]



# admin.site.register(Profile)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
