from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import User  # Use your actual User model if custom
from .models import User  # Your custom User model
from multiprocessing import context
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import FarmerRegistrationForm, OfficerCreationForm
from .models import User  # Make sure this is your custom User model
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from .models import User

from django.shortcuts import render
# Create your views here.


def admin_required(user):
    return user.is_authenticated and user.role == 'admin'


def officer_required(user):
    return user.is_authenticated and user.role == 'officer'


def farmer_required(user):
    return user.is_authenticated and user.role == 'farmer' and user.status == 'active'


# Login view
def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')  # or any page you'd like to go to after logout

# Farmer Registration View


def farmer_register(request, self_registration=False):
    if request.method == 'POST':
        form = FarmerRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Registration successful! Please wait for approval.')
            return redirect('login')
    else:
        form = FarmerRegistrationForm()

    template = 'registration/farmer_register_self.html' if self_registration else 'registration/farmer_register.html'
    return render(request, template, {'form': form})

# Create Officer (Admin Only)


@login_required
@user_passes_test(admin_required)
def create_officer(request):
    if request.method == 'POST':
        form = OfficerCreationForm(request.POST, request.FILES)
        if form.is_valid():
            officer = form.save(commit=False)
            officer.created_by = request.user
            officer.save()
            messages.success(request, 'Officer account created!')
            return redirect('dashboard')
    else:
        form = OfficerCreationForm()

    return render(request, 'registration/create_officer.html', {'form': form})


def dashboard(request):
    return render(request, 'accounts/dashboard.html')

# Approve Farmer (Officer Only)


@login_required
@user_passes_test(officer_required)
def approve_farmer(request, user_id):
    farmer = get_object_or_404(User, id=user_id, role='farmer')
    farmer.status = 'active'
    farmer.save()
    messages.success(request, f'Approved farmer: {farmer.username}')
    return redirect('dashboard')


# Dashboard (Login Required)
@login_required
def dashboard(request):
    context = {}

    if request.user.role == 'admin':
        # Farmer stats
        context['pending_farmers'] = User.objects.filter(
            role='farmer', status='pending').count()
        context['active_farmers'] = User.objects.filter(
            role='farmer', status='active').count()
        context['suspended_farmers'] = User.objects.filter(
            role='farmer', status='suspended').count()

        # All user counts for the bar chart
        context['total_admins'] = User.objects.filter(role='admin').count()
        context['total_officers'] = User.objects.filter(role='officer').count()
        context['total_farmers'] = User.objects.filter(role='farmer').count()

        # Status breakdown
        context['pending_users'] = User.objects.filter(
            status='pending').count()
        context['active_users'] = User.objects.filter(status='active').count()
        context['suspended_users'] = User.objects.filter(
            status='suspended').count()

    elif request.user.role == 'officer':
        context['pending_farmers'] = User.objects.filter(
            role='farmer', status='pending')

    elif request.user.role == 'farmer' and request.user.status == 'active':
        context['total_farms'] = 3  # Replace with dynamic farm count
        context['active_licenses'] = 2  # Replace with actual license count
        context['monthly_production'] = 'Rs.100 000'  # Replace with real data

    return render(request, 'dashboard.html', context)
