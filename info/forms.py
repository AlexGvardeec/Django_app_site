from django import forms


# Создаем класс формы для обратной связи
class ContactForm(forms.Form):
    name = forms.CharField(label='Ваше имя',
                           required=True,
                           error_messages={
                               'required': 'Введите свое имя',
                           }
                           )
    email = forms.EmailField(label='Ваш e-mail',
                             required=True,
                             error_messages={
                                 'required': 'Введите свой e-mail',
                             })
    message = forms.CharField(
            widget=forms.Textarea(
                attrs={
                    'rows': '7',
                    'cols': '50',
                },
            ),
            label='Ваше сообщение',
    )
