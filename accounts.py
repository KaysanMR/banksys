
import random
import math
id_list = []

def generate_id():
  id = math.floor(random.random() * 1006)
  id_list.append(id) if id not in id_list else generate_id()
  return id
  
def create():
  while True:
    username = input("Enter your username:")
    password = input("Enter your password:")
    if input("Confirm password: ") ==  password:
      print("Account created")
      return [username, password]
    else:
      print("Passwords do not match.")
      break
  
def store(credentials):
  with open("accounts.txt", "a") as file:
    file.write(f"[{generate_id()}, {', '.join(credentials)}]" + '\n')
  
  
[store(create()) for i in range(3)]


