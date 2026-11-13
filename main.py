"""Кейс-задача № 2: дата рождения и её вывод символами '*'.
Запуск: python main.py (Python 3.8+).
"""

import calendar
from datetime import date

WEEKDAYS_RU = (
    "понедельник", "вторник", "среда", "четверг",
    "пятница", "суббота", "воскресенье",
)

# Каждый символ занимает 5 столбцов и 7 строк.
DIGITS = {
    "0": ("*****", "*   *", "*   *", "*   *", "*   *", "*   *", "*****"),
    "1": ("  *  ", " **  ", "  *  ", "  *  ", "  *  ", "  *  ", "*****"),
    "2": ("*****", "    *", "    *", "*****", "*    ", "*    ", "*****"),
    "3": ("*****", "    *", "    *", "*****", "    *", "    *", "*****"),
    "4": ("*   *", "*   *", "*   *", "*****", "    *", "    *", "    *"),
    "5": ("*****", "*    ", "*    ", "*****", "    *", "    *", "*****"),
    "6": ("*****", "*    ", "*    ", "*****", "*   *", "*   *", "*****"),
    "7": ("*****", "    *", "    *", "   * ", "  *  ", "  *  ", "  *  "),
    "8": ("*****", "*   *", "*   *", "*****", "*   *", "*   *", "*****"),
    "9": ("*****", "*   *", "*   *", "*****", "    *", "    *", "*****"),
    " ": ("  ",) * 7,
}


def parse_birthdate(day: int, month: int, year: int, today: date = None) -> date:
    """Проверка реальности даты и того, что она не находится в будущем."""
    birthday = date(year, month, day)  # ValueError для невозможных дат
    if birthday > (today or date.today()):
        raise ValueError("Дата рождения не может находиться в будущем")
    return birthday


def weekday_name(birthday: date) -> str:
    return WEEKDAYS_RU[birthday.weekday()]


def is_leap_year(year: int) -> bool:
    return calendar.isleap(year)


def calculate_age(birthday: date, today: date = None) -> int:
    today = today or date.today()
    if birthday > today:
        raise ValueError("Дата рождения не может находиться в будущем")
    return today.year - birthday.year - (
        (today.month, today.day) < (birthday.month, birthday.day)
    )


def render_stars(value: str) -> str:
    """Собирает семь строк из символов *. Формат dd mm yyyy."""
    if any(character not in DIGITS for character in value):
        raise ValueError("Допускаются только цифры и пробелы")
    return "\n".join(
        " ".join(DIGITS[character][row] for character in value)
        for row in range(7)
    )


def main() -> None:
    print("Введите дату рождения (три отдельных числа).")
    try:
        day = int(input("День: ").strip())
        month = int(input("Месяц: ").strip())
        year = int(input("Год: ").strip())
        birthday = parse_birthdate(day, month, year)
    except (ValueError, EOFError) as error:
        print(f"Ошибка ввода: {error}. Проверьте дату и повторите запуск.")
        return

    print(f"Дата рождения: {birthday:%d.%m.%Y}")
    print(f"День недели: {weekday_name(birthday)}")
    print(f"Високосный год: {'да' if is_leap_year(birthday.year) else 'нет'}")
    print(f"Возраст полных лет: {calculate_age(birthday)}")
    print("Дата рождения на звёздочном табло:")
    print(render_stars(birthday.strftime("%d %m %Y")))


if __name__ == "__main__":
    main()
