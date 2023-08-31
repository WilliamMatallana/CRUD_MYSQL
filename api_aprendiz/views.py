from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Aprendiz

def listar_aprendices(request):
    # Obtener todos los aprendices
    aprendices = Aprendiz.objects.all()

    # Renderizar el template
    return render(request, 'listar_aprendices.html', {'aprendices': aprendices})

def crear_aprendiz(request):
    if request.method == 'POST':
        # Procesar el formulario de nuevo aprendiz
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        numero_documento = request.POST.get('numero_documento')
        tipo_documento = request.POST.get('tipo_documento')
        numero_ficha = request.POST.get('numero_ficha')

        # Crear un nuevo aprendiz
        aprendiz = Aprendiz(nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento,
                            numero_documento=numero_documento, tipo_documento=tipo_documento,
                            numero_ficha=numero_ficha)
        aprendiz.save()

        # Redirigir a la página de inicio
        return HttpResponseRedirect(reverse('listar_aprendices'))
    else:
        # Mostrar el formulario de nuevo aprendiz
        return render(request, 'crear_aprendiz.html')

def ver_aprendiz(request, aprendiz_id):
    # Obtener el aprendiz
    aprendiz = get_object_or_404(Aprendiz, pk=aprendiz_id)

    # Renderizar el template
    return render(request, 'ver_aprendiz.html', {'aprendiz': aprendiz})

def editar_aprendiz(request, aprendiz_id):
    # Obtener el aprendiz
    aprendiz = get_object_or_404(Aprendiz, pk=aprendiz_id)

    if request.method == 'POST':
        # Procesar el formulario de edición de aprendices
        aprendiz.nombre = request.POST.get('nombre')
        aprendiz.apellido = request.POST.get('apellido')
        aprendiz.fecha_nacimiento = request.POST.get('fecha_nacimiento')
        aprendiz.numero_documento = request.POST.get('numero_documento')
        aprendiz.tipo_documento = request.POST.get('tipo_documento')
        aprendiz.numero_ficha = request.POST.get('numero_ficha')

        # Guardar los cambios en el aprendiz
        aprendiz.save()

        # Redirigir a la página de detalles del aprendiz
        return HttpResponseRedirect(reverse('ver_aprendiz', args=[aprendiz.id]))
    else:
        # Mostrar el formulario de edición de aprendices
        return render(request, 'editar_aprendiz.html', {'aprendiz': aprendiz})

def eliminar_aprendiz(request, aprendiz_id):
    # Obtener el aprendiz
    aprendiz = get_object_or_404(Aprendiz, pk=aprendiz_id)

    if request.method == 'POST':
        # Eliminar el aprendiz
        aprendiz.delete()

        # Redirigir a la página de inicio
        return HttpResponseRedirect(reverse('listar_aprendices'))
    else:
        # Mostrar la confirmación de eliminación del aprendiz
        return render(request, 'eliminar_aprendiz.html', {'aprendiz': aprendiz})
