import time

import openai

example_prompt_path = 'prompt.txt'

output_file = 'gpt3.5-fine-tuning-result-american.txt'
# model = "gpt-3.5-turbo"

model = 'ft:gpt-3.5-turbo-1106:personal:cs6474:9CGT9LCd'
# openai.FineTuningJob.create(
#     file=open("finetuning.jsonl", "rb"),
#     purpose="fine-tune"
# )


def askGPT(pt):
    # print("Asking GPT...")
    response = openai.ChatCompletion.create(
        model=model,
        temperature=0,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        max_tokens=256,
        messages=[
            {
                "role": "system",
                "content": "You are rating predictor with given review text. Do some sentiment analysis and predict a rating from 1-5, only print a single number.",
            },
            {"role": "user", "content": pt},
        ],
    )
    # print(response)
    message = response["choices"][0]["message"]["content"]
    print(message)
    return message


def parseData(fn):
    with open(fn, "r") as file:
        lines = file.readlines()
        # print(lines[0])
        headers = lines[0].split(',')
        headers = [header.strip() for header in headers]
        # headers.pop()
        # print(headers)
        error = 0
        # use review 0-100 for prompt engieering
        for i in range(100):
            with open("prompt.txt", "a") as output:
                line = lines[i]
                review_dict = {}
                try:
                    data = line.split(',')
                    for i in range(len(headers)):
                        # print(headers[i], ":", data[i].strip())
                        review_dict[headers[i]] = data[i].strip()
                    # print("review:", review_dict["review_text"], file=None)
                    # print("rating:", review_dict["review_star"], file=None)
                except:
                    error += 1
                    continue
        # finished 100-200
        # finished 200-300
        # finished 300-400
        # finishing 400-500
        for i in range(1000, 2000):
            with open("prompt.txt", "r") as prompt_file:
                prompt = prompt_file.read()
                line = lines[i]
                # print(line)
                review_dict = {}
                try:
                    data = line.split(',')
                    for i in range(len(headers)):
                        # print(headers[i], ":", data[i].strip())
                        review_dict[headers[i]] = data[i].strip()
                    # prompt += "\n+ This is the a review without knowing the rating, " \
                    #           "please predict its rating by doing some SENTIMENT ANALYSIS." \
                    #           "You should only give a number between 0-5. \n\n\n"
                    prompt = "Review:" + review_dict["review_text"]
                    # print(prompt)
                    if "American" not in review_dict["category"]:
                        print("skip")
                        continue
                    print("gpt predicts: ", end="")
                    message = askGPT(prompt)
                    print("actual rating: ", review_dict["review_star"])
                    with open(output_file, "a") as result_file:
                        result_file.write(message + " " + review_dict["review_star"] + "\n")
                    time.sleep(6)
                except:
                    time.sleep(6)
                    continue
        print("total error:", error)


parseData("dataset_revised.csv")
