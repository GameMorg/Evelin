import openai


def main():
    openai.api_base = "http://localhost:4891/v1"

    openai.api_key = "not needed for a local LLM"

    # Set up the prompt and other parameters for the API request
    prompt = "Who is Michael Jordan?"

    #model = "mpt-7b-chat"
    model = "gpt4all-j-v1.3-groovy"

    # Make the API request
    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        max_tokens=50,
        temperature=0.28,
        top_p=0.95,
        n=1,
        echo=True,
        stream=False
    )

    # Print the generated completion
    print(response)


if __name__=="__main__":
    main()