from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Book, User

class AddNewBookForm(forms.ModelForm):
	name = forms.CharField(
		label='', 
		widget=forms.widgets.Input({ 'placeholder': 'Название книги' }))
	annotation = forms.CharField(
		label='', 
		widget=forms.widgets.Textarea({ 'placeholder': 'Аннотация' }))
	publication_year = forms.IntegerField(
		label='', 
		widget=forms.widgets.Input({ 'placeholder': 'Год публикации' }))
	photo = forms.ImageField(label='')

	class Meta:
		model = Book
		fields = ['name', 'photo', 'annotation', 'publication_year']

class RegistrationForm(UserCreationForm):
	username: forms.Field = forms.CharField(
		label="Имя пользователя",
		help_text = ''
	)
	password1: forms.Field = forms.CharField(
		label="Пароль",
		widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
		help_text = ''
	)
	password2: forms.Field = forms.CharField(
		label="Подтверждение пароля",
		widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
		help_text = ''
	)

	class Meta:
		model = User
		fields = [	'username', 
					'first_name', 
					'last_name', 
					'patronymic', 
					'phone_number']
