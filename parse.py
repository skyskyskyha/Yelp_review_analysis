import json

with open('231-240.json', 'r', encoding='utf-8') as file:
    data_dict = json.load(file)


# print(data_dict['organic_results'])


with open('place_ids.txt', 'a') as file:
    for result in data_dict['organic_results']:
        print(result['place_ids'][0])
        file.write(result['place_ids'][0]+"\n")