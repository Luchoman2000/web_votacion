from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ImagenForm
from .models import Imagen
import cv2
import numpy as np
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

def index_test(request):
    return HttpResponse("Hello, world. You're at the web_votacion_ocr index.")

def dashboard(request):
    return render(request, 'demo/index.html')

def ver_imagen_view(request, pk):
    imagen = get_object_or_404(Imagen, pk=pk)
    return render(request, 'ver_imagen.html', {'imagen': imagen})

def procesar_imagen_view(request):
    if request.method == 'POST':
        form = ImagenForm(request.POST, request.FILES)
        if form.is_valid():
            imagen_obj = form.save(commit=False)
            
            # Leer la imagen directamente desde request.FILES
            imagen_in_memory = request.FILES['imagen_original']
            nparr = np.fromstring(imagen_in_memory.read(), np.uint8)
            imagen = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            
            # Cargar el clasificador de rostros
            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

            # Procesar la imagen, ejemplo: convertir a escala de grises
            imagen_procesada = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
            
            # detectar caras
            faces = face_cascade.detectMultiScale(imagen_procesada, 1.3, 5)
            
            # dibujar rectangulos en las caras detectadas
            for (x, y, w, h) in faces:
                cv2.rectangle(imagen_procesada, (x, y), (x+w, y+h), (255, 0, 0), 2)
                
            
            _, buf = cv2.imencode('.jpg', imagen_procesada)
            imagen_procesada_content = ContentFile(buf.tobytes())

            # Guardar la imagen procesada en el modelo
            imagen_procesada_nombre = 'procesada_' + imagen_in_memory.name
            imagen_obj.imagen_procesada.save(imagen_procesada_nombre, imagen_procesada_content, save=True)
            
            imagen_obj.save()

            return redirect('ver_imagen', pk=imagen_obj.pk)
    else:
        form = ImagenForm()
    return render(request, 'subir_imagen.html', {'form': form})