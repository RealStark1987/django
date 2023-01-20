from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
#Importando el Componente Formulario desde COMPONENTS
from .components.forms import WorkerForm
from .models import Worker

# Create your views here.


def home(req):
    return render(req, 'home.html')

def about(req):
    return render(req, 'about.html')

def signup(req):
    if req.method == 'GET':
        return render(req, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if req.POST['password1'] == req.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=req .POST['username'],
                    password=req.POST['password1'])
                
                user.save()
                login(req,user)
                return redirect('worker')
                
            except IntegrityError:
                    return render(req, 'signup.html',{
                        'form': UserCreationForm,
                        'error': "Username Already Exists" 
                
                    })

    return render(req, 'signup.html',{
                        'form': UserCreationForm,
                        'error': "Password Doesnt Match" 
                    })

@login_required
def worker(req):
    worker = Worker.objects.all()
    return render(req, 'worker/worker.html',{
       'worker': worker
    })

@login_required
def edit_worker(req, worker_id):
    if req.method == 'GET':
        worker   = Worker.objects.get(pk=worker_id)
        form = WorkerForm(instance=worker)
        return render(req, 'worker/edit_worker.html',{
        'form':form
        })
    else:
        try:
            worker   = Worker.objects.get(pk=worker_id)
            form = WorkerForm(req.POST,instance=worker)
            form.save()
            return redirect('worker')
        except ValueError:
            return render(req, 'worker/edit_worker.html',{
        'form':form,
        'error': "Error al Modificar el Trabajador"
        })

@login_required            
def delete_worker(req, worker_id):
    worker   = Worker.objects.get(pk=worker_id)
    if req.method == 'POST':
        worker.delete()
        return redirect('worker')  
  
@login_required    
def worker_detail(req, worker_id):
    worker   = Worker.objects.get(pk=worker_id)
    return render(req, 'worker/worker_detail.html',{
        'worker':worker
    })

def signout(req):
    logout(req)
    return redirect('home')

def signin(req):
    if req.method == 'GET':
        return render(req, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(req, username=req.POST['username'],
            password=req.POST['password'])
        if user is None:
            return render(req, 'signin.html',{
                        'form': AuthenticationForm,
                        'error': "Username or Password Incorrect" 
                
                    })
        else:
            login(req,user)
            return redirect('worker')

@login_required
def create_worker(req):
    if req.method == 'GET':
        return render(req, 'worker/create_worker.html',{
        'form': WorkerForm
        })
    else:
        try:
            form = WorkerForm(data=req.POST)
            new_worker = form.save(commit=False)
            new_worker.added_by = req.user
            new_worker.save()
            return redirect('worker')
        except:
            return render(req, 'worker/create_worker.html',{
            'form': WorkerForm,
            'error': "No se Pudo Crear el Trabajador"
        })
               