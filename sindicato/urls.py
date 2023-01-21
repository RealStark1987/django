"""sindicato URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from project import views
from django.conf.urls import handler404, handler500

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('search/',views.search,name='search'),
    path('signup/',views.signup, name= 'signup'),
    path('login/',views.login, name= 'login'),
    path('logout/',views.signout, name = 'logout'),
    path('about/',views.about, name= 'about'),
    #Rutas de los Trabajadores    
    path('worker/',views.worker, name= 'worker'),
    path('worker/create',views.create_worker, name= 'create_worker'),
    path('worker/<int:worker_id>/edit/',views.edit_worker, name= 'edit_worker'),
    path('worker/<int:worker_id>/delete/',views.delete_worker, name= 'delete_worker'),
    path('worker/<int:worker_id>',views.worker_detail ,name= 'worker_detail'),
    #Rutas de las Actas
    path('act/',views.act, name= 'act'),
    path('act/create',views.create_act, name= 'create_act'),
    path('act/<int:act_id>/edit/',views.edit_act, name= 'edit_act'),
    path('act/<int:act_id>/delete/',views.delete_act, name= 'delete_act'),
    path('act/<int:act_id>',views.act_detail ,name= 'act_detail'),
    
    
    path('accounts/', include('django.contrib.auth.urls')),
]
handler404 = views.pag_404_not_found
handler500 = views.pag_500_server_error

