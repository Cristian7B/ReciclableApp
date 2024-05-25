from django.http import HttpResponse
from django.shortcuts import render

from django.http import JsonResponse

def inicio(request):
    return render(request, "Reciclable/inicio.html/")

def tecnologias(request):
    return render(request, "Reciclable/tecnologias.html/")

def camara(request):
    return render(request, "Reciclable/camara.html/")

# views.py
import base64
from django.core.files.base import ContentFile
from django.http import JsonResponse
from PIL import Image
import io

def guardar_foto(request):
    if request.method == 'POST':
        image_data = request.POST.get('image_data')
        if image_data:
            format, imgstr = image_data.split(';base64,')
            ext = format.split('/')[-1]
            img_data = base64.b64decode(imgstr)


            image = Image.open(io.BytesIO(img_data)) #prueba
            imagenprueba = image.convert('L')

            buffer = io.BytesIO()
            imagenprueba.save(buffer, format=ext)
            buffer.seek(0)
            imagenprueba_data = buffer.getvalue()

            imagenprueba_base64 = base64.b64encode(imagenprueba_data).decode('utf-8')
            imagenprueba_url = f"data:image/{ext};base64,{imagenprueba_base64}"

            return JsonResponse({'status': 'ok', 'imagenprueba_url': imagenprueba_url})
        return JsonResponse({'status': 'fail'}, status=400)

    return JsonResponse({'status': 'fail'}, status=405)

