import json
import xlrd

with open("sentimentBySuburb.json") as f:
    dict_f = json.load(f)
    print(dict_f)

def open_excel(file= 'suburb_postcode.xlsx'):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(str(e))


