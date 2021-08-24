from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register_user,name="register"),
    path('addProfil/',views.addProfilAuto,name="addProfil"),
    path('editProfil/<int:id>/',views.addProfilAuto,name="addProfil"),
]
