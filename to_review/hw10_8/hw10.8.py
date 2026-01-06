input_file = "input.txt"
output_file = "output.txt"

with open(input_file, "w", encoding="utf-8") as f:
    f.write(
        "Первая строка\n"
        "Вторая строка\n"
        "Третья строка\n"
    )

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

lines = lines[:-1]

with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(lines)

