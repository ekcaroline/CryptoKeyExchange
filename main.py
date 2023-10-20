import datetime
import json 
import pytz
import secrets

def is_a_primitive(a,q): #checks for primitive root
  lst = []
  i = 1
  
  while i < q:
    result = (a**i) % q
    lst.append(result)
    i += 1
  
  lst.sort()
  print(lst)
  
  if len(set(lst)) == q-1:
      print('\nA is a primitive root of q. \n')
  else:
      print('\nA is not a primitive root of q. \n')

def compute_public_key(a,q,Xa,Xb): #compute public key/session key
  Ya = 0
  Yb = 0
  shared_keya = 0
  shared_keyb = 0

  #compute public key
  Ya = (a**Xa) % q
  Yb = (a**Xb) % q

  #timestamps
  pacific = pytz.timezone('US/Pacific')
  timestamp = datetime.datetime.now(pacific).strftime("%m-%d-%Y %I:%M:%S %p %Z")

  print(f"{timestamp} - Message from Alice (Ya): {Ya}")
  print(f"{timestamp} - Message from Bob (Yb): {Yb}\n")

  #compute session key
  shared_keya = (Yb**Xa) % q
  shared_keyb = (Ya**Xb) % q

  print("-----------------------Session Key in progress...-------------------------")

  if shared_keya == shared_keyb:
    print("Shared session key is: ", shared_keya)
    print("The shared session key is the same for both Alice and Bob.")
  else:
    print("Shared session key is: ", shared_keya)
    print("The shared session key is different for both Alice and Bob.")
  

def main(): 
  print("\nThis program will compute primitive root and public key/shared session key. Security measures have also been implemented\n ")
  print("--------------------------             Menu             ---------------------------------\n")
  
  while True:
    print("1. Only Primitive Root")
    print("2. Both Primitive Root and Compute Public Key/Session Key")
    print("3. Quit")
    
    choice = int(input("\nWhat would you like to do? \n"))

    if choice < 1 or choice > 2:
      return print("Invalid choice. Try again.")
           
    if choice == 1: #primitive root
      a = int(input("Enter a value of a: "))
      q = int(input("Enter a value for q: "))

      is_a_primitive(a,q)
      
    elif choice == 2: #compute primitive root and public key/session key
      a = int(input("Enter a value of a: "))
      q = int(input("Enter a value for q: "))
      Xa = int(input("\nLet Person #1 choose a private key: "))
      Xb = int(input("Let Person #2 choose a private key: "))

      if (Xa > q and Xb > q): #checks if 
        print("Invalid private key. (Xa or Xb greater than q)")
        return 
      compute_public_key(a,q,Xa,Xb)
        
    elif choice == 3:
      print("Goodbye!")
      break
