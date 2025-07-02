with open("input/students.txt", "r") as f1:
    name = f1.read()

txt = name.strip().title()

with open("Output/output11.txt", "w") as f2:
    f2.write(txt)