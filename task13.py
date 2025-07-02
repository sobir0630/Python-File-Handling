with open('input/students.txt') as f1:
    name = f1.read().split()

sort = sorted(name, key=str.lower)
with open('output/output13.txt', 'w') as f2:
    f2.write(f'alfabet tartibi: {sort}')