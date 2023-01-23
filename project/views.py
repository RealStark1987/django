from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.db import IntegrityError
#Importando el Componente Formulario desde COMPONENTS
from .components.forms import *
from .models import Worker
from django.shortcuts import render
from django.db.models import Q

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
@permission_required( 'project.change_worker',raise_exception=True)
def edit_worker(req, worker_id):
    if req.method == 'GET':
        worker   = Worker.objects.get(pk=worker_id)
        form = WorkerForm(instance=worker)
        return render(req, 'worker/edit_worker.html',{
        'form':form,        
        'worker':worker
        })
        
    else:
        try:
            worker   = Worker.objects.get(pk=worker_id)
            worker.added_by = req.user
            form = WorkerForm(req.POST,instance=worker)
            form.save()
            return redirect('worker')
        except ValueError:
            return render(req, 'worker/edit_worker.html',{
        'worker':worker,
        'error': "Error al Modificar el Trabajador"
        })

@login_required
@permission_required( 'project.delete_worker',raise_exception=True)            
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

def login(req):
    if req.method == 'GET':
        return render(req, 'login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(req, username=req.POST['username'],
            password=req.POST['password'])
        if user is None:
            return render(req, 'login.html',{
                        'form': AuthenticationForm,
                        'error': "Username or Password Incorrect" 
                
                    })
        else:
            login(req,user)
            return redirect('worker')

@login_required
@permission_required( 'project.add_worker',raise_exception=True)
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
            
def pag_404_not_found(req, exception):
    return render(req,'error/404.html')

def pag_500_server_error(req, *args, **argv):
    return render(req, '500.html', status=500)

@login_required
@permission_required( 'project.view_acta',raise_exception=True)
def create_act(req):
    if req.method == 'GET':
        return render(req, 'acts/create_act.html',{
        'form': ActForm
        })
    else:
        try:
            form = ActForm(data=req.POST)
            new_act = form.save(commit=False)
            new_act.created_by = req.user
            new_act.save()
            return redirect('act')
        except:
            return render(req, 'acts/create_act.html',{
            'form': ActForm,
            'error': "No se Pudo Crear el Acta"
        })

@login_required            
@permission_required( 'project.view_acta',raise_exception=True)
def act_detail(req, act_id):
    act   = Acta.objects.get(pk=act_id)
    return render(req, 'acts/act_detail.html',{
        'act':act
    })

@login_required
@permission_required( 'project.view_acta',raise_exception=True)
def act(req):
    act = Acta.objects.all()
    return render(req, 'acts/act.html',{
       'act': act
    })

@login_required
@permission_required( 'project.view_acta',raise_exception=True)
def edit_act(req, act_id):
    if req.method == 'GET':
        act   = Acta.objects.get(pk=act_id)
        form = ActForm(instance=act)
        return render(req, 'acts/edit_act.html',{
        'form':form
        })
    else:
        try:
            acta   = Acta.objects.get(pk=act_id)
            form = ActForm(req.POST,instance=acta)
            form.save()
            return redirect('act')
        except ValueError:
            return render(req, 'acts/edit_act.html',{
        'form':form,
        'error': "Error al Modificar el Acta"
        })

@login_required
@permission_required( 'project.view_acta',raise_exception=True)            
def delete_act(req, act_id):
    acta   = Acta.objects.get(pk=act_id)
    if req.method == 'POST':
        acta.delete()
        return redirect('act')  
    
    
def search(req):
    query=req.GET['query']
    queryset = Worker.objects.filter(
       Q(correo__icontains=query)|
        Q(name__icontains=query)|
        Q(occupation__icontains=query)|
        Q(lastname__icontains=query)
        )
    context={
        'queryset':queryset
    }
    print(context)
    return render (req, 'worker/worker.html',context)