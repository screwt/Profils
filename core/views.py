from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm,ProfilForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from core.models import Profil, Photo
from django.forms import inlineformset_factory



# Create your views here.
@login_required
def profils(request):
    context = {
        "profils": Profil.objects.all()
    }
    return render(request, "core/profils.html", context=context)


def register_user(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Account created successfully")
            return redirect('login')
    return render(request, "register.html", {"form": form})


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password1")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profils.html')
        else:
            messages.info(request, "Invalid Cridentials")
    return render(request, "login.html", {})


def addProfil(request):
    if request.method == "POST":
        pro = Profil()
        pro.nom = request.POST.get("nom")
        pro.prenom = request.POST.get("prenom")
        pro.date_de_naissance = request.POST.get("date_de_naissance")
        pro.classe = request.POST.get("classe_ecole")
        pro.adresse = request.POST.get("adresse")
        pro.ville = request.POST.get("ville")
        pro.situation = request.POST.get("histoire_famille")
        pro.etat = request.POST.get("etat")
        pro.date_ajoute = request.POST.get("date_dajoute")
        pro.nomparrain = request.POST.get("nom_parrain")
        pro.etat = request.POST.get("etat")

        pro.save()
        messages.success(request, "ajouté déjà un enfant")
    return render(request, 'addProfil.html')

def addProfilAuto(request, id=None):
    PhotoFormset= inlineformset_factory(Profil, Photo, exclude=())
    instance = None
    if id is not None:
        instance = Profil.objects.get(pk=id)

    if request.method=="GET":
        form=ProfilForm(instance=instance)
        photoform_set=PhotoFormset(instance=instance)
        ret = render(request,'addProfilAuto.html',context={"form":form,"photoformset":photoform_set})
        
    elif request.method=="POST":
        form=ProfilForm(request.POST, instance=instance)
        photoform_set=PhotoFormset(request.POST, request.FILES, instance=instance)
        print("profilForm.is_valid()", form.is_valid())
        if form.is_valid() and photoform_set.is_valid():
            profil=form.save()
            photoform_set.save()
            messages.success(request,'form déjà envoyé')
            ret = redirect('addProfil', profil.id)
        else:
            ret = render(request,'addProfilAuto.html',context={"form":form,"photoformset":photoform_set})

    return ret

#update 
