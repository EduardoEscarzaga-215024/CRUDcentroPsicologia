from django import forms
from .models import Recepcionista

class RegistroRecepcionistaForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Confirmar Contraseña')

    class Meta:
        model = Recepcionista
        fields = ['nombre','email','telefono','email','password']
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm: 
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data
