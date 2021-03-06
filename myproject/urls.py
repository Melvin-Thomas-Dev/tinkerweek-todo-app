"""myproject URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from todo.views import index_view, home, detail_view
from .settings import STATIC_ROOT, STATIC_URL
# from todo.views import get_notifications
# from appname import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('todo/details/<int:id>/', detail_view, name='details'),
    path('index/', index_view, name="index"),
    # path('appname/', include(appname.urls)),
    # path('notifications/', get_notifications, name='notifications')
] +  static(STATIC_URL, document_root=STATIC_ROOT)
