from django import forms

class FormularioRegistro(forms.Form):
    usuario = forms.CharField(required=True, min_length=4, max_length=50, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                                        'id':'username',
                                                                                                        'placeholder':'Username'}))
    correo = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                                                        'id':'email',
                                                                                                        'placeholder':'example@naturalstar.com'}))
    contraseña = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                                        'id':'Password',
                                                                                                        'placeholder':'Password'}))