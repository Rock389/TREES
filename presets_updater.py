import os
with open('TREES.txt', 'r', encoding='utf-8') as f:
    code=f.read()
code = code[code.index('-- Код начинается тут'):]

for file_name in os.listdir('presets'):
    with open('presets/' + file_name, 'r', encoding='utf-8') as f:
        inf = f.read()
    with open('presets/' + file_name, 'w', encoding='utf-8') as f:
        f.write(inf[:inf.index('-- Код начинается тут')] + code)