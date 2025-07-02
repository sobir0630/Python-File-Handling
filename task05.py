with open('input/numbers.txt') as f1:
    content = f1.read()

if content:
    nums = [int(n) for n in content.split()]
    avarage_numbers = sum(nums) / len(nums)
        

    with open('Output/output05.txt', 'w') as f2:
        f2.write(f'even numbers: {avarage_numbers}')

else:
    print("topilmadi")