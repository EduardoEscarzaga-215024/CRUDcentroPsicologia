from django.shortcuts import render, redirect
from .forms import RegistroRecepcionistaForm
from django.contrib.auth import login as auth_login, authenticate
from .models import Recepcionista
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def registrar_recepcionista(request):
    if request.method == 'POST':
        form = RegistroRecepcionistaForm(request.POST)
        if form.is_valid():
            recepcionista = form.save(commit=False)
            recepcionista.set_password(form.cleaned_data['password'])
            recepcionista.save()
            auth_login(request, recepcionista)  # Iniciar sesión automáticamente
            return redirect('home')  # Redirigir a la página de inicio o a donde desees
    else:
        form = RegistroRecepcionistaForm()
    return render(request, 'registro_recepcionista.html', {'form': form})

def login_recepcionista(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, f"¡Bienvenido(a), {user.nombre}!")
            return redirect('home')
        else:
            messages.error(request, 'Correo o contraseña incorrectos.')
    return render(request, 'login.html')

@login_required
def logout_recepcionista(request):
    logout(request)
    messages.success(request, "¡Sesión cerrada exitosamente!")
    return redirect('home')



