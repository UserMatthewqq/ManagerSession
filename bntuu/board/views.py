import json
import os

from django.contrib.sites import requests
from django.core.files.storage import default_storage
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import requests
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from selenium import webdriver

from board.models import Save_P, SaveImageModel

from board.forms import SaveImageForm


def index(request):
    p_obj = Save_P.objects.all()
    return render(request, 'board/index.html', {'save_p_objects': p_obj})


def save_data(request):
    if request.method == 'POST':
        # Получение данных из POST-запроса
        room_id = request.POST.get('room_id')
        coordinates = request.POST.get('coordinates')
        text = request.POST.get('text')

        save_p_objects = Save_P.objects.filter(room_id=room_id)
        text_values = [obj.text for obj in save_p_objects]

        if text in text_values:
            Save_P.objects.filter(room_id=room_id, text=text).update(coordinates=coordinates)
        else:
            obj = Save_P(room_id=room_id, coordinates=coordinates, text=text)
            obj.save()

        # Возврат JSON-ответа
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})


def load_data(request):
    p_obj = Save_P.objects.all().values()
    return JsonResponse({'save_p_objects': list(p_obj)})


def delete_item(request):
    if request.method == 'POST':
        room_id = request.POST.get('room_id')
        # coordinates = request.POST.get('coordinates')
        text = request.POST.get('text')

        obj = Save_P.objects.filter(room_id=room_id, text=text)
        obj.delete()
        return JsonResponse({'message': 'Элемент успешно удален'})
    else:
        return JsonResponse({'message': 'Ошибка удаления элемента'}, status=500)


def save_upload_image(request):
    if request.method == 'POST':
        form = SaveImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    return JsonResponse({'status': 'error', 'message': 'Only POST method is allowed'})


def load_img(request):
    img_obj = SaveImageModel.objects.all().values()
    return JsonResponse({'saveimagemodel_objects': list(img_obj)})


def save_coord_img(request):
    if request.method == 'POST':
        room_id = request.POST.get('room_id')
        coordinates = request.POST.get('coordinates')
        src = request.POST.get('src')

        SaveImageModel.objects.filter(room_id=room_id, src=src).update(coordinates=coordinates)
        SaveImageModel.objects.filter(room_id=room_id, image=src[6:]).update(coordinates=coordinates)

        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})


def delete_img(request):
    if request.method == 'POST':
        room_id = request.POST.get('room_id')
        src = request.POST.get('src')

        print(src)
        os.remove('media/' + src)

        obj = SaveImageModel.objects.filter(room_id=room_id, image=src)
        obj.delete()
        return JsonResponse({'message': 'Элемент успешно удален!'})
    else:
        return JsonResponse({'message': 'Ошибка удаления элемента!'}, status=500)
