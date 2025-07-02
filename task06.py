with open('input/numbers.txt') as f1:
    content = f1.read()

if content:
    nums = [int(n) for n in content.split()]
    even_numbers = [n for n in nums if n % 3 == 0]
        

    with open('Output/output06.txt', 'w') as f2:
        f2.write(f'even numbers:' + '; '.join(map(str, even_numbers)))

else:
    print("topilmadi")