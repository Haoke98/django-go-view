"""gpt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os

from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import login, index, get_oss_info, get_project_list, create_project, get_project_data, publish_project, \
    delete_project, edit_project, project_upload, save_project

MEDIA_ROOT = getattr(settings, 'MEDIA_ROOT', 'media')
MEDIA_URL = getattr(settings, 'MEDIA_URL', '/media/')

app_name = 'goview'
urlpatterns = ([
                   path("api/sys/login", login),
                   path("api/sys/getOssInfo", get_oss_info),
                   path("api/project/list", get_project_list),
                   path("api/project/create", create_project),
                   path("api/project/getData", get_project_data),
                   path("api/project/publish", publish_project),
                   path("api/project/delete", delete_project),
                   path("api/project/edit", edit_project),
                   path("api/project/upload", project_upload),
                   path("api/project/save/data", save_project),
                   path("", index, name="index")
               ] + static("static/", document_root=os.path.join(os.path.dirname(__file__), 'frontend', 'static'))
               + static("media/", document_root=MEDIA_ROOT))
