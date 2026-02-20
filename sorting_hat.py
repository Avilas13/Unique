# Write code below 💖

Gryffindor = 0  
Ravenclaw = 0  
Hufflepuff = 0  
Slytherin = 0
print("Q1) Do you like Dawn or Dusk?")
print("1) Dawn")  
print("2) Dusk")
Q1=int(input())     
if Q1==1:
  Gryffindor+= 1
  Ravenclaw+=1
  print("Gryffindor and Ravenclaw both get a +1.")
elif Q1==2:
  Hufflepuff+=1
  Slytherin+=1
  print("Hufflepuff and Slytherin both get a +1.")  
else:
  print("Wrong Output")  
print("Q2: When I’m dead, I want people to remember me as:")
print("1) The Good")  
print("2) The Great")   
print(" 3) The Wise")  
print("4) The Bold")  
Q2=int(input())    
if Q2==1:
  Hufflepuff+= 2
  print("Hufflepuff +2")
elif Q2==2:
  Slytherin+=2
  print("Slytherin +2")
elif Q2==3:
 Ravenclaw+=2
 print("Ravenclaw +2")
elif Q2==4:
 Gryffindor+=2
 print("Gryffindor +2.")   
else:
  print("Wrong Output")      
print("Q3: Which kind of instrument most pleases your ear?")
print("1) The violin")  
print(" 2) The trumpet")   
print(" 3) The piano")  
print("4) The drum")
Q3=int(input() )   
if Q3==1:
  Hufflepuff+=4
  print("Hufflepuff +4")
elif Q3==2:
  Slytherin+=4
  print("Slytherin +4")
elif Q3==3:
 Ravenclaw+=4
 print("Ravenclaw +4")
elif Q3==4:
 Gryffindor+=4
 print("Gryffindor +4.")   
else:
 print("Wrong Output")

print(Hufflepuff)
print(Slytherin) 
print(Ravenclaw) 
print(Gryffindor)           