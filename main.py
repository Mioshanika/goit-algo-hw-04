from pathlib import Path
from pprint import pp
from task1.salary import total_salary
from task2.cat_info import get_cats_info
from task3.folder_tree import print_folder_tree

def main():
    current_dir = Path(__file__).parent
    print('='*42)

    # Task #1: calculating total, avarage from salaries file.
    salaries_file = current_dir/'task1'/'salaries.txt'
    total, average = total_salary(str(salaries_file))
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    print('-'*42)

    # Task #2: parse cat information from the file
    cats_file = current_dir/'task2'/'cats.txt'
    cats_info = get_cats_info(str(cats_file))
    pp(cats_info)
    print('-'*42)
    
    # Task #3: Colored printing of a given directory structure.
    test_dir = current_dir/'test-dir'
    print_folder_tree(str(test_dir))
    print('='*42)

if __name__ == '__main__':
    main()