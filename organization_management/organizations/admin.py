from django.contrib import admin
from .models import Organization, Role, User

admin.site.register(Organization)
admin.site.register(Role)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'organization')
    filter_horizontal = ('roles',)
