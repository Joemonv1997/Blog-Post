from django.contrib import admin
from .models import login_user,register_user,title,Article

# Register your models here.
admin.site.register(login_user)
admin.site.register(register_user)
admin.site.register(title)
admin.site.register(Article)