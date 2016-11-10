import csv
import os


def import_data():
    path = os.path.abspath('controller/scripts/test.csv')
    with open(path) as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='\n')
        result = []

        for row in reader:
            result.append(
                {
                    'email_verified': True,
                    'permission': 'student',
                    'password': 'password',
                    'first_name': row[1],
                    'last_name': row[0],
                    'email': row[4],
                    'group': row[5]
                }
            )

        return result