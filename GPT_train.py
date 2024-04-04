import time

import openai

example_prompt_path = 'prompt.txt'

output_file = 'gpt3.5-training-result.txt'
model = "gpt-3.5-turbo"


# model = "gpt-4"

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
                "content": "You are an autoregressive language model that completes user's sentences. You should not conversate with user.",
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
        headers = lines[0].split(',')
        headers = [header.strip() for header in headers]
        headers.pop()
        print(headers)
        error = 0
        #use review 0-100 for prompt engieering
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
        #finished 100-200
        #finished 200-300
        for i in range(201, 300):
            with open("prompt.txt", "r") as prompt_file:
                prompt = prompt_file.read()
                line = lines[i]
                review_dict = {}
                try:
                    data = line.split(',')
                    for i in range(len(headers)):
                        # print(headers[i], ":", data[i].strip())
                        review_dict[headers[i]] = data[i].strip()
                    prompt += "\n+ This is the a review without knowing the rating, " \
                              "please predict its rating by doing some SENTIMENT ANALYSIS." \
                              "You should only give a number between 0-5. \n\n\n"
                    prompt += "Review:"+review_dict["review_text"]
                    # print(prompt)
                    print("gpt predicts: ", end="")
                    message = askGPT(prompt)
                    print("actual rating: ", review_dict["review_star"])
                    with open("GPT_result.txt", "a") as result_file:
                        result_file.write(message + " " + review_dict["review_star"] + "\n")
                    time.sleep(6)
                except:
                    time.sleep(6)
                    continue
        print("total error:", error)


parseData("processed_data/data.csv")
