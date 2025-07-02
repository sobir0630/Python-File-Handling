with open('input/students.txt') as f1:
    names = f1.read().split()

count = len(names)

with open('output/output12.txt', 'w') as f2:
    f2.write(f'ismlar: {count}')
