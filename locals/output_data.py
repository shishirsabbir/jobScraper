import csv
import json


def exportData(filename ,data_list):

    fields = list(data_list[0].keys())

    with open(f'{filename}_json.json', mode='w', encoding='utf-8') as json_output_file:
        json_data = json.dumps(data_list)
        json_output_file.write(json_data)
        print('--Data Saved as JSON file!')

    with open(f'{filename}_csv.csv', mode='w', encoding='utf-8', newline='') as csv_output_file:
        dict_writer = csv.DictWriter(csv_output_file, fieldnames=fields)
        dict_writer.writeheader()
        dict_writer.writerows(data_list)
        print('--Data Saved as CSV file!')