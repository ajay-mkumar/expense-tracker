from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout as logout_user
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Expense
from .forms.userform import UserForm
from .forms.expenseform import ExpenseForm


# Create your views here.
@login_required
def home(request):
    return render(request, 'home.html', {'user': request.user})


def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            User.objects.create_user(form)
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
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def about_us(request):
    data = {'address': '4/51 pillaiyarkoil st,Keelaiur, Mayiladuthurai-609304',
            'contact': '8838927282'}
    return render(request, 'about_us.html', {'data': data})


@login_required
def add_expense(request):
    data = Expense.objects.filter(user_id=request.user)
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user_id = request.user
            expense.save()
            return redirect('add_expense')
        else:
            print(form.errors)
    else:
        form = ExpenseForm()

    return render(request, 'add_expense.html', {'form': form, 'data': data})


def expense_view(request):
    data = Expense.objects.filter(user_id=request.user)
    return render(request, 'expense_view.html', {'expense_data': data})


@login_required
def edit(request, id):
    expense = get_object_or_404(Expense, expense_id=id)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid:
            form.save()
            return redirect('expense')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'add_expense.html', {'form': form, 'is_edit': True})


def logout(request):
    logout_user(request)
    return redirect('login')
