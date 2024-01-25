from django import forms
from demoapp.models import Demo


class DemoForm(forms.ModelForm):

	some_datetime = forms.DateTimeField(
		required=True,
		widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
		label="Data/Ora",
	)

	class Meta:
		model = Demo
		fields = '__all__'
