from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


@admin.register(User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("EXTRA"),{"fields": ("status", "phone", "passport")}),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


admin.site.register(Role)
admin.site.register(Staff)
admin.site.register(Category)
admin.site.register(Info)
admin.site.register(Food)
admin.site.register(Menu)
admin.site.register(Rooms)
admin.site.register(Ads)
admin.site.register(Hotel)
