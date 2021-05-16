from django import forms
from .models import Empleados


class EmpleadosForm(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = {'nombrecompleto', 'movil', 'empleadocodigo', 'posicion'}
        labels = {
            'nombrecompleto': 'Nombre Completo',
            'empleadocodigo': 'Codigo Empleado'

        }

    def __init__(self, *args, **kwargs):
        super(EmpleadosForm, self).__init__(*args, **kwargs)
        self.fields['posicion'].empty_label = "Seleccionar"
        self.fields['empleadocodigo'].required = False