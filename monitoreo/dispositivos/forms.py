from django import forms
from .models import dispositivo

class DispositivoForm(forms.ModelForm):
    class Meta:
        model = dispositivo
        fields = ['nombre', 'categoria', 'zona', 'consumo_maximo', 'estado']
        widgets == {
            'nombre': forms.TextInput(attrs={'class': ' form-control'}),
            'consumo_maximo': forms.NumberInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}), #butstrappppppp
            
        }