import json
from docx import Document

def parse_docx(filename):
    doc = Document(filename)
    table = doc.tables[0]

    questions = []

    for row in table.rows[1:]:
        content = row.cells[1].text.strip()
        correct_letter = row.cells[2].text.strip()

        if not content:
            continue

        lines = content.split("\n")

        question_text = lines[0].strip()

        options = []

        for line in lines[1:]:
            line = line.strip()
            if ")" in line:
                option_text = line.split(")", 1)[1].strip()
                options.append(option_text)

        if len(options) != 4:
            print("Ошибка: не 4 варианта")

        letter_map = {
            "А": 0,
            "Б": 1,
            "В": 2,
            "Г": 3
        }

        correct_index = letter_map.get(correct_letter)

        if correct_index is None:
            continue

        questions.append({
            "question": question_text,
            "options": options,
            "correct": correct_index
        })

    return questions

questions_2017 = parse_docx("Теор.вопросы компрессоры 2017 г.docx")
questions_2018 = parse_docx("Теор.вопросы компрессоры 2018 г.docx")

all_questions = questions_2017 + questions_2018

with open("questions.json", "w", encoding="utf-8") as f:
    json.dump(all_questions, f, ensure_ascii=False, indent=4)

print("Готово. Создан questions.json")
print("Количество вопросов:", len(all_questions))