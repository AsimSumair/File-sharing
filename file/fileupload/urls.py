from django.urls import path,include,re_path
from rest_framework import routers
from fileupload import views
from fileupload.views import SignupAPI,LoginAPI
from django.urls import re_path as url

router = routers.DefaultRouter()
router.register('fileupload',views.FileViewSet,basename='fileupload')

urlPatterns = [
    # api urls viewset 
      path('file_api/',views.FileUpload,name='file'),
      path('signup_api/',views.SignupAPI,name='signup'),
      path('login/', LoginAPI.as_view(), name='login'),
]

