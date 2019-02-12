from django import forms


ACCIONISTAS_SOCIOS = (
        ('ACCIONISTAS', 'accionistas'),
        ('SOCIOS', 'socios'),
    )


class InformeForm(forms.Form):
    empresa = forms.CharField(required=True, label='Nombre de la empresa')
    fecha = forms.DateField(required=True, label="Fecha")
    accionistas_socios = forms.ChoiceField(choices=ACCIONISTAS_SOCIOS, required=True, label='Accionistas o socios')
    salvedades = forms.BooleanField(required=True)
    enfasis = forms.BooleanField(required=True)
