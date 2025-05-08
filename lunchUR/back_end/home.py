from django.shortcuts import redirect
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'  
    
    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('usuario_id'):
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = self.request.session.get('nombre_usuario', 'Usuario')
        return context
    
    