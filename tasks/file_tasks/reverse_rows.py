"""
Написать функцию revert_rows, которая принимает путь к файлу и делает новый
файл. Создать новый файл, каждая строка которого получается из соответствующей
строки исходного файла перестановкой слов в обратном порядке.
"""
from pathlib import Path


def revert_rows(file_text, new_text):
    with open(file_text, 'r+') as f, open(new_text, 'w') as f_new:
        for i in f:
            f_new.writelines(right_rows(i) + '\n')


def right_rows(line):
    line = line.split()
    new_dict = {}
    for idx, i in enumerate(line):
        if i[-1] in ',.':
            new_dict[idx] = i[-1]
        line[idx] = i.strip(',.')
    line.reverse()
    for k, v in new_dict.items():
        line[k] += v
    line = ' '.join(line)
    return '. '.join(map(lambda s: s.strip().capitalize(), line.split('.')))


revert_rows(Path('text.txt'), Path('text1.txt'))

