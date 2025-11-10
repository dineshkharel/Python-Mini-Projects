import csv
class Students:

    def __init__(self,sid,sname,saddress,scontact,gender):
        self.id=sid
        self.name=sname
        self.address=saddress
        self.contact=scontact
        self.gender=gender

class StudentManagementSystem:
  

     def main(self):
         inside = True
         while inside:
            print("----Welcome to Student Management System----")
            print("""1.Add Students Records 
2.View Records
3.Delete Reccords
4.Update Records
5.Exit""")
       
            option= input("Enter Your option (1-5): ")

            if(option =="1"):
                  self.add_Student()

            elif (option == "2"):
                  self.view_records()

            elif (option == "3"):
                  self.delete_record()

            elif (option == "4"):
                  self.update_records()
            else:
                  inside = False
          
           

    

     def add_Student(self):
        id=int(input("Enter ID: "))
        name=input("Enter Name: ")
        address= input("Enter Address: ")
        contact=input("Enter Contact: ")
        gender=input("Enter Gender: ")
        stu=Students(id,name,address,contact,gender)
        with open("Students.csv","r") as r:
             reader= csv.reader(r)
             rows=list(reader)
             duplicate= False
             for i in rows[1:]:
                  
                  if len(i)<2:
                       continue
                  if id ==int(i[0]) or name == i[1]:
                       duplicate= True
                       break
             if duplicate:
                  print("Data is already present")
             else:
                with open("Students.csv","a",newline="") as f:
                 writer=csv.writer(f)
            # writer.writerow(["ID","Name","Address","Contact","Gender"])
                 writer.writerow([id,name,address,contact,gender])
                 print("Student added Success fully!")
    
     def view_records(self):
        with open("Students.csv","r") as f:
            reader= csv.reader(f)
            for row in reader:
                if row ==[]:
                    continue
                print(row)

     def delete_record(self):
        self.view_records()
        delete_id= int(input("Enter the id you want to delete: "))
        with open("Students.csv","r") as f:
            reader=csv.reader(f)
            rows= list(reader)
            found =False
            for i in rows[1:]:
                if i==[]:
                    continue

                if int(i[0])==delete_id:
                    # print("Record Found!")
                    found=True
                    rows.remove(i)
                    print("Record Deleted!")
                    # print(rows)
                    # after=rows.copy()
                    # print(i)
                    break

        if found==True:
                        
                     with open("Students.csv","w",newline="") as w:
                        writer= csv.writer(w)
                        writer.writerows(rows)

     def update_records(self):
         self.view_records()
         update_id= int(input("Enter the ID of the record you want to update: "))
         with open("Students.csv","r") as r:
             reader= csv.reader(r)
             rows= list(reader)
             for i in rows[1:]:
                 if i ==[]:
                    continue
                 

                 if int(i[0])==update_id:
                     print("1.Name,2.Address, 3.Contact,4.Gender")
                     ch = input("Enter what do you want to update:")
                     if ch=="1":
                        #  print("Enter the Name:")
                         i[1]=input("Enter Name: ")
                        #  print(rows)
                     elif ch =="2":
                         i[2]=input("Enter Address:")
                     elif ch =="3":
                         i[3]= input("Enter Contact:")
                     else:
                         i[4]= input("Enter Gender: ")
                    
                    
         with open("Students.csv","w",newline="") as f:
                             writer = csv.writer(f)
                             writer.writerows(rows)
                 
    



           





    


sms =StudentManagementSystem()
sms.main()
# sms.add_Student()
# sms.add_Student()
# sms.view_records()
# sms.delete_record()
# sms.view_records()
# sms.update_records()
