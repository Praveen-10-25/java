import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="5028",
    database="employeeDb"
)

cursor = con.cursor()

def main():
    name_input = input("Enter your name: ")
    print("Welcome", name_input)

    while True:
        print("\n--- Main Menu ---")
        print("1. View all employee records")
        print("2. Insert new employee")
        print("3. Update employee")
        print("4. Delete employee")
        print("5. Exit")
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            cursor.execute("SELECT * FROM my_table;")
            rows = cursor.fetchall()
            print("\nEmployee Records:")
            for row in rows:
                print(row)

        elif choice == "2":
            name = input("Enter employee name: ")
            mail_id = input("Enter mail ID: ")
            ph_number = input("Enter phone number: ")

            insert_query = "INSERT INTO my_table (name, mail_id, ph_number) VALUES (%s, %s, %s)"
            values = (name, mail_id, ph_number)

            cursor.execute(insert_query, values)
            con.commit()

            print("Record inserted successfully!")

            view = input("Do you want to view the inserted record? (yes/no): ")
            if view.lower() == "yes":
                cursor.execute("SELECT * FROM my_table WHERE mail_id = %s", (mail_id,))
                record = cursor.fetchone()
                if record:
                    print("\nInserted Record:", record)
                else:
                    print("No record found.")

        elif choice == "3":
            data = input("Enter the employee's mail ID to update: ")
            cursor.execute("SELECT * FROM my_table WHERE mail_id = %s", (data,))
            record = cursor.fetchone()

            if record:
                print("Record found:", record)
                print("1. Update Name")
                print("2. Update Phone Number")
                print("3. Update Mail ID")
                update_choice = input("Choose what to update (1/2/3): ")

                if update_choice == "1":
                    new_name = input("Enter the new name: ")
                    cursor.execute("UPDATE my_table SET name = %s WHERE mail_id = %s", (new_name, data))
                    con.commit()
                    print("Name updated successfully.")

                elif update_choice == "2":
                    new_phone = input("Enter the new phone number: ")
                    cursor.execute("UPDATE my_table SET ph_number = %s WHERE mail_id = %s", (new_phone, data))
                    con.commit()
                    print("Phone number updated successfully.")

                elif update_choice == "3":
                    new_mail = input("Enter the new mail ID: ")
                    cursor.execute("UPDATE my_table SET mail_id = %s WHERE mail_id = %s", (new_mail, data))
                    con.commit()
                    print("Mail ID updated successfully.")
                else:
                    print("Invalid update option.")
            else:
                print("No employee found with that mail ID.")

        elif choice == "4":
            delete = input("Enter the employee mail to delete: ")
            cursor.execute("SELECT * FROM my_table WHERE mail_id = %s", (delete,))
            record = cursor.fetchone()
            if record:
                print("Record found:", record)
                confirm = input("Press 1 to delete the employee details: ")
                if confirm == "1":
                    cursor.execute("DELETE FROM my_table WHERE mail_id = %s", (delete,))
                    con.commit()
                    print("Data successfully deleted.")
                else:
                    print("Operation cancelled.")
            else:
                print("No employee found with that mail ID.")

        elif choice == "5":
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")

    cursor.close()
    con.close()

main()
