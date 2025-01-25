def total_salary(path):
    total = 0
    count = 0
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                try:
                    parts = line.strip().split(",")
                    salary = int(parts[1])  
                    total += salary  
                    count += 1  
                except ValueError:
                    print(f"Помилка при обробці рядка: {line.strip()} (не вдалося перетворити зарплату)")
        if count == 0:
            return 0, 0  
        average = total / count  
        return total, average  
    except FileNotFoundError:
        print(f"Файл {path} не знайдено.")
        return 0, 0
    except Exception as e:
        print(f"Сталася помилка під час роботи з файлом: {e}")
        return 0, 0
path = "salary_file.txt"
total, average = total_salary(path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")