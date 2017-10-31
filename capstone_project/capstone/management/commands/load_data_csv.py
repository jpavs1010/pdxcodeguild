from django.core.management.base import BaseCommand
from capstone.models import AccessData
import pandas as pd


# erase the database
def erase_database():
    AccessData.objects.all().delete()


path = r'C:\Users\Jessica\PycharmProjects\pdxcodeguild\capstone_project\capstone\management\commands\food_environment_atlas.csv'

# open xls (pick out relevant data)
def open_data():
    with open(path, 'r') as file:
        text = file.read()
    # file = pd.read_excel(open('food environment atlas.xls', 'rb'), sheetname = 'ACCESS')
    # df = load_file.parse()
    # text = pd.read_csv(r'C:\Users\Jessica\PycharmProjects\pdxcodeguild\capstone_project\capstone\management\commands\food_environment_atlas3.csv', dtype={"FIPS": str}, encoding = "ISO-8859-1")
    #print(xl.sheet_names))

    #sheet = xl.parse('ACCESS')
    data_column = 'PCT_LACCESS_POP10'
    state_column = 'State'
    county_column = 'County'
    county_id_column = 'FIPS'
    #print(type(data_column))
    #print(len(data_column))
    #print(data_column[0])
    #for datum in sheet['PCT_LACCESS_POP10']:
    #    print(datum)

    lines = text.split('\n')
    #access_values = []
    for i in range(1, len(lines)):
        access_value = lines[i].split(',')
        county_id = access_value[0]
        state = access_value[1]
        county = access_value[2]
        pct_access = access_value[6]
        access_data = AccessData(county_id=county_id, state=state, county=county, pct_access=pct_access)
        #access_values.append(access_data)
        #all_data.save()

        access_data.save()
        print(f'{((i/len(lines))*100)}%')


class Command(BaseCommand):

    def handle(self, *args, **options):
        erase_database()
        open_data()
