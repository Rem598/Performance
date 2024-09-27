
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import PerformanceData
from .forms import PerformanceDataForm
import json


def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        return redirect('login')  # Redirect to login after registration
    return render(request, 'register.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


@login_required
def dashboard(request):
    # Handle form submission
    if request.method == 'POST':
        form = PerformanceDataForm(request.POST)
        if form.is_valid():
            performance_data = form.save(commit=False)
            performance_data.user = request.user
            performance_data.save()
            return redirect('dashboard')
    else:
        form = PerformanceDataForm()

    # Get all performance data for the logged-in user
    data = PerformanceData.objects.filter(user=request.user).order_by('date')

    # Prepare data for chart (JSON format)
    dates = [entry.date.strftime("%Y-%m-%d") for entry in data]
    income_data = [entry.income for entry in data]
    expenses_data = [entry.expenses for entry in data]
    profit_data = [entry.profit for entry in data]

    chart_data = {
        'dates': dates,
        'income': income_data,
        'expenses': expenses_data,
        'profit': profit_data,
    }

    context = {
        'form': form,
        'data': data,
        'chart_data': json.dumps(chart_data),
    }

    return render(request, 'dashboard.html', context)

@login_required
def account(request):
    return render(request, 'account.html')

def logout_view(request):
    logout(request)
    return redirect('login')  