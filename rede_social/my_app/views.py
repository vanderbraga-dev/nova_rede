from django.shortcuts import render

def login_view(request):
    if request.method == 'POST':
        # Aqui você processaria o login
        pass
    return render(request, 'usuarios/login.html')

def cadastro_view(request):
    if request.method == 'POST':
        # Aqui você processaria o cadastro
        pass
    return render(request, 'usuarios/cadastro.html')
