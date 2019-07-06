
from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework_swagger.views import get_swagger_view
from rest_framework.documentation import include_docs_urls
from .views import login
# schema_view = get_schema_view(title ='Blog API')
schema_view = get_swagger_view(title='Messages API')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('posts.urls')),
    path('api-auth', include('rest_framework.urls')),
    # path('api/v1/rest-auth/',include('rest_auth.urls')),
    path('api/v1/login', login),
    path('api/v1/rest-auth/registration/',
         include('rest_auth.registration.urls')),
    path('docs/', include_docs_urls(title='Blog Api')),
    path('schema/', schema_view),  # install pyyaml to run this
    path('swagger-docs/', schema_view),

]
