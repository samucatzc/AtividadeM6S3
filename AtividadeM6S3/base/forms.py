from django import forms
from base.models import Contato, Reserva
class ContatoForm(forms.ModelForm):
   class Meta:
     model = Contato


     fields = ['nome', 'email', 'mensagem']

     widgets = {
        'nome'  : forms.TextInput(
           attrs={
              'placeholder' : 'insira o seu nome aqui'
           }
        ),
        'email' : forms.EmailInput(
           attrs={
              'placeholder' : 'insira o seu e-mail aqui'
           }
        ),
        'mensagem': forms.Textarea(
           attrs={
              'placeholder' : 'insira o sua mensagem aqui'
           }
        )
      }
     labels = {
       'nome' : 'Nome:',
       'email' : 'E-mail:',
       'mensagem' : 'Mensagem'
    }

class ReservaForm(forms.ModelForm):
   class Meta:
     model = Reserva


     fields = ['nome_do_pet', 'telefone','data', 'mensagem']

     widgets = {
        'nome_do_pet'  : forms.TextInput(
           attrs={
              'placeholder' : 'insira o seu nome do seu pet aqui!'
           }
        ),
        'telefone' : forms.TextInput(
           attrs={
              'placeholder' : 'insira o seu telefone aqui!'
           }
           
        ),
        'data' : forms.DateInput(),

        'mensagem': forms.Textarea(
           attrs={
              'placeholder' : 'insira o sua mensagem aqui!'
           }
        )
      }
     labels = {
       'nome_do_pet' : 'Nome do Pet:',
       'telefone' : 'Telefone:',
       'data' : 'Data de Reserva',
       'mensagem' : 'Mensagem'
    }