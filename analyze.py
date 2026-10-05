INPUT_FILE = "students.csv"
OUTPUT_FILE = "result.txt"

the_best_student = None
the_bs_score = 0
students_number = 0
math = 0
english = 0
python = 0
with open(INPUT_FILE, "r", encoding="utf-8") as f:
    next(f)
    lines = f.readlines()
    for line in lines:
        students_number += 1
        line = line.strip()
        words = line.split(",")
        sym_rew_stud = 0
        for word in words[1::]:
            sym_rew_stud += int(word)
        math += int(words[1])
        english += int(words[2])
        python += int(words[3])
        sym_rew_stud = sym_rew_stud / 3
        if sym_rew_stud > the_bs_score:
            the_best_student = words[0]
            the_bs_score = sym_rew_stud

math = round(math/students_number, 1)
eng = round(english/students_number, 1)
py = round(python/students_number, 1)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("\n")
    f.write("Середній бал по класу: \n")
    f.write(f"math: {math}\n")
    f.write(f"python: {py}\n")
    f.write(f"english: {eng}\n")
    f.write("\n")
    f.write(f"Найкращий студент: {the_best_student} ({the_bs_score})\n")
    f.write("\n")

print("Середній бал по класу: \n")
print(f"math: {math}")
print(f"python: {py}")
print(f"english: {eng}\n")
print(f"Найкращий студент: {the_best_student} ({the_bs_score})")