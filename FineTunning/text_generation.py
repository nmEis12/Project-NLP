import numpy as np
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

np.random.seed(42)
torch.manual_seed(42)
tokenizer = GPT2Tokenizer.from_pretrained("models/essays/trained")
model = GPT2LMHeadModel.from_pretrained("models/essays/trained")
model.cuda()

text = input("Начало предложения: ")
inpt = tokenizer.encode(text, return_tensors="pt")
print("Генерация...")
out = model.generate(inpt.cuda(),
                     max_length=100,
                     do_sample=True,
                     top_k=1,
                     top_p=0.5,
                     no_repeat_ngram_size=2)

print(tokenizer.batch_decode(out)[0])
