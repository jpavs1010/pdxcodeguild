from django.shortcuts import render
from django.http import JsonResponse
from .models import AccessData
from .models import MapData

import pandas as pd


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
        elif user_choice == 'Convenience 2009':
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
    return JsonResponse({'all_data': json_data_set})


def getmetadata(request):
    graph_name = request.GET.get('graph_name')
    map_data = MapData.objects.get(variable=graph_name)
    d = {'variable': map_data.variable,
         'header_text': map_data.header_text,
         'legend_text': map_data.legend_text,
         'upper_bound': map_data.upper_bound,
         'lower_bound': map_data.lower_bound}
    return JsonResponse(d)


def correlation(request):
    user_choice1 = request.GET.get('var1')
    user_choice2 = request.GET.get('var2')



    d = AccessData.objects.all()
    df = pd.DataFrame(data=d)
    df_corr = pd.DataFrame(df)

    x = df_corr[''].corr(df_corr[''], method='spearman')

    # check if variable selected


    return render(request, 'capstone/correlation.html', {})


