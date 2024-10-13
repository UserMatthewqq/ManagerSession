from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from g4f.client import Client
from django.views.generic import View
from django.http import JsonResponse
from .forms import RegisterForm, RoomForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password

from .models import Room


def index(request):
    return render(request, 'main/index.html')


@login_required
def git(request):
    data = request.GET.get('room')
    return render(request, 'git/index.html', {'room_id': data})


@login_required
def video(request):
    return render(request, 'videoconference_app/dashboard.html')


@login_required
def board(request):
    data = request.GET.get('room')
    return render(request, 'board/index.html', {'room_id': data})


@login_required
def gpt(request):
    return render(request, 'main/gpt.html')


def messenger(request):
    return HttpResponse("<h1>MESSENGER<h1>")


@login_required
def after_reg(request):
    return render(request, 'main/after_reg.html')


@login_required
def room(request):
    return render(request, 'main/room.html')


class MyAction(View):
    def post(self, *args, **kwargs):
            data = {}

            # Получаем данные из запроса
            action = self.request.POST.get('action')
            req = self.request.POST.get('req')

            # Проверяем что значение соответствует ожидаемому
            # и возвращаем число
            # иначе строку с текстом Error
            if action == 'NeedGpt':
                client = Client()
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": req}],
                )
                data['result'] = response.choices[0].message.content
            else:
                data['result'] = 'Error'
            return JsonResponse(data)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'main/login.html', {'success': "Registration successful. Please login."})
        else:
            error_message = form.errors.as_text()
            return render(request, 'main/register.html', {'error': error_message})

    return render(request, 'main/register.html')


def login_view(request):
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/after_reg")
        else:
            return render(request, 'main/login.html', {'error': "Invalid credentials. Please try again."})

    return render(request, 'main/login.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect("/")


@login_required
def create_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            hashed_password = make_password(password)
            room = Room(name=name, password=hashed_password)
            room.save()
            # Дополнительные действия, например, перенаправление на страницу комнаты
            return redirect('room_detail', room_id=room.id)
    else:
        form = RoomForm()
    return render(request, 'main/create_room.html', {'form': form})


@login_required
def enter_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            password = form.cleaned_data['password']
            try:
                room = Room.objects.get(name=name)
                if check_password(password, room.password):
                    # Пароль совпадает
                    # Дополнительные действия, например, перенаправление на страницу комнаты

                    return redirect('room_detail', room_id=room.id)
                else:
                    # Пароль не совпадает
                    form.add_error(None, 'Неверное имя комнаты или пароль')
            except Room.DoesNotExist:
                form.add_error(None, 'Неверное имя комнаты или пароль')
    else:
        form = RoomForm()
    return render(request, 'main/enter_room.html', {'form': form})


@login_required
def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    # Дальнейший код для обработки страницы комнаты с использованием объекта room

    return render(request, 'main/room.html', {'room': room, 'room_id': room_id})

