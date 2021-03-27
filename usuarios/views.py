from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
# Create your views here.
from usuarios.forms import FormularioUsuarios


class RegistrarUsuario(CreateView):
    model = User
    form_class = FormularioUsuarios
    template_name = 'usuarios/registrar_usuarios.html'
    success_url = reverse_lazy('portafolio:index')

    def post(self, request, *args, **kwargs):
        form  = self.form_class(request.POST)
        if form.is_valid():
            nuevo_usuario = User(
                username=form.cleaned_data.get('username'),
                first_name = form.cleaned_data.get('first_name'),
                last_name=form.cleaned_data.get('last_name'),
                email=form.cleaned_data.get('email'),
            )
            nuevo_usuario.set_password(form.cleaned_data.get('password1'))
            nuevo_usuario.save()
            return redirect('portafolio:index')
        else:
            return render(request, self.template_name, {'form':form})

