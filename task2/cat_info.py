def get_cats_info(path: str) -> list[dict]:
    cats_info = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            cats_file_lines = file.readlines()
    except FileNotFoundError:
        return []
    for cat_info in cats_file_lines:
        id, name, age = cat_info.strip().split(',')
        cats_info.append({'id': id,'name': name,'age': age})
    return cats_info