import os
with open('TREES.lua', 'r', encoding='utf-8') as f:
    code=f.read()
code = code[code.index('-- Code begins here'):].replace('enable_vertical_branches_generate_leaves_only', 'enable_leaves_only_on_vertical_branches')

for file_name in list(map(lambda x: 'presets/' + x, os.listdir('presets'))) + ["TREES.txt"]:
    with open(file_name, 'r', encoding='utf-8') as f:
        inf = f.read()
        inf = inf.replace('enable_vertical_branches_generate_leaves_only', 'enable_leaves_only_on_vertical_branches')
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(inf[:inf.index('-- Code begins here')] + code)

