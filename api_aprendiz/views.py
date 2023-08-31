from django.http import JsonResponse
from django.views import View
from .models import Aprendiz
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json


class ApprenticesView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get (self, request, id = 0) :
        if (id > 0) :
            apprentices = list(Aprendiz.objects.filter(id=id).values())
            if len(apprentices) > 0 :
                apprentice = apprentices[0]
                datos = {'message': 'success', 'apprentices': apprentice}
            else :
                datos = {'message': 'apprentice not found'}
        else:
            apprentices = list(Aprendiz.objects.values())
            if len(apprentices) > 0:
                datos = {'message': 'Success', 'apprentices':apprentices}
            else:
                datos = {'message': 'apprentices not found...'}
        return JsonResponse(datos)
    
    def post (self, request) :
        js = json.loads(request.body)
        Aprendiz.objects.create(nombre =js['nombre'], 
                                apellido = js['apellido'], 
                                fecha_nacimiento = js['fecha_nacimiento'], 
                                numero_documento = js['numero_documento'], 
                                tipo_documento = js['tipo_documento'], 
                                numero_ficha = js['numero_ficha'])
        datos = {'message': 'Success'}
        return JsonResponse(datos)
    
    def put (self, request, id):
        jd = json.loads(request.body)
        apprentices = list(Aprendiz.objects.filter(id=id).values())
        if len(apprentices) > 0:
            apprentice = Aprendiz.objects.get(id=id)
            apprentice.nombre = jd['nombre']
            apprentice.apellido = jd['apellido']
            apprentice.fecha_nacimiento = jd['fecha_nacimiento']
            apprentice.numero_documento = jd['numero_documento']
            apprentice.tipo_documento = jd['tipo_documento']
            apprentice.numero_ficha = jd['numero_ficha']
            apprentice.save()

            datos = {'message': 'Success'}
        else:
            datos = {'message': 'Apprentices not found...'}
        
        return JsonResponse(datos)
    
    def delete(self, request, id):
        apprentices = list(Aprendiz.objects.filter(id=id).values())
        if (len(apprentices) > 0):
            Aprendiz.objects.filter(id=id).delete()
            datos = {'message': 'success'}
        else:
            datos = {'message': 'Apprentice not found...'}

        return JsonResponse(datos)