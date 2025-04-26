from django import forms
from .models import Cita

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['nombre_paciente', 'telefono_paciente', 'fecha', 'hora', 'motivo']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
        }
        labels = {
            'nombre_paciente': 'Nombre del Paciente',
            'telefono_paciente': 'Teléfono del Paciente',
            'fecha': 'Fecha de la Cita',
            'hora': 'Hora de la Cita',
            'motivo': 'Motivo de la Cita',
        }