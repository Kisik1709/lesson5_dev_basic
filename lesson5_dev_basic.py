import os
import random

from faker import Faker

import file_operations

FAKE = Faker("ru_RU")
OUTPUT_DIR = "out_pers"
TEMPLATE = "template/charsheet.svg"
LETTER_MAPING = {
    "а": "а͠",
    "б": "б̋",
    "в": "в͒͠",
    "г": "г͒͠",
    "д": "д̋",
    "е": "е͠",
    "ё": "ё͒͠",
    "ж": "ж͒",
    "з": "з̋̋͠",
    "и": "и",
    "й": "й͒͠",
    "к": "к̋̋",
    "л": "л̋͠",
    "м": "м͒͠",
    "н": "н͒",
    "о": "о̋",
    "п": "п̋͠",
    "р": "р̋͠",
    "с": "с͒",
    "т": "т͒",
    "у": "у͒͠",
    "ф": "ф̋̋͠",
    "х": "х͒͠",
    "ц": "ц̋",
    "ч": "ч̋͠",
    "ш": "ш͒͠",
    "щ": "щ̋",
    "ъ": "ъ̋͠",
    "ы": "ы̋͠",
    "ь": "ь̋",
    "э": "э͒͠͠",
    "ю": "ю̋͠",
    "я": "я̋",
    "А": "А͠",
    "Б": "Б̋",
    "В": "В͒͠",
    "Г": "Г͒͠",
    "Д": "Д̋",
    "Е": "Е",
    "Ё": "Ё͒͠",
    "Ж": "Ж͒",
    "З": "З̋̋͠",
    "И": "И",
    "Й": "Й͒͠",
    "К": "К̋̋",
    "Л": "Л̋͠",
    "М": "М͒͠",
    "Н": "Н͒",
    "О": "О̋",
    "П": "П̋͠",
    "Р": "Р̋͠",
    "С": "С͒",
    "Т": "Т͒",
    "У": "У͒͠",
    "Ф": "Ф̋̋͠",
    "Х": "Х͒͠",
    "Ц": "Ц̋",
    "Ч": "Ч̋͠",
    "Ш": "Ш͒͠",
    "Щ": "Щ̋",
    "Ъ": "Ъ̋͠",
    "Ы": "Ы̋͠",
    "Ь": "Ь̋",
    "Э": "Э͒͠͠",
    "Ю": "Ю̋͠",
    "Я": "Я̋",
    " ": " "
}
SKILLS = [
    "Стремительный прыжок",
    "Электрический выстрел",
    "Ледяной удар",
    "Стремительный удар",
    "Кислотный взгляд",
    "Тайный побег",
    "Ледяной выстрел",
    "Огненный заряд"
]


def main():
    update_skills = []
    for skill in SKILLS:
        for old, new in LETTER_MAPING.items():
            skill = skill.replace(old, new)
        update_skills.append(skill)

    base_dir = os.path.dirname(__file__)
    output_dir = os.path.join(base_dir, OUTPUT_DIR)
    template = os.path.join(base_dir, TEMPLATE)

    os.makedirs(output_dir, exist_ok=True)

    for i in range(10):
        random_skills = (random.sample(update_skills, 3))

        personal = {
            "first_name": FAKE.first_name(),
            "last_name": FAKE.last_name(),
            "job": FAKE.job(),
            "town": FAKE.city(),
            "strength": random.randint(3, 18),
            "agility": random.randint(3, 18),
            "endurance": random.randint(3, 18),
            "intelligence": random.randint(3, 18),
            "luck": random.randint(3, 18),
            "skill_1": random_skills[0],
            "skill_2": random_skills[1],
            "skill_3": random_skills[2],
        }

    filename = os.path.join(output_dir, f"pers_{i + 1}.svg")

    file_operations.render_template(template, filename, personal)


if __name__ == "__main__":
    main()
