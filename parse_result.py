import re

pattern = r'\b[1-5]\b'

with open("GPT_result.txt", "r") as result:
    data = result.readlines()
    for line in data:
        matches = re.findall(pattern, line)
        if len(matches) == 2:
            with open("parsed_data.txt", "a") as parse_file:
                print(matches[0], matches[1], file=parse_file)
