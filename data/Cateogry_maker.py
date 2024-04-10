import json
import os

folder_path = 'place_ids'

category_dict={}
with open("data_revised.csv", "w") as csv_file:
    csv_file.write("business_name, total_results, username, user_id, friends, elite_year, review_count, address, review_text, review_star, date, categories\n")
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.json'):
                full_path = os.path.join(root, file)
                print(full_path)
                with open(full_path, "r", encoding="utf-8") as json_file:
                    try:
                        data = json.load(json_file)
                        for res in data["organic_results"]:
                            print(res['title'], res['categories'])
                            for category in res['categories']:
                                if res['title'] not in category_dict.keys():
                                    category_dict[res['title']] = [category['title']]
                                else:
                                    category_dict[res['title']].append(category['title'])
                    except Exception as e:
                        print(f"error in file {full_path} with error {e}")
                        continue
    print(category_dict)
    with open('data.csv', "r") as csv_data:
        rest_info = csv_data.readlines()
        for i in range(1, len(rest_info)):
            res_title = rest_info[i].split(',')[0]
            print(res_title)
            output_str = rest_info[i].strip()+", "
            if res_title in category_dict.keys():
                print(category_dict[res_title])
                output_str += ' '.join(category_dict[res_title])
            else:
                print("no category found")
                output_str += "no category found"
            csv_file.write(output_str+"\n")






