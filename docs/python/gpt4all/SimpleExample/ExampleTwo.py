from gpt4all import GPT4All
model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf") # downloads / loads a 4.66GB LLM

res = model.generate("Write a poem about Data Science")

print("res=", res)

with open("Output.txt", "w") as text_file:
    text_file.write(res)