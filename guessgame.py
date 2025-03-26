import random
a=random.randint(1,10)
print("ONLY 3 CHANCES")
for x in range(0,3):
  x=int(input("ENTER THE NUMBER : "))
  if x<a:
      print("IT IS A LOWER NUMBER")
  elif x>a:
       print("IT IS A HIGHER NUMBER")
  else:
        print("RIGHT GUESS")
        break
else:
    print(f" CHANCES OVER,THE NUMBER IS {a} ")




