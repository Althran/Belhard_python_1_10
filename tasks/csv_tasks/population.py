"""
Написать функцию max_delta, в которой будет происходить чтение csv
файла world_population.csv и функцию должна возвращать год, в котором
наибольший процент прироста населения.
"""
from pathlib import Path
import csv


def max_delta(find_population):
    max_count = 0
    with open(find_population, 'r') as f_p:
        reader = csv.reader(f_p)
        count = 0
        find_year = 0
        for row in reader:
            if count == 0:
                pass
            else:
                number = float(row[2])
                if number > max_count:
                    max_count = number
                    find_year = int(row[0])
            count += 1

        print(str(find_year))


max_delta(Path('world_populations1.csv'))
