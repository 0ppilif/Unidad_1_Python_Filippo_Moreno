from django import forms
from .models import dispositivo

class DispositivoForm(forms.ModelForm):
    class Meta:
        model = Dispositivo
        fields = ['nombre', 'categoria', 'zona', 'consumo_maximo', 'estado']
        widgets == {
            'nombre': forms.TextInput(attrs={'class': ' form-control'}),
            'consumo_maximo': forms.NumberInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}), #butstrappppppp
            "zona": forms.Select(attrs={'class': 'form-select'}),
            "estado": forms.Select(attrs={'class': 'form-select'}),
            'imagen':forms.FileInput(attrs={'class': 'form-control'}),
        }