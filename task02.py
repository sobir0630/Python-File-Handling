with open('input/numbers.txt') as f1:
    content = f1.read()

nums = [int(n) for n in content.split()]
result = sum(nums)

with open('Output/output02.txt', 'w') as f2:
    f2.write(f'yig\'indi: {result}')
