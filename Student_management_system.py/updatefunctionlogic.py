filename ="studentdata.json"
import json
def update_studentdata(option,email):
    try:
        with open(filename,"r") as r:
            data = json.load(r)
            for  i in range (len(data)):
                if data[i]['email']==email:
                    if option == 1:
                        u_name= input("Updated Name: ")
                        data[i]['name']=u_name
                    elif option == 2:
                        u_age= int(input("Update Age: "))
                        data[i]['age']=u_age
                    elif option == 3:
                        u_email= input("Updated Email: ")
                        data[i]['email']=u_email
                    else:
                        print("Invalid input!")
        
        with open(filename,"w") as w:
            json.dump(data,w)
        print("Update done!")
    except Exception:
        print(Exception)
