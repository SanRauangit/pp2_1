import psycopg2
import csv
import os

class PhoneBook:
    def __init__(self, dbname="phonebook", user="postgres", password="1204", host="localhost", port="5432"):
        try:
            self.conn = psycopg2.connect(
                dbname=dbname,
                user=user,
                password=password,
                host=host,
                port=port
            )
            print("Connected to PostgreSQL database successfully!")
        except Exception as e:
            print(f"Database connection failed: {e}")
            raise
    def insert_from_csv(self, csv_file_path):
        try:
            with open(csv_file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                inserted_count = 0
                updated_count = 0
                
                with self.conn.cursor() as cur:
                    for row in reader:
                        try:
                            cur.execute("""
                                INSERT INTO phonebook (first_name, last_name, phone, email)
                                VALUES (%s, %s, %s, %s)
                                ON CONFLICT (phone) DO UPDATE SET
                                    first_name = EXCLUDED.first_name,
                                    last_name = EXCLUDED.last_name,
                                    email = EXCLUDED.email
                            """, (
                                row['first_name'], 
                                row.get('last_name', ''), 
                                row['phone'], 
                                row.get('email', '')
                            ))
                            
                            if cur.rowcount == 1:
                                inserted_count += 1
                            else:
                                updated_count += 1
                                
                        except Exception as e:
                            print(f"Error inserting {row.get('first_name', 'unknown')}: {e}")
                            continue
                    
                    self.conn.commit()
                
                print(f"CSV import completed!")
                print(f"Inserted: {inserted_count}, Updated: {updated_count}")
                
        except FileNotFoundError:
            print(f"CSV file not found: {csv_file_path}")
        except Exception as e:
            print(f"Error reading CSV file: {e}")
            self.conn.rollback()

    def insert_from_console(self):
        print("\n" + "="*40)
        print("ADD NEW CONTACT")
        print("="*40)
        
        # Get user input
        first_name = input("Enter first name: ").strip()
        last_name = input("Enter last name (optional): ").strip()
        phone = input("Enter phone number: ").strip()
        email = input("Enter email (optional): ").strip()
        
        # Validation
        if not first_name:
            print("First name is required!")
            return
        if not phone:
            print("Phone number is required!")
            return
        
        try:
            with self.conn.cursor() as cur:
                cur.execute("""
                    INSERT INTO phonebook (first_name, last_name, phone, email)
                    VALUES (%s, %s, %s, %s)
                    ON CONFLICT (phone) DO UPDATE SET
                        first_name = EXCLUDED.first_name,
                        last_name = EXCLUDED.last_name,
                        email = EXCLUDED.email
                    RETURNING id, first_name, phone
                """, (first_name, last_name, phone, email))
                
                result = cur.fetchone()
                self.conn.commit()
                
                if result:
                    print(f"Contact saved successfully!")
                    print(f"ID: {result[0]}, Name: {result[1]}, Phone: {result[2]}")
                    
        except Exception as e:
            print(f"Error saving contact: {e}")
            self.conn.rollback()
    def update_contact(self):
        print("\n" + "="*40)
        print("UPDATE CONTACT")
        print("="*40)
        
        # Find contact by phone
        phone = input("Enter phone number of the contact to update: ").strip()
        
        if not phone:
            print("Phone number is required!")
            return
        
        try:
            with self.conn.cursor() as cur:
                # Check if contact exists
                cur.execute("""
                    SELECT id, first_name, last_name, phone, email 
                    FROM phonebook WHERE phone = %s
                """, (phone,))
                contact = cur.fetchone()
                
                if not contact:
                    print("Contact not found!")
                    return
                
                print(f"\nCurrent contact details:")
                print(f"ID: {contact[0]}")
                print(f"Name: {contact[1]} {contact[2]}")
                print(f"Phone: {contact[3]}")
                print(f"Email: {contact[4]}")
                
                # Update options
                print("\nWhat would you like to update?")
                print("1. First Name")
                print("2. Last Name") 
                print("3. Phone Number")
                print("4. Email")
                print("5. Cancel")
                
                choice = input("\nEnter your choice (1-5): ").strip()
                
                if choice == '1':
                    new_first_name = input("Enter new first name: ").strip()
                    if new_first_name:
                        cur.execute("UPDATE phonebook SET first_name = %s WHERE phone = %s", 
                                   (new_first_name, phone))
                        print("First name updated successfully!")
                
                elif choice == '2':
                    new_last_name = input("Enter new last name: ").strip()
                    cur.execute("UPDATE phonebook SET last_name = %s WHERE phone = %s", 
                               (new_last_name, phone))
                    print("Last name updated successfully!")
                
                elif choice == '3':
                    new_phone = input("Enter new phone number: ").strip()
                    if new_phone:
                        cur.execute("UPDATE phonebook SET phone = %s WHERE phone = %s", 
                                   (new_phone, phone))
                        print("Phone number updated successfully!")
                
                elif choice == '4':
                    new_email = input("Enter new email: ").strip()
                    cur.execute("UPDATE phonebook SET email = %s WHERE phone = %s", 
                               (new_email, phone))
                    print("Email updated successfully!")
                
                elif choice == '5':
                    print("Update cancelled.")
                    return
                
                else:
                    print("Invalid choice!")
                    return
                
                self.conn.commit()
                
        except Exception as e:
            print(f"Error updating contact: {e}")
            self.conn.rollback()
    def query_contacts(self):
        print("\n" + "="*40)
        print("SEARCH CONTACTS")
        print("="*40)
        print("1. Show all contacts")
        print("2. Search by first name")
        print("3. Search by last name") 
        print("4. Search by phone number")
        print("5. Search by email")
        print("6. Search by name pattern")
        print("7. Back to main menu")
        
        choice = input("\nEnter your choice (1-7): ").strip()
        
        try:
            with self.conn.cursor() as cur:
                if choice == '1':
                    # Show all contacts
                    cur.execute("""
                        SELECT id, first_name, last_name, phone, email, created_at 
                        FROM phonebook 
                        ORDER BY first_name, last_name
                    """)
                    contacts = cur.fetchall()
                    self._display_contacts(contacts)
                
                elif choice == '2':
                    # Search by first name
                    first_name = input("Enter first name to search: ").strip()
                    cur.execute("""
                        SELECT id, first_name, last_name, phone, email, created_at 
                        FROM phonebook 
                        WHERE first_name ILIKE %s 
                        ORDER BY first_name, last_name
                    """, (f"%{first_name}%",))
                    contacts = cur.fetchall()
                    self._display_contacts(contacts)
                
                elif choice == '3':
                    # Search by last name
                    last_name = input("Enter last name to search: ").strip()
                    cur.execute("""
                        SELECT id, first_name, last_name, phone, email, created_at 
                        FROM phonebook 
                        WHERE last_name ILIKE %s 
                        ORDER BY first_name, last_name
                    """, (f"%{last_name}%",))
                    contacts = cur.fetchall()
                    self._display_contacts(contacts)
                
                elif choice == '4':
                    # Search by phone
                    phone = input("Enter phone number to search: ").strip()
                    cur.execute("""
                        SELECT id, first_name, last_name, phone, email, created_at 
                        FROM phonebook 
                        WHERE phone ILIKE %s 
                        ORDER BY first_name, last_name
                    """, (f"%{phone}%",))
                    contacts = cur.fetchall()
                    self._display_contacts(contacts)
                
                elif choice == '5':
                    # Search by email
                    email = input("Enter email to search: ").strip()
                    cur.execute("""
                        SELECT id, first_name, last_name, phone, email, created_at 
                        FROM phonebook 
                        WHERE email ILIKE %s 
                        ORDER BY first_name, last_name
                    """, (f"%{email}%",))
                    contacts = cur.fetchall()
                    self._display_contacts(contacts)
                
                elif choice == '6':
                    # Search by name pattern
                    pattern = input("Enter name pattern to search: ").strip()
                    cur.execute("""
                        SELECT id, first_name, last_name, phone, email, created_at 
                        FROM phonebook 
                        WHERE first_name ILIKE %s OR last_name ILIKE %s 
                        ORDER BY first_name, last_name
                    """, (f"%{pattern}%", f"%{pattern}%"))
                    contacts = cur.fetchall()
                    self._display_contacts(contacts)
                
                elif choice == '7':
                    return
                
                else:
                    print("Invalid choice!")
                    
        except Exception as e:
            print(f"Error searching contacts: {e}")

    def _display_contacts(self, contacts):
        if not contacts:
            print("No contacts found!")
            return
        
        print(f"\n{'ID':<4} {'First Name':<15} {'Last Name':<15} {'Phone':<15} {'Email':<20}")
        print("-" * 75)
        for contact in contacts:
            contact_id, first_name, last_name, phone, email, created_at = contact
            print(f"{contact_id:<4} {first_name:<15} {last_name:<15} {phone:<15} {email:<20}")
        print(f"\nTotal contacts found: {len(contacts)}")
    def delete_contact(self):
        print("\n" + "="*40)
        print("DELETE CONTACT")
        print("="*40)
        print("1. Delete by phone number")
        print("2. Delete by first name")
        print("3. Delete by last name")
        print("4. Cancel")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        try:
            with self.conn.cursor() as cur:
                if choice == '1':
                    # Delete by phone
                    phone = input("Enter phone number to delete: ").strip()
                    if not phone:
                        print("Phone number is required!")
                        return
                    
                    cur.execute("SELECT first_name, last_name FROM phonebook WHERE phone = %s", (phone,))
                    contact = cur.fetchone()
                    
                    if contact:
                        confirm = input(f"Delete {contact[0]} {contact[1]} (phone: {phone})? (y/n): ").strip().lower()
                        if confirm == 'y':
                            cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
                            self.conn.commit()
                            print("Contact deleted successfully!")
                        else:
                            print("Deletion cancelled.")
                    else:
                        print("Contact not found!")
                
                elif choice == '2':
                    # Delete by first name
                    first_name = input("Enter first name to delete: ").strip()
                    if not first_name:
                        print("First name is required!")
                        return
                    
                    cur.execute("SELECT COUNT(*) FROM phonebook WHERE first_name ILIKE %s", (first_name,))
                    count = cur.fetchone()[0]
                    
                    if count > 0:
                        confirm = input(f"Delete {count} contact(s) with first name '{first_name}'? (y/n): ").strip().lower()
                        if confirm == 'y':
                            cur.execute("DELETE FROM phonebook WHERE first_name ILIKE %s", (first_name,))
                            self.conn.commit()
                            print(f"{cur.rowcount} contact(s) deleted successfully!")
                        else:
                            print("Deletion cancelled.")
                    else:
                        print("No contacts found with that first name!")
                
                elif choice == '3':
                    # Delete by last name
                    last_name = input("Enter last name to delete: ").strip()
                    if not last_name:
                        print("Last name is required!")
                        return
                    
                    cur.execute("SELECT COUNT(*) FROM phonebook WHERE last_name ILIKE %s", (last_name,))
                    count = cur.fetchone()[0]
                    
                    if count > 0:
                        confirm = input(f"Delete {count} contact(s) with last name '{last_name}'? (y/n): ").strip().lower()
                        if confirm == 'y':
                            cur.execute("DELETE FROM phonebook WHERE last_name ILIKE %s", (last_name,))
                            self.conn.commit()
                            print(f"{cur.rowcount} contact(s) deleted successfully!")
                        else:
                            print("Deletion cancelled.")
                    else:
                        print("No contacts found with that last name!")
                
                elif choice == '4':
                    return
                
                else:
                    print("Invalid choice!")
                    
        except Exception as e:
            print(f"Error deleting contact: {e}")
            self.conn.rollback()

    def close(self):
        """Close database connection"""
        self.conn.close()
        print("Database connection closed.")

# def create_sample_csv():
#     """Create sample CSV file for testing"""
#     sample_data = [
#         ["first_name", "last_name", "phone", "email"],
#         ["John", "Doe", "+1234567890", "john.doe@email.com"],
#         ["Jane", "Smith", "+0987654321", "jane.smith@email.com"],
#         ["Bob", "Johnson", "+1122334455", "bob.johnson@email.com"],
#         ["Alice", "Brown", "+5566778899", "alice.brown@email.com"],
#         ["Charlie", "Wilson", "+9988776655", "charlie.wilson@email.com"]
#     ]
    
#     with open('contacts.csv', 'w', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerows(sample_data)
#     print("Sample CSV file 'contacts.csv' created!")

def main():
    POSTGRES_PASSWORD = "1204"
    
    try:
        phonebook = PhoneBook(password=POSTGRES_PASSWORD)
    except Exception as e:
        print("Failed to start PhoneBook application.")
        return
    
    # # Create sample CSV file
    # create_sample_csv()
    
    while True:
        print("\n" + "="*50)
        print("           PHONEBOOK MANAGEMENT SYSTEM")
        print("="*50)
        print("1. Upload data from CSV file")
        print("2. Add contact from console")
        print("3. Update contact")
        print("4. Search contacts")
        print("5. Delete contact")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            csv_file = input("Enter CSV file path (or press Enter for contacts.csv): ").strip()
            if not csv_file:
                csv_file = "contacts.csv"
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
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Please try again.")
    
    phonebook.close()

if __name__ == "__main__":
    main()