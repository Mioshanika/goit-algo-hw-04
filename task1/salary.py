def total_salary(path: str) -> tuple[int, int]:
    salary_info = []
    salary_sum = 0
    salary_avarage = 0 
    try:
        with open(path, "r", encoding="utf-8") as file:
            salary_info = file.readlines()
    except FileNotFoundError:
        return (0, 0)
    for salary in salary_info:
        _, num = salary.split(',')
        salary_sum += int(num)
    salary_avarage = salary_sum // len(salary_info)
    return (salary_sum, salary_avarage)