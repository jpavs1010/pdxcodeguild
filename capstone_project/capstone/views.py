from django.shortcuts import render
from django.http import JsonResponse
from .models import AccessData


# Create your views here.


def index(request):
    return render(request, 'capstone/index.html', {})


def getdata(request):
    data_set = AccessData.objects.all()
    json_data_set = []
    for data in data_set:
        all_data = {}
        all_data['state'] = data.state
        all_data['county'] = data.county
        all_data['pct_access'] = data.pct_access
        all_data['county_id'] = data.county_id
        all_data['pct_obese'] = data.pct_obese
        all_data['pct_diabetes'] = data.pct_diabetes
        json_data_set.append(all_data)
    return JsonResponse({'all_data': json_data_set})


def diabetesmap(request):
    return render(request, 'capstone/diabetesmap.html', {})

def obesemap(request):
    return render(request, 'capstone/obesemap.html', {})