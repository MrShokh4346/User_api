from django.urls import include, path
from rest_framework import routers
from . import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='User API')



urlpatterns = [
    path('swagger/', schema_view),
    path('api/user', views.create_user),
    path('api/user-detail/<int:id>', views.user_detail),
]
