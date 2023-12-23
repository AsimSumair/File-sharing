from django.contrib import admin
from django.urls import path, include
from fileupload.views import *
from fileupload import urls
from fileupload.views import SignupAPI
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login/', TokenObtainPairView.as_view(), name='login_view'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh_view'),
    path('login_api/', LoginAPI.as_view()),
    path('file_api/', FileViewSet.as_view({'get':'list'})),
    path('signup_api/',SignupAPI.as_view()),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
