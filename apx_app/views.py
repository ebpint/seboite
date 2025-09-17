from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views import View
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse

from .forms import LoginForm, BlacklistForm, OperationForm
from .models import CustomUser, ListaNegra, Operacion


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'apx_app/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            perfil = form.cleaned_data['perfil']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_superuser:
                    login(request, user)
                    messages.success(request, f'Bienvenido superusuario {user.username}!')
                    return redirect('apx_app:dashboard')

                if user.perfil == perfil:
                    login(request, user)
                    messages.success(request, f'Bienvenido {user.get_perfil_display()} {user.username}!')
                    return redirect('apx_app:dashboard')
                else:
                    messages.error(request, 'Perfil incorrecto.')

            else:
                messages.error(request, 'Credenciales incorrectas.')

        return render(request, 'apx_app/login.html', {'form': form})


class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'apx_app/dashboard.html')


class ServerView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'apx_app/server.html')


class ListasNegrasView(LoginRequiredMixin, View):
    def get(self, request):
        form = BlacklistForm()
        return render(request, 'apx_app/listas_negras.html', {'form': form})

    def post(self, request):
        form = BlacklistForm(request.POST, request.FILES)
        if form.is_valid():
            lista_negra = form.save(commit=False)
            lista_negra.cargado_por = request.user
            lista_negra.save()
            messages.success(request, "El archivo de la lista negra se ha cargado correctamente.")
            return redirect('apx_app:listas_negras')

        return render(request, 'apx_app/listas_negras.html', {'form': form})


class OperacionesView(LoginRequiredMixin, View):
    def get(self, request):
        form = OperationForm()
        return render(request, 'apx_app/operaciones.html', {'form': form})

    def post(self, request):
        form = OperationForm(request.POST, request.FILES)
        if form.is_valid():
            operacion = form.save(commit=False)
            operacion.cargado_por = request.user
            operacion.save()
            messages.success(request, "El archivo de operaciones se ha cargado correctamente.")
            return redirect('apx_app:operaciones')

        return render(request, 'apx_app/operaciones.html', {'form': form})


class KYCView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'apx_app/kyc.html')


class ClienteView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'apx_app/cliente.html')