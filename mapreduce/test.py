import json

with open("sentimentByHours.json") as f:
    dict_f = json.load(f)
    sum_value = 0
    for line in dict_f["rows"]:
        sum_value += line['value']
    print(sum_value) # 77875