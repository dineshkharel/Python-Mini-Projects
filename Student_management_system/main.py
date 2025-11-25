import functions,msvcrt
class StudentManagementSystem:
    def main(self):
        print("Welcome to the SStudent Management System")
        inside = True
        while inside:
            print("1. Add student")
            print("2. Delete student")
            print("3. View student")
            print("4. Update student")
            print("5. Exit")
            choice = int(input("Enter your choice(1-5): "))

            if  choice ==1:
                functions.add_student()

            elif choice ==2:
                functions.delete_student()

            elif choice ==3:
                functions.view_student()

            elif choice ==4:
                functions.update_student()
        
            else:
                print("Invalid input! ")


sms = StudentManagementSystem()
if __name__=="__main__": #only runs in this file

    sms.main()

msvcrt.getch()