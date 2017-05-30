from django.contrib.auth.mixins import LoginRequiredMixin as LoginRequired


class LoginRequiredMixin(LoginRequired):
    login_url = 'portfolio:login'
