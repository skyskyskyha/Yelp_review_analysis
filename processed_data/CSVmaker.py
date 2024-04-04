import json
import os

folder_path = 'reviews'
table_head = \
    ["business_name",
     "total_results",
     "username",
     "user_id",
     "friends",
     "elite_year",
     "review_count",
     "address",
     "review_text",
     "review_star",
     "date"
     ]

with open("data.csv", "w") as csv_file:
    print_to = csv_file  # None for screen, csv_file for csv
    for head in table_head:
        print(head, end=", ", file=print_to)
    print(file=print_to)
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.json'):
                full_path = os.path.join(root, file)
                print(full_path)
                with open(full_path, "r", encoding="utf-8") as json_file:
                    try:
                        data = json.load(json_file)
                        for review in data["reviews"]:
                            print(str(data["search_information"]["business"]), end=", ", file=print_to)
                            print(str(data["search_information"]["total_results"]), end=", ", file=print_to)
                            print(str(review["user"]["name"]), end=", ", file=print_to)
                            print(str(review["user"]["user_id"]), end=", ", file=print_to)
                            print(str(review["user"]["friends"]), end=", ", file=print_to)
                            if "elite_year" in review["user"]:
                                print(str(review["user"]["elite_year"]), end=", ", file=print_to)
                            else:
                                print("N/A", end=", ", file=print_to)
                            print(str(review["user"]["reviews"]), end=", ", file=print_to)
                            print(str(review["user"]["address"].replace(",", " ")), end=", ", file=print_to)
                            print(str(review["comment"]["text"].replace("\n", " ").replace(',', ' ')), end=", ", file=print_to)
                            print(str(review["rating"]), end=", ", file=print_to)
                            print(str(review["date"]), file=print_to)
                    except Exception as e:
                        print(f"error in file {full_path} with error {e}")
                        print(file=print_to)
                        continue
