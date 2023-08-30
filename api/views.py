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

    def get(self, request, id = 0):
        if(id > 0):
            companies = list(Company.objects.filter(id=id).values())
            if len(companies) > 0:
                company = companies[0]
                datos = {'message': 'Success', 'companies': company}
            else:
                datos = {'message': 'Company not found'}
        else:
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

    def put(self, request, id):
        jd = json.loads(request.body)
        # print(jd)
        companies = list(Company.objects.filter(id=id).values())
        if (len(companies) >0 ):
            company = Company.objects.get(id=id)
            company.name = jd['name']
            company.website = jd['website']
            company.foundation = jd['foundation']
            company.save()

            datos = {'message': 'Success'}
        else:
            datos = {'message': 'companies not found...'}
        
        return JsonResponse(datos)

    def delete(self, request, id):
        companies = list(Company.objects.filter(id=id).values)
        if (len(companies) > 0):
            Company.objects.filter(id=id).delete()
            datos = {'message': 'success'}
        else:
            datos = {'message': 'company not found...'}

        return JsonResponse(datos)