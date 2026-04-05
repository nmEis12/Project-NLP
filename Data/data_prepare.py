import numpy as np
import pandas as pd
import re

with open(r"D:\DataSet\Dal.txt", 'r',encoding='utf-8') as file:
    dataset = file.read()

dataset = dataset.replace('.', '\n')

to_remove = ['церк', "стар", "кавк"]

def prepare_text(text):

    text = re.sub(r'[^\w\s]', '', text.lower())

    for _ in to_remove:
        text = text.replace(_, '')

    return text

prepared_text = prepare_text(dataset)

with open(r"D:\Projects\AI\Dataset.txt", 'w', encoding='utf-8') as file:
    file.write(prepared_text)
