from gpt4all import GPT4All


def neural_network_response(message):
    model = GPT4All("orca-mini-3b-gguf2-q4_0.gguf")
    output = model.generate(message, max_tokens=20)
    return(output)