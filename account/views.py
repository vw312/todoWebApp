from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as real_login, logout as real_logout,update_session_auth_hash
from django.urls import reverse
from django.http import HttpResponseRedirect

from .models import myUser
from .forms import accountCreateForm, accountLoginForm, passwordChangeForm,accountEditForm
from schedules.models import Schedules

def account_view(request,user_id):
    """displays user profile """
    if not request.user.is_authenticated:
        return redirect('login/')
    else:
        if request.user.id != user_id :
            return redirect(request.user)
        else:
            queryset=Schedules.objects.filter(user=user_id )
            queryset_email=Schedules.objects.filter(state_user = False,email_sent=False)

            for instance in queryset_email :
                instance.email()

            for instance in queryset :
                instance.update()

            context={
                'user':myUser.objects.get(id=user_id),
                'schedule_list':queryset,
            }
            return (render(request, "profile.html", context))


def register_view(request):
    """displays the create account screen"""
    if request.user.is_authenticated:
        return redirect(request.user)

    else:
        if request.method == "POST":
            form = accountCreateForm(request.POST )
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('login'))

        else :
            form = accountCreateForm()

        context = {
            'form': form
        }

        return render(request, "register.html", context)


def logout_view(request,user_id):
    """Logs the user out"""
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        if request.user.id != user_id :
            return redirect(request.user)
        if request.method == "POST":
            real_logout(request)
            chk = True
            context = {
                'chk': chk
            }
            return render(request, "logout.html", context)


def login_view(request):
    """displays the login screen"""
    if request.user.is_authenticated:
        return redirect(request.user)
    else:
        form = accountLoginForm(data=(request.POST or None))
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get(
                "username"), password=form.cleaned_data.get("password"))
            if user is not None and user.is_active:
                real_login(request, user)
                return redirect(request.user)

        context = {
            'form': form
        }
        return render(request, "login.html", context)


def change_password_view(request,user_id):
    """For changing user's password"""
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        if request.user.id != user_id :
            return redirect(request.user)
        if request.method == 'POST':
            form = passwordChangeForm(request.user, request.POST)
            context={
                'form':form,
                'chk':False,
            }
            if form.is_valid():
                user = form.save()
                context['chk']=True
                update_session_auth_hash(request, user)  # Important!
                return render(request, 'password_change.html', context)

        else:
            form = passwordChangeForm(request.user, None)
            context={
                'form':form,
                'chk':False,
            }

        return render(request, 'password_change.html', context)


def account_edit_view(request,user_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        if request.user.id != user_id :
            return redirect(request.user)
        if request.method == 'POST':
            form = accountEditForm( request.POST)
            context={
                'form':form,
            }
            if form.is_valid():
                request.user.email=form.cleaned_data.get('email')
                request.user.save()
                return redirect(request.user)

        else:
            form = accountEditForm(initial=request.user.__dict__)
            context={
                'form':form,
            }

        return render(request, 'profile_edit.html', context)


def account_delete_view(request,user_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    else:
        if request.user.id != user_id :
            return redirect(request.user)
        if request.method == 'POST':
            request.user.delete()
            return render(request, 'account_delete.html', {})

        else:
            return redirect(request.user)
