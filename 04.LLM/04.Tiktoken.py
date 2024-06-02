import tiktoken
import os

encoding = tiktoken.encoding_for_model("gpt-2")

a = encoding.encode("Il gatto nero attraversa la strada buia.")

os.system('cls')


print(a)
print("\n")
print(encoding.decode(a))