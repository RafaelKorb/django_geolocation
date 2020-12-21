from django.shortcuts import render, redirect
from .models import Target
from .forms import TargetForm
import folium



def show_map(request):
        mapa = folium.Map(location=[-15.788497,-47.879873],zoom_start=3)
        return render(request, 'map.html', {'mapa': mapa})


def list_targets(request):
    targets = Target.objects.all()
    mapa = folium.Map(location=[-15.788497,-47.879873],zoom_start=3)
    return render(request, 'targets.html', {'targets': targets})



def create_target(request):
    form = TargetForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_targets')

    return render(request, 'targets-form.html', {'form': form})


def update_target(request, id):
    target = Target.objects.get(id=id)
    form = TargetForm(request.POST or None, instance=target)

    if form.is_valid():
        form.save()
        return redirect('list_targets')

    return render(request, 'targets-form.html', {'form': form, 'target': target})


def delete_target(request, id):
    target = Target.objects.get(id=id)

    if request.method == 'POST':
        target.delete()
        return redirect('list_targets')

    return render(request, 'target-delete-confirm.html', {'target': target})