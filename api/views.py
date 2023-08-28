from django.http import JsonResponse
from django.views import View
from .models import Company
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json


class CompanyView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        companies = list(Company.objects.values())
        if len(companies) > 0:
            datos = {'message': 'Success', 'companies':companies}
        else:
            datos = {'message': 'companies not found...'}
        return JsonResponse(datos)

    def post(self, request):
        # print(request.body)
        js = json.loads(request.body)
        # print(js)
        Company.objects.create(name=js['name'], website=js['website'], foundation=js['foundation'])
        datos = {'message': 'Success'}
        return JsonResponse(datos)

    def put(self, request):
        pass

    def delete(self, request):
        pass
