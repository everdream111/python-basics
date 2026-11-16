# Калькулятор вартості квитків у кінотеатр
# Програма приймає дані користувача, робить розрахунки та виводить чек.

# ---------- Константи (з анотаціями типів) ----------
BASE_PRICE: float = 150.0        # базова ціна квитка, грн
MAX_TICKETS: int = 10            # максимум квитків за одне замовлення
CHILD_AGE: int = 12              # до цього віку - дитячий квиток
SENIOR_AGE: int = 60             # від цього віку - пільговий квиток
STUDENT_MAX_AGE: int = 25        # максимальний вік для студентської знижки
GROUP_SIZE: int = 5              # від такої кількості квитків - груповий

print("=== Кінотеатр «Зірка»: калькулятор квитків ===")

# ---------- Введення даних (input) ----------
name: str = input("Введіть ваше ім'я: ").strip()

# Перетворення введених значень: str -> int / float
age: int = int(input("Введіть ваш вік: "))
tickets: int = int(input(f"Кількість квитків (1-{MAX_TICKETS}): "))
bonus_balance: float = float(input("Бонусний баланс, грн (0 якщо немає): "))

print("Тип сеансу: 1 - Звичайний, 2 - 3D, 3 - VIP")
session_choice: int = int(input("Ваш вибір: "))

student_answer: str = input("Чи є студентський квиток? (так/ні): ").lower()
is_student: bool = student_answer == "так"

# ---------- Перевірка коректності (порівняння та and / or / not) ----------
if age <= 0 or age > 120:
    print("Помилка: некоректний вік.")
elif not (1 <= tickets <= MAX_TICKETS):
    print(f"Помилка: кількість квитків має бути від 1 до {MAX_TICKETS}.")
elif bonus_balance < 0:
    print("Помилка: бонусний баланс не може бути від'ємним.")
else:
    # ---------- match-case: доплата за тип сеансу ----------
    match session_choice:
        case 1:
            session_name: str = "Звичайний"
            surcharge: float = 0.0
        case 2:
            session_name = "3D"
            surcharge = 40.0
        case 3:
            session_name = "VIP"
            surcharge = 120.0
        case _:
            session_name = "Звичайний (за замовчуванням)"
            surcharge = 0.0

    # Ціна одного квитка до знижок (математичні операції)
    ticket_price: float = BASE_PRICE + surcharge

    # ---------- Умовні конструкції if / elif / else ----------
    if age < CHILD_AGE:
        discount_percent: int = 50
        category: str = "Дитячий"
    elif age >= SENIOR_AGE:
        discount_percent = 30
        category = "Пільговий"
    elif is_student and age <= STUDENT_MAX_AGE:
        discount_percent = 20
        category = "Студентський"
    else:
        discount_percent = 0
        category = "Повний"

    # ---------- Вкладені умови: додаткова знижка за групу ----------
    if tickets >= GROUP_SIZE:
        if session_choice == 3:
            discount_percent += 5   # менша знижка на VIP
        else:
            discount_percent += 10

    # ---------- Умовний вираз (тернарний оператор) ----------
    order_type: str = "Груповий" if tickets >= GROUP_SIZE else "Індивідуальний"

    # ---------- Розрахунок підсумку ----------
    subtotal: float = ticket_price * tickets
    discount_sum: float = subtotal * discount_percent / 100
    total: float = subtotal - discount_sum

    # Використання бонусів (не більше половини суми)
    bonus_used: float = min(bonus_balance, total / 2)
    to_pay: float = total - bonus_used

    # ---------- Виведення результату (print + f-рядки) ----------
    print("\n" + "=" * 36)
    print(f"Клієнт: {name}, вік: {age}")
    print(f"Категорія: {category} | Замовлення: {order_type}")
    print(f"Сеанс: {session_name}")
    print(f"Ціна квитка: {ticket_price:.2f} грн x {tickets} = {subtotal:.2f} грн")
    print(f"Знижка: {discount_percent}% (-{discount_sum:.2f} грн)")
    print(f"Списано бонусів: {bonus_used:.2f} грн")
    print(f"До сплати: {to_pay:.2f} грн")
    print("=" * 36)
    print("Дякуємо за покупку, гарного перегляду!")
