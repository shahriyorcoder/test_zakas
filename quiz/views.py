from django.shortcuts import render,redirect
from .models import Task , Category ,Taskusers,Appect_user
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm
import datetime
from django.views.generic.edit import UpdateView


now = datetime.datetime.now()

def homepage(request):


    tasks = Task.objects.all()
    if request.user.is_active == True:
        # request.user.appect_user_set.all()
 

        # datas = Appect_user.objects.create(
        #         users=request.user
        #     )
            # print(datas)
        # datas.save()
        if request.method == 'POST':

        

            if request.user.taskusers_set.all().count() == 0:
                Taskusers.objects.create(
                    username = request.user,
                    natija=request.POST.get('natija'),
                    checking=request.POST.get('checking')
                )
                return redirect('/')
            else:
                dt = request.user.taskusers_set.all()[0]
                dt.natija = request.POST.get('natija')
                dt.checking = request.POST.get('checking')
                dt.date=datetime.datetime.now()
                dt.save()
                return redirect('/')
        context={
            'task':tasks,
            'users_appect':Appect_user.objects.all(),
            'yourtest':request.user.taskusers_set.all(),
        }
    else:
        context={
        }

    return render(request,'test.html',context)


def adminpage(request):
    tasks = Task.objects.all()
    usertask = Taskusers.objects.all()
    category = Category.objects.all().order_by('id')
    context ={
        'testlar':tasks,
        'topshirganlar':usertask,
        'category':category,
    }
    return render(request,'admin.html',context)

def apply(request):
    usertask = Taskusers.objects.all().order_by('-date')
    
    context ={
    'topshirganlar':usertask,
    'true':Taskusers.objects.filter(checking='True').all().count(),
    'false':Taskusers.objects.filter(checking='False').all().count(),
    }
    return render(request,'apply.html',context)


def admindetail(request,id):
    categ = Category.objects.get(id=id)
    if request.method =="POST":
        Task.objects.create(
            category=categ,
            title=request.POST.get('title'),
            a=request.POST.get('a'),
            b=request.POST.get('b'),
            c=request.POST.get('c'),
            d=request.POST.get('d'),
            togri_javob=request.POST.get('togri_javob')
        )
        return redirect('admindetail',categ.id)


    context={
        'categ':categ,
        'tasks':categ.task_set.all().order_by('-id')
    }
    return render(request,'categorydetail.html',context)

def taskdelete(request,id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('admindetail',task.category.id)


class Updatetask(UpdateView):
    model= Task
    template_name='updatetask.html'
    fields='__all__'

def index(request):
    if request.user.is_active == True:
        context={
            'yourtest':request.user.taskusers_set.all(),
        }
    else:
        context={}
    
    return render(request,'index.html',context)
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    return redirect('login')