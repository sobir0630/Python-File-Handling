with open('input/numbers.txt') as f1:
    name = f1.read()

if name:
    numbers = [int(n) for n in name.split()]

    digit_counts = {}
    for nambur in numbers:
        digit_len = len(str(numbers))
        if digit_len in digit_counts:
            digit_counts[digit_len] += 1
        else:
            digit_counts[digit_len] = 1

    with open('output/output09,txt', 'w') as f2:
        for digit, count in sorted(digit_counts.items()):
            f2.write(f"{digit} xonali sonlar {count} ta \n")

else:
    print('xatolik')