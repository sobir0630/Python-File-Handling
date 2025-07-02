with open('input/numbers.txt') as f1:
    name = f1.read()

if name:
    assign = [int(n) for n in name.split()]
    result = [n**2 for n in assign]

    with open('Output/output07.txt', 'w') as f2:
        f2.write(f'square:' + '; '.join(map(str, result)))
else:
    print("xatolik!!!")