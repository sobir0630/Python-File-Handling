with open('input/numbers.txt') as f1:
    content = f1.read()

nums = [int(n) for n in content.split()]
result = max(nums)

with open('Output/output03.txt', 'w') as f2:
    f2.write(f'max: {result}')