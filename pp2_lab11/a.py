import psycopg2
import csv

class PhoneBook:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname="phonebook",
            user="postgres",
            password="1204",
            host="localhost",
            port="5432"
        )

    def search_by_pattern(self):
        pattern = input("Enter search pattern: ")
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook WHERE first_name ILIKE %s OR phone ILIKE %s", 
                       (f'%{pattern}%', f'%{pattern}%'))
            for row in cur.fetchall():
                print(row)

    def insert_from_console(self):
        first_name = input("Enter first name: ")
        phone = input("Enter phone: ")
        
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO phonebook (first_name, phone)
                VALUES (%s, %s)
                ON CONFLICT (first_name) DO UPDATE SET
                    phone = EXCLUDED.phone
            """, (first_name, phone))
            self.conn.commit()

    def insert_many_users(self):
        print("Enter users (name,phone). Type 'done' when finished:")
        users = []
        while True:
            entry = input("> ")
            if entry.lower() == 'done':
                break
            users.append(entry)
        
        invalid_entries = []
        with self.conn.cursor() as cur:
            for entry in users:
                if ',' in entry:
                    name, phone = entry.split(',', 1)
                    name = name.strip()
                    phone = phone.strip()
                    clean_phone = phone.replace(' ', '').replace('+', '')
                
                    if len(clean_phone) >= 10 and clean_phone.isdigit():
                        cur.execute("""
                            INSERT INTO phonebook (first_name, phone)
                            VALUES (%s, %s)
                            ON CONFLICT (first_name) DO UPDATE SET phone = EXCLUDED.phone
                        """, (name, phone))
                    else:
                        invalid_entries.append(entry)
            
            self.conn.commit()
        
        if invalid_entries:
            print(f"Invalid entries: {invalid_entries}")


    def get_paginated(self):
        limit = int(input("Enter limit: "))
        offset = int(input("Enter offset: "))
        with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM phonebook ORDER BY id LIMIT %s OFFSET %s", (limit, offset))
            for row in cur.fetchall():
                print(row)

    def insert_from_csv(self, csv_file_path):
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            with self.conn.cursor() as cur:
                for row in reader:
                    cur.execute("""
                        INSERT INTO phonebook (first_name, phone)
                        VALUES (%s, %s)
                        ON CONFLICT (phone) DO UPDATE SET
                            first_name = EXCLUDED.first_name
                    """, (row['first_name'], row['phone']))
                self.conn.commit()

    def update_contact(self):
        phone = input("Enter phone of contact to update: ")
        new_first_name = input("Enter new first name: ")
        with self.conn.cursor() as cur:
            cur.execute("UPDATE phonebook SET first_name = %s WHERE phone = %s", (new_first_name, phone))
            self.conn.commit()

    def query_contacts(self):
        print("Search by: 1. Name, 2. Phone")
        choice = input("Choice: ")
        with self.conn.cursor() as cur:
            if choice == '1':
                name = input("Enter name: ")
                cur.execute("SELECT * FROM phonebook WHERE first_name = %s", (name,))
            elif choice == '2':
                phone = input("Enter phone: ")
                cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))
            for row in cur.fetchall():
                print(row)

    def delete_contact(self):
        print("Delete by: 1. Username, 2. Phone")
        choice = input("Choice: ")
        with self.conn.cursor() as cur:
            if choice == '1':
                name = input("Enter username: ")
                cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
            elif choice == '2':
                phone = input("Enter phone: ")
                cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
            self.conn.commit()

    def close(self):
        self.conn.close()

def main():
    phonebook = PhoneBook()
    
    while True:
        print("\n1. Insert from CSV\n2. Insert from console\n3. Update\n4. Query\n5. Search by pattern\n6. Insert many users\n7. Paginated view\n8. Delete\n9. Exit")
        choice = input("Choice: ")
        
        if choice == '1':
            csv_file = input("CSV file path: ")
            phonebook.insert_from_csv(csv_file)
        elif choice == '2':
            phonebook.insert_from_console()
        elif choice == '3':
            phonebook.update_contact()
        elif choice == '4':
            phonebook.query_contacts()
        elif choice == '5':
            phonebook.search_by_pattern()
        elif choice == '6':
            phonebook.insert_many_users()
        elif choice == '7':
            phonebook.get_paginated()
        elif choice == '8':
            phonebook.delete_contact()
        elif choice == '9':
            break
    
    phonebook.close()

if __name__ == "__main__":
    main()