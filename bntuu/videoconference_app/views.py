from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request, 'index.html')

@login_required
def dashboard(request):
    return render(request, 'videoconference_app/dashboard.html', {'name': request.user.first_name})

@login_required
def videocall(request):
    return render(request, 'videoconference_app/videocall.html', {'name': request.user.first_name + " " + request.user.last_name})


@login_required
def join_room(request):
    if request.method == 'POST':
        roomID = request.POST['roomID']
        return redirect("/meeting?roomID=" + roomID)
    return render(request, 'videoconference_app/joinroom.html')
