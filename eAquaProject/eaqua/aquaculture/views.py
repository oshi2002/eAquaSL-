from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from .models import FishDisease
from .forms import FishDiseaseForm


def is_admin(user):
    return user.is_staff


def disease_list(request):
    query = request.GET.get('q', '')
    diseases = FishDisease.objects.all().order_by('-updated_at')

    if query:
        diseases = diseases.filter(
            Q(name__icontains=query) |
            Q(symptoms__icontains=query) |
            Q(causes__icontains=query) |
            Q(prevention__icontains=query) |
            Q(treatment__icontains=query)
        )

    return render(request, 'aquaculture/user_diseases.html', {
        'diseases': diseases,
        'query': query
    })


@login_required
@user_passes_test(is_admin)
def manage_diseases(request):
    query = request.GET.get('q', '')
    diseases = FishDisease.objects.all().order_by('-updated_at')

    if query:
        diseases = diseases.filter(
            Q(name__icontains=query) |
            Q(symptoms__icontains=query) |
            Q(causes__icontains=query) |
            Q(severity__icontains=query)

        )

    return render(request, 'aquaculture/admin_diseases.html', {
        'diseases': diseases,
        'query': query
    })


@login_required
@user_passes_test(is_admin)
def add_disease(request):
    if request.method == 'POST':
        form = FishDiseaseForm(request.POST)
        if form.is_valid():
            disease = form.save(commit=False)
            disease.created_by = request.user
            disease.save()
            return redirect('aquaculture:manage_diseases')
    else:
        form = FishDiseaseForm()

    return render(request, 'aquaculture/disease_form.html', {
        'form': form,
        'title': 'Add New Disease'
    })


@login_required
@user_passes_test(is_admin)
def edit_disease(request, pk):
    disease = get_object_or_404(FishDisease, pk=pk)
    if request.method == 'POST':
        form = FishDiseaseForm(request.POST, instance=disease)
        if form.is_valid():
            form.save()
            return redirect('aquaculture:manage_diseases')
    else:
        form = FishDiseaseForm(instance=disease)

    return render(request, 'aquaculture/disease_form.html', {
        'form': form,
        'title': 'Edit Disease'
    })


@login_required
@user_passes_test(is_admin)
def delete_disease(request, pk):
    disease = get_object_or_404(FishDisease, pk=pk)
    if request.method == 'POST':
        disease.delete()
        return redirect('aquaculture:manage_diseases')

    return render(request, 'aquaculture/delete_disease.html', {
        'disease': disease
    })
