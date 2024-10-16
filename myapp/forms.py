from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label="Título de tarea", max_length=200, widget=forms.TextInput(attrs={'class': 'input'}))
    description = forms.CharField(
        widget=forms.Textarea,  # Esto especifica que quieres un área de texto
        label="Descripción de la tarea",  # La etiqueta del campo
        required=False  # Este campo no es obligatorio
    )

class CreateNewProject(forms.Form):
    name = forms.CharField(label='Título del proyecto', max_length=200, widget=forms.Textarea(attrs={'class': 'input'}))