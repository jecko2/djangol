from django.contrib import admin
from .models import CustomUserApp
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreateNew, UserChangeFormOriginal


class CustomUserAdmin(UserAdmin):
    add_form = UserCreateNew
    form = UserChangeFormOriginal
    model = CustomUserApp

    list_display = ('email', 'is_staff', 'is_active', 'is_superuser')
    # list_filter = ('email', 'is_staff', 'is_active')
    # fieldsets = (
    #     (None, {"fields": ('email', 'password')}),
    #     ('Privilages', {'fields': ('is_staff', 'is_active')}),
    # )
    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide', ),
    #         'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active'),
    #     })
    # )
    search_fields = ('email', )
    ordering = ('email', )


admin.site.register(CustomUserApp, CustomUserAdmin)
