from django import forms
from .models import PerfilUsuario

class PerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ['numero_documento', 'rol', 'foto']  # Campos que el usuario puede editar

    # Opcional: personalizar etiquetas o estilos
    def __init__(self, *args, **kwargs):
        super(PerfilUsuarioForm, self).__init__(*args, **kwargs)
        self.fields['numero_documento'].label = "Número de Documento"
        self.fields['rol'].label = "Rol"
        self.fields['foto'].label = "Foto de Perfil"
