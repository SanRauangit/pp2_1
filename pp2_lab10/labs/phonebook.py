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

    def insert_from_console(self):
        first_name = input("Enter first name: ")
        phone = input("Enter phone: ")
        
        with self.conn.cursor() as cur:
            cur.execute("""
                INSERT INTO phonebook (first_name, phone)
                VALUES (%s, %s)
                ON CONFLICT (phone) DO UPDATE SET
                    first_name = EXCLUDED.first_name
            """, (first_name, phone))
            self.conn.commit()

    def update_contact(self):
        phone = input("Enter phone of contact to update: ")
        new_first_name = input("Enter new first name: ")
        
        with self.conn.cursor() as cur:
            cur.execute("""
                UPDATE phonebook 
                SET first_name = %s 
                WHERE phone = %s
            """, (new_first_name, phone))
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
            
            results = cur.fetchall()
            for row in results:
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
        print("\n1. Insert from CSV\n2. Insert from console\n3. Update\n4. Query\n5. Delete\n6. Exit")
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
            phonebook.delete_contact()
        elif choice == '6':
            break
    
    phonebook.close()

if __name__ == "__main__":
    main()