from django.shortcuts import render, redirect, get_object_or_404
from .forms import CitaForm
from .models import Cita
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def agendar_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            cita = form.save(commit=False)
            cita.recepcionista = request.user  # Asignar el recepcionista actual
            cita.save()
            return redirect('lista_citas') # Redirigir a la lista de citas después de guardar
    else:
        form = CitaForm()
    return render(request, 'agendar_cita.html', {'form': form})

@login_required
def lista_citas(request):
    query = request.GET.get('buscar', '')
    citas = Cita.objects.filter(recepcionista=request.user)

    if query:
        citas = citas.filter(nombre_paciente__icontains=query)

    citas = citas.order_by('-fecha', '-hora')

    return render(request, 'lista_citas.html', {'citas': citas, 'query': query})

@login_required
def editar_cita(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id, recepcionista=request.user)  # Asegurarse de que el recepcionista es el dueño de la cita

    if request.method == 'POST':
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            return redirect('lista_citas')
    else:
        form = CitaForm(instance=cita)
    return render(request, 'editar_cita.html', {'form': form, 'cita': cita})

@login_required
def eliminar_cita(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id, recepcionista=request.user) # Asegurarse de que el recepcionista es el dueño de la cita

    if request.method == 'POST':
        cita.delete()
        return redirect('lista_citas')
    return render(request, 'eliminar_cita.html', {'cita': cita})


