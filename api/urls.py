from django.urls import include, path

urlpatterns = [
    path('user/', include('api.user.urls')),
    path('auth/', include('api.auth.urls')),
]
