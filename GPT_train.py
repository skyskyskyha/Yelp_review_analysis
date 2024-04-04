import openai

example_prompt_path = 'example_click_option.txt'

output_file = 'gpt4-cot-maxstep_5-miniwob_5problems.txt'
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

askGPT("1+1=?")