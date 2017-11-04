from django.core.management.base import BaseCommand
from capstone.models import AccessData
import pandas as pd


# erase the database
def erase_database():
    AccessData.objects.all().delete()



def open_data():
    file = r'C:\Users\Jessica\PycharmProjects\pdxcodeguild\capstone_project\capstone\management\commands\food_environment_atlas.xls'
    xls_file = pd.ExcelFile(file)

    # df = pd.read_excel(file, converters={'FIPS': str})
    # print(df['Food Environment Atlas data download'][1])
    #print(xls_file.sheet_names)
    print(xls_file.parse('ACCESS', converters={'FIPS': str})['FIPS'][0])


# open xls (pick out relevant data)
def open_data2():
    file = r'C:\Users\Jessica\PycharmProjects\pdxcodeguild\capstone_project\capstone\management\commands\food_environment_atlas.xls'
    # worksheets = ['ACCESS', 'HEALTH']
    # df = pd.read_excel(file, sheetname=worksheets, converters={'FIPS': str})
    # access_worksheet = df['ACCESS']
    # health_worksheet = df['HEALTH']

    df1 = pd.read_excel(file, sheetname='ACCESS', converters={'FIPS': str}, usecols=[0, 1, 2, 6])
    df2 = pd.read_excel(file, sheetname='HEALTH', converters={'FIPS': str}, usecols=[0, 4, 6])

    df_join = pd.merge(df1, df2, on='FIPS', how='inner')





    data_column = df_join['PCT_LACCESS_POP10']
    state_column = df_join['State']
    county_column = df_join['County']
    county_id_column = df_join['FIPS']
    diabetes_column = df_join['PCT_DIABETES_ADULTS13']
    obese_column = df_join['PCT_OBESE_ADULTS13']


    for i in range(len(data_column)):
        pct_access = data_column[i]
        state = state_column[i]
        county = county_column[i]
        county_id = county_id_column[i]
        pct_diabetes = diabetes_column[i]
        pct_obese = obese_column[i]

        all_data = AccessData(state=state, county=county, pct_access=pct_access, county_id=county_id,
                              pct_diabetes=pct_diabetes, pct_obese=pct_obese)
        all_data.save()

        print(f'{((i/len(data_column))*100)}%')

    # df_corr = pd.DataFrame(df_join, columns=['PCT_LACCESS_POP10', 'PCT_DIABETES_ADULTS13', 'PCT_OBESE_ADULTS13'])
    # df_corr['PCT_LACCESS_POP10'].corr(df_corr['PCT_DIABETES_ADULTS13'], method='spearman')
    # df_corr['PCT_LACCESS_POP10'].corr(df_corr['PCT_OBESE_ADULTS13'], method='spearman')

class Command(BaseCommand):

    def handle(self, *args, **options):
        erase_database()
        open_data()
