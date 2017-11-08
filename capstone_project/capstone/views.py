from django.shortcuts import render
from django.http import JsonResponse
from .models import AccessData
from .models import MapData


# Create your views here.


def index2(request):
    return render(request, 'capstone/index2.html', {})


def getdata(request):

    user_choice = request.GET.get('graph_name')


    data_set = AccessData.objects.all()
    json_data_set = []
    for data in data_set:
        data_row = {}
        data_row['county_id'] = data.county_id
        data_row['state'] = data.state
        data_row['county'] = data.county
        if user_choice == 'Access 2010':
            data_row['data_value'] = data.pct_access_2010
        elif user_choice == 'Access 2015':
            data_row['data_value'] = data.pct_access_2015
        elif user_choice == 'Diabetes 2008':
            data_row['data_value'] = data.pct_diabetes_2008
        elif user_choice == 'Diabetes 2013':
            data_row['data_value'] = data.pct_diabetes_2013
        elif user_choice == 'Obese 2008':
            data_row['data_value'] = data.pct_obese_2008
        elif user_choice == 'Obese 2013':
            data_row['data_value'] = data.pct_obese_2013
        elif user_choice == 'Grocery 2009':
            data_row['data_value'] = data.grocery_2009
        elif user_choice == 'Grocery 2014':
            data_row['data_value'] = data.grocery_2014
        elif user_choice == 'Supercenter 2009':
            data_row['data_value'] = data.supercenter_2009
        elif user_choice == 'Supercenter 2014':
            data_row['data_value'] = data.supercenter_2014
        elif user_choice == 'Convenience 2014':
            data_row['data_value'] = data.convenience_2009
        elif user_choice == 'Convenience 2014':
            data_row['data_value'] = data.convenience_2014
        elif user_choice == 'White 2010':
            data_row['data_value'] = data.white_2010
        elif user_choice == 'Black 2010':
            data_row['data_value'] = data.black_2010
        elif user_choice == 'Hispanic 2010':
            data_row['data_value'] = data.hispanic_2010
        elif user_choice == 'Asian 2010':
            data_row['data_value'] = data.asian_2010
        elif user_choice == 'American Indian 2010':
            data_row['data_value'] = data.amerindian_2010
        elif user_choice == 'Hawaiian 2010':
            data_row['data_value'] = data.hawaiian_2010

        json_data_set.append(data_row)
    return JsonResponse({'data_row': json_data_set})


def getmetadata(request):
    data_set = MapData.objects.all()
    json_data_set = {}
    for data in data_set:
        data_row = {}
        data_row['variable'] = data.variable
        data_row['header_text'] = data.header_text
        data_row['legend_text'] = data.legend_text
        data_row['lower_bound'] = data.lower_bound
        data_row['upper_bound'] = data.upper_bound

        json_data_set.append(data_row)

    graph_name = request.GET.get('graph_name')
    map_data = MapData.objects.get(variable=graph_name)
    return JsonResponse({'data_row': json_data_set})

def diabetesmap(request):
    return render(request, 'capstone/diabetesmap.html', {})
