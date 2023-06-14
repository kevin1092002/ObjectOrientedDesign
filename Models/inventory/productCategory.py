import csv


class ProductCategory:
    def __init__(self, category_id, name, description):
        self.category_id = category_id
        self.name = name
        self.description = description

    def save(self, filename='Database/category.csv'):
        with open(filename, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.category_id, self.name,
                             self.description])
