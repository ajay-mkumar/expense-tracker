from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout as logout_user
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms.userform import UserForm
# from .forms.userform import UserForm


# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html', {'user': request.user})

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home')
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
        else:
            print(form.errors)
    else:
        form = AuthenticationForm()
        
    return render(request, 'login.html', {'form': form})

def about_us(request):
    data = {'address': '4/51 pillaiyarkoil st,Keelaiur, Mayiladuthurai-609304',
    'contact' : '8838927282'}
    return render(request, 'about_us.html', {'data': data})

def add_expense(request):
    return render(request, 'add_expense.html')

def logout(request):
    logout_user(request)
    return redirect('login')