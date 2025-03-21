from django import forms
#from django.contrib.auth.models import User
from clientes.models import Cliente


class FormularioRegistro(forms.Form):
    usuario = forms.CharField(required=True, min_length=4, max_length=50, 
                              widget=forms.TextInput(attrs={'class': 'form-control', 'id':'username', 'placeholder':'Username'}))
    correo = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control','id':'email','placeholder':'example@naturalstar.com'}))
    contraseña = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    contraseña2 = forms.CharField(label='Confirmar Contraseña', required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    

    # definir metodo y tomar el dato de usuario
    def clean_usuario(self):
        usuario = self.cleaned_data.get('usuario')
        #realizar consulta a nuestra base de datos
        if Cliente.objects.filter( username = usuario).exists():
            raise forms.ValidationError('El usuario se encuentra en uso')
        return  usuario
    
    def clean_correo(self):
        correo = self.cleaned_data.get('correo')
        #realizar consulta a nuestra base de datos
        if Cliente.objects.filter( email = correo).exists():
            raise forms.ValidationError('El email se encuentra en uso')
        return  correo
    

    #obtener los datos de la tabla padre
    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('contraseña2') != cleaned_data.get('contraseña'):
            self.add_error('contraseña2', 'la contraseña no coincide' )

    def save(self):

        return Cliente.objects.create_user(
            self.cleaned_data.get('usuario'),
            self.cleaned_data.get('correo'),
            self.cleaned_data.get('contraseña'),
        )


