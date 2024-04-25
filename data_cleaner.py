category_dict = {
    "Asian": ["Asian", "Japanese", "Korean", "Indian", "Szechuan", "Vietnamese",
              "Chinese", "Thai", "Turkish", "Indonesian", "Persian", "Sushi", "Lebanese"],
    "American": ["American", "Barbeque", "Southern", "Burgers",
                                                     "Pizza", "Steakhouse", "Cajun"],
    "Europe": ["Spanish", "Italian", "Greek", "Mediterranean", "French", "Turkish"],
    "Latin American": ["Mexico", "Mexican", "Cuban", "Tacos", "Latin"]
}
output_file = "dataset_revised.csv"
with open("data/data_revised.csv", "r") as file:
    with open("dataset_revised2.csv", "w") as output:
        output.write("business_name, total_results, username, user_id, friends, elite_year, "
                     "review_count, address, review_text, review_star, date, categories, main_category"
                     ", sub_category\n")

        lines = file.readlines()
        for line in lines:
            attributes = line.split(',')
            if len(attributes) == 12:
                # print(len(attributes), attributes)
                category = ""
                sub_category = ""
                category_set = set()
                sub_category_set = set()
                for keyword in category_dict:
                    found = False
                    for word in category_dict[keyword]:
                        if word in attributes[-1]:
                            found = True
                            if keyword not in category_set:
                                category += keyword + " "
                            if word not in sub_category_set:
                                sub_category += word + " "
                            category_set.add(keyword)
                            sub_category_set.add(word)
                            # break
                    # if found:
                    #     break
                for attribute in attributes:
                    attribute = attribute.strip()
                    print(attribute, end=', ', file=output)
                print(category + ', ' + sub_category, file=output)
