from django.shortcuts import render,redirect

def index_view(request):
    if request.user.is_authenticated:
        return redirect(request.user)
    return render(request,"index.html",{})
