#Terminal based program for client information database

#Create an empty dictionary to store client information
client_info = {}


#Function to add client information
def add_client():
    while True:
        name = input("Enter client's name: ").lower()
        age = input("enter client's age: ")
        address = input("Enter client's address: ")
        phone = input("Enter client's phone number: ")

        try:
            age = int(age)
            phone = int(phone)
            break
        except ValueError:
            print("Invalid input! Age and phone number must be numbers. Please try again.\n")

#Save client information to file
    with open("clients.txt", "a") as file:
        file.write(name + "," + str(age) + "," + address + "," + str(phone) + "\n")
        print("client's information added successfully!")
  
#Function to display client information
def display_client():
  with open("clients.txt", "r") as file:
    clients = file.readlines()
    if not clients:
      print("No clients found!")
      return
    name = input("Enter client's name to display information (or press enter to display all clients): ").lower()
    if not name:
     for clients in clients:
       name, age, address, phone = line.strip().split(",")
       print("Client's name:", name)
       print("Client's age:", age)
       print("Client's address:", address)
       print("Client's phone:", phone)
    else:
      found = False
      for client in clients:
        client_info = client.strip().split(",")
        if name ==client_info[0].lower():
           print("Client's name:", client_info[0]) 
           print("Client's age:",client_info[1])
           print("Client's address:", client_info[2])
           print("Client's phone:", client_info[3])
           found = True
           break
      if not found:
        print("Client information not found!")
          
#If file does not exist, create it
  open("clients.txt", "a").close()

def remove_client():
    name = input("Enter client's name to remove: ").lower()
    with open("clients.txt", "r") as file:
        clients = file.readlines()
    with open("clients.txt", "w") as file:
        removed = False 
        for client in clients:
            client_info = client.strip().split(",")
            if name == client_info[0].lower():
                removed = True
            else:
                file.write(client)
        if removed:
            print("Client's information removed successfully!")
         
        else:
            print("Client information not found!") 

        #if name in client_info:
         #   del client_info[name]
    

#Main program.
while True: 
  print("\nMenu.")
  print("1. Add client's information.")
  print("2. Display client's information.")
  print("3. Remove client's information.")
  print("4. Quit.")
  choice = int(input("Enter your choice: "))
  if choice == 1:
    add_client()
  elif choice == 2:
    display_client()
  elif choice == 3:
    remove_client()
  elif choice == 4:
    break
  else:
    print("Invalid choice! Please try again. ")
        
  