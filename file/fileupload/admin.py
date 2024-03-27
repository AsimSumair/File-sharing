from django.contrib import admin
from fileupload.models import FileUpload
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import *

// This is the admin page 

class UserAdmin(BaseUserAdmin):
  list_display = ('id', 'email', 'username',)
  list_filter = ('email',)
  fieldsets = (
      ('User Credentials', {'fields': ('email', 'password',)}),
      ('Personal info', {'fields': ('username',)}),
      ('Permissions', {'fields': ('is_admin',)}),
  )
  add_fieldsets = (
      (None, {
          'classes': ('wide',),
          'fields': ('email', 'username', 'password1', 'password2'),
      }),
  )
  search_fields = ('email',)
  ordering = ('email', 'id',)
  filter_horizontal = ()

admin.site.register(adminLogin, UserAdmin)

class File_Upload(admin.ModelAdmin):
  list_display = ('id','name','file')

  add_fieldsets = (
      (None, {
          'classes': ('wide',),
          'fields': ('Date'),
      }),
  )
  search_fields = ('name',)
  ordering = ('id', 'name',)
  filter_horizontal = ()

admin.site.register(FileUpload,File_Upload)
 

class signup(admin.ModelAdmin):
  list_display = ('id','Username','Email','is_Verified')
  add_fieldsets = (
      (None, {
          'classes': ('wide',),
          'fields': ('created_at'),
      }),
  )
  search_fields = ('Username','Email',)
  ordering = ('Username',)
  filter_horizontal = ()

admin.site.register(Signup,signup)


class login(admin.ModelAdmin):

  list_display = ('id','Email','is_Verified')

  add_fieldsets = (
      (None, {
          'classes': ('wide',),
          'fields': ('created_at'),
      }),
  )
  search_fields = ('Email',)
  ordering = ('Email',)
  filter_horizontal = ()

admin.site.register(Login,login)


