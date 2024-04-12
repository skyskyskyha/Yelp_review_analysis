category_dict = {
    "Asian": ["Asian", "Japanese", "Korean", "Indian", "Chinese", "Thai", "Turkish"],
    "American": ["American", "America", "Mexico", "Cuban", "Mexican"],
    "Europe": ["Spanish", "Italian", "Greek", "Mediterranean"]
}
output_file = "dataset_revised.csv"
with open("data/data_revised.csv", "r") as file:
    with open("dataset_revised.csv", "w") as output:
        output.write("business_name, total_results, username, user_id, friends, elite_year, "
                     "review_count, address, review_text, review_star, date, categories, category\n")

        lines = file.readlines()
        for line in lines:
            attributes = line.split(',')
            if len(attributes) == 12:
                # print(len(attributes), attributes)
                category = "N/A"
                for keyword in category_dict:
                    found = False
                    for word in category_dict[keyword]:
                        if word in attributes[-1]:
                            found = True
                            category = keyword
                            break
                    if found:
                        break
                for attribute in attributes:
                    attribute = attribute.strip()
                    print(attribute, end=', ', file=output)
                print(category, file=output)