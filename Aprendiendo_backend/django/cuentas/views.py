from django.shortcuts import render

# Create your views here.
def login_view(request):
    if request.method == "POST":
        pass
    else:
        return render(request, 'cuentas/login.html', {'form': ''})