from django.shortcuts import render
from django.db import connection
from django.http import JsonResponse
from .models import AccessData
from .models import MapData

import pandas as pd


def index2(request):
    mapdata = MapData.objects.all()
    context = {'mapdata': mapdata}
    return render(request, 'capstone/index2.html', context)


def get_attribute(variable_name, data_row):
    if variable_name == 'Access 2010':
        return data_row.pct_access_2010
    elif variable_name == 'Access 2015':
        return data_row.pct_access_2015
    elif variable_name == 'Diabetes 2008':
        return data_row.pct_diabetes_2008
    elif variable_name == 'Diabetes 2013':
        return data_row.pct_diabetes_2013
    elif variable_name == 'Obese 2008':
        return data_row.pct_obese_2008
    elif variable_name == 'Obese 2013':
        return data_row.pct_obese_2013
    elif variable_name == 'Grocery 2009':
        return data_row.grocery_2009
    elif variable_name == 'Grocery 2014':
        return data_row.grocery_2014
    elif variable_name == 'Supercenter 2009':
        return data_row.supercenter_2009
    elif variable_name == 'Supercenter 2014':
        return data_row.supercenter_2014
    elif variable_name == 'Convenience 2009':
        return data_row.convenience_2009
    elif variable_name == 'Convenience 2014':
        return data_row.convenience_2014
    elif variable_name == 'White 2010':
        return data_row.white_2010
    elif variable_name == 'Black 2010':
        return data_row.black_2010
    elif variable_name == 'Hispanic 2010':
        return data_row.hispanic_2010
    elif variable_name == 'Asian 2010':
        return data_row.asian_2010
    elif variable_name == 'American Indian 2010':
        return data_row.amerindian_2010
    elif variable_name == 'Hawaiian 2010':
        return data_row.hawaiian_2010
    return None


def getdata(request):

    user_choice = request.GET.get('graph_name')

    data_set = AccessData.objects.all()
    json_data_set = []
    for data in data_set:
        data_row = {}
        data_row['county_id'] = data.county_id
        data_row['state'] = data.state
        data_row['county'] = data.county
        data_row['data_value'] = get_attribute(user_choice, data)
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

import math
def correlation(request):
    mapdata = MapData.objects.all()


    user_choice1 = request.GET.get('v1')
    user_choice2 = request.GET.get('v2')

    correlation = ''

    if user_choice1 is not None and user_choice2 is not None:
        data_column1 = []
        data_column2 = []
        for data_row in AccessData.objects.all():
            datum1 = get_attribute(user_choice1, data_row)
            datum2 = get_attribute(user_choice2, data_row)
            if datum1 is not None and datum2 is not None:
                data_column1.append(float(datum1))
                data_column2.append(float(datum2))

        df = pd.DataFrame({'datum1': data_column1, 'datum2':data_column2})
        correlation = user_choice1+' x '+user_choice2+': '+str(df['datum1'].corr(df['datum2'], method='spearman'))

    # query = str(AccessData.objects.all().query)
    # d = pd.read_sql_query(query, connection)
    # df = pd.DataFrame(d)
    # df_corr = pd.DataFrame(df)
    #
    # for mapdata in mapdata:
    #     if user_choice1 == {{mapdata.variable}} and user_choice2 == {{mapdata.variable}}:
    #         df_corr['{{mapdata.variable}}'].corr(df_corr['{{mapdata.variable}}'], method='spearman')
    context = {'mapdata': mapdata, 'correlation': correlation}
    return render(request, 'capstone/correlation.html', context)

