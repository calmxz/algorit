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
    
    while True:
        search_term = input("Enter the name to search (or type 'exit' to quit): ")
        if search_term.lower() == 'exit':
            break

        results = search(person_list, search_term)
        if results:
            print("Search Results:")
            for person in results:
                print(f"\nID: {person.id}\nFirst name: {person.first_name}\nMiddle Name: {person.middle_name}\nLast Name: {person.last_name}\nBirthday: {person.birthday}\nGender: {person.gender}\nAddress: {person.address}")
        else:
            print("No matching results found.")