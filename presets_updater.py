import os
with open('TREES.lua', 'r', encoding='utf-8') as f:
    code=f.read()
code = code[code.index('-- Код начинается тут'):]

for file_name in list(map(lambda x: 'presets/' + x, os.listdir('presets'))) + ["TREES.txt"]:
    with open(file_name, 'r', encoding='utf-8') as f:
        inf = f.read()
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(inf[:inf.index('-- Код начинается тут')] + code)