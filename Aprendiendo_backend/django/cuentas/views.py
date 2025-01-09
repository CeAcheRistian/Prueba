from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, login

# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
    else:
        form = AuthenticationForm()
    return render(request, 'cuentas/login.html', {'form': form})