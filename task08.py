with open('input/numbers.txt') as f:
    name = f.read()

if name:
    nums = [int(n) for n in name.split()]
    assign = [n for n in nums if n % 5 == 0]

    count = len(assign)\

    with open('output/output08.txt', 'w') as y:
        y.write(f'namburs: {count}\n')
        y.write('divisable by 5: ' +  '; '.join(map(str, assign)))

else:
    print('xatollik!!!')