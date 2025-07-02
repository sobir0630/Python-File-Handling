with open('input/numbers.txt') as f1:
    name = f1.read().strip()

if name:
    numbers = [int(n) for n in name.split()]
    sort = sorted(numbers)

    with open('output/output10.txt', 'w') as f2:
        f2.write('tartiblangan sonlar:' + '; '.join(map(str, sort)))

else:
    print('xatolik')