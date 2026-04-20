from django.shortcuts import render, redirect
from mi_admin.models import PerfilUsuario
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

@login_required
def editar_perfil(request):
    try:
        perfil = PerfilUsuario.objects.get(User__id=request.session['usuario_id'])
    except ObjectDoesNotExist:
        return redirect('perfil')  # Redirige si no hay ningun perfil. 

    if request.method == 'POST':
        perfil.numero_documento = request.POST.get('numero_documento')
        perfil.rol = request.POST.get('rol')

        if 'foto' in request.FILES:
            perfil.foto = request.FILES['foto']

        perfil.save()
        return redirect('perfil')

    return render(request, 'editar_perfil.html', {'perfil': perfil})