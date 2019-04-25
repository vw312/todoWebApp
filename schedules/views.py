from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response


from .forms import scheduleCreateForm,scheduleEditForm
from schedules.models import Schedules
from .serializers import scheduleSerializer
from timezone.models import timezone

def create_schedule(request,user_id):
    """Displays screen for creating schedules"""
    if user_id != request.user.id:
        return redirect(request.user)
    if request.method =="POST":
        form = scheduleCreateForm(data=request.POST )
        if form.is_valid():
            description=form.cleaned_data.get('description')
            what_todo=form.cleaned_data.get('what_todo')
            date_time=form.cleaned_data.get('date_time')

            Schedules.objects.create(what_todo=what_todo,date_time=date_time,user_id=user_id)

            return redirect(request.user)
    else:
        form =  scheduleCreateForm()
    context={
        'form':form,
    }
    return render(request,'schedule_create_view.html',context)

def edit_schedule(request,user_id,schedule_id):
    """Displays screen for editing schedules"""
    if user_id != request.user.id:
        return redirect(request.user)

    schedule=Schedules.objects.get(id=schedule_id)
    if request.method == "POST":
        form = scheduleEditForm(request.POST,initial=schedule.__dict__)
        if form.is_valid():
            if form.has_changed():
                schedule.description=form.cleaned_data.get('description')
                schedule.what_todo=form.cleaned_data.get('what_todo')
                schedule.date_time=form.cleaned_data.get('date_time')
                schedule.state_user=form.cleaned_data.get('state_user')
                schedule.state_db=False
                schedule.save()
                return redirect(request.user)
            else :
                return redirect(request.user)

    else :
        form = scheduleEditForm(initial=schedule.__dict__)

    context={
        'form':form,
    }
    return render(request,"schedule_edit.html",context)

def delete_schedule(request,user_id,schedule_id):
    """Deletes schedules"""
    if user_id != request.user.id:
        return redirect(request.user)

    if request.method == "POST":
        Schedules.objects.filter(id=schedule_id).delete()
        return render(request,"schedule_delete.html",{})

    else :
        return redirect(request.user)

class scheduleList(APIView):
    """RestFul API"""
    def get(self,request,user_id):
        schedules= Schedules.objects.filter(user=user_id)
        serializer=scheduleSerializer(schedules,many=True)
        return Response(serializer.data)

    def post(self):
        pass
