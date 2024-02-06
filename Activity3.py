import csv

class Person:
    def __init__(self, id, first_name, middle_name, last_name, birthday, gender, address):
        self.id = id
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.birthday = birthday
        self.gender = gender
        self.address = address
    

def load_csv(file_path):
    persons = []
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row in reader:
            id, first_name, middle_name, last_name, birthday, gender, address = row
            person = Person(id, first_name, middle_name, last_name, birthday, gender, address)
            persons.append(person)
    return persons

person_list = load_csv("persons.csv")

def search(persons, searchTerm):
    results = []
    for person in persons:
        if searchTerm.lower() in person.first_name.lower() or \
            searchTerm.lower() in person.middle_name.lower() or \
            searchTerm.lower() in person.last_name.lower():
            results.append(person)
    return results

if __name__ == "__main__":
    file_path = "persons.csv"
    person_list = load_csv(file_path)
    
    search_name = input("Enter the name of the person you want to search: ")
    search_results = search(person_list, search_name)
    
    if search_results:
        print("\nSearch Results:")
        for person in search_results:
            print(f"{person.first_name} {person.middle_name} {person.last_name} ({person.gender})")
    else:
        print("No matching persons found.")