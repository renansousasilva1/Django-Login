from django.contrib.auth.views import PasswordResetConfirmView

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

def reset_token_cleaner(request, uidb64, token):
    # Remove o "=" e quebras de linha que o terminal insere
    clean_token = token.replace('=', '').replace('\n', '').replace('\r', '').strip()
    
    # Renderiza a view de confirmação original usando o token limpo
    return PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html'
    )(request, uidb64=uidb64, token=clean_token)


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'