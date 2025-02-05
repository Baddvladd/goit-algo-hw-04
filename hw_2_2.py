def get_cats_info(path):
    cats = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()  
                if line:  
                    parts = line.split(',')  
                    if len(parts) == 3:  
                        cat_id, name, age = parts
                        cats.append({
                            "id": cat_id,
                            "name": name,
                            "age": age
                        })
    except FileNotFoundError:
        print(f"Файл за шляхом '{path}' не знайдено.")
    except Exception as e:
        print(f"Виникла помилка: {e}")
    return cats

file_path = "cats_file.txt"

data = """60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5
"""

with open(file_path, "w", encoding="utf-8") as file:
    file.write(data)

cats_info = get_cats_info(file_path)
print(cats_info)
