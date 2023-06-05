from django import forms

class EmailPostForm(forms.Form):
    name = forms.CharField(
                            max_length=30,
                            label='Введите ваше имя',
                            required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Ваше имя...'}))
    email = forms.EmailField(
                            label='Введите ваш Email',
                            required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Email'})

    )
    to = forms.EmailField(
                            label='Введите Email получателя',
                            required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Email'})
    )
    comments = forms.CharField(
                            label='Комментарий получателю',
                            required=False,
                            widget=forms.Textarea(attrs={'class': 'form-control mb-3', 'placeholder': 'Введите текст...'}))