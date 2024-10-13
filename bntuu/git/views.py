import os

from django.http import JsonResponse
from django.shortcuts import render

from git.forms import SaveFilesForm

from git.models import SaveFilesModell


def index(request):
    return render(request, 'git/index.html')


def save_upload_file(request):
    if request.method == 'POST':
        form = SaveFilesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})
    return JsonResponse({'status': 'error', 'message': 'Only POST method is allowed'})


def load_data(request):
    f_obj = SaveFilesModell.objects.all().values()
    return JsonResponse({'save_files_objects': list(f_obj)})


def delete_file(request):
    if request.method == 'POST':
        room_id = request.POST.get('room_id')
        # coordinates = request.POST.get('coordinates')
        file = request.POST.get('file')

        os.remove('media/files/' + file)

        obj = SaveFilesModell.objects.filter(room_id=room_id, filee='files/' + file)
        obj.delete()
        return JsonResponse({'message': 'Элемент успешно удален'})
    else:
        return JsonResponse({'message': 'Ошибка удаления элемента'}, status=500)
