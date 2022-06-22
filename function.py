#ground shipping.  flat charge of $20
# weight of package      price per pound
# 2 lbs or less          $1.50
# over 2 lb but less than or equal to 6 lb $3
# over 6 less that or equal to 10 $4      
# over 10 lbs $4.75 

#ground shipping premium. no price per pound only a flat charge of 125

#drone shipping
# 2lb or less = 4.5 per pound
# over 2 lb but less than or equal to 6 lb 9
# over 6lb but less than or equal to 10lb 12
# over 10 lb 14.25

from random import randrange
def fortune(full_name, q_answered):

  list = ["Yes - definitely.", "It is decidedly so.", "Without a doubt.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "My sources say no.", "Outlook not so good.", "Very doubtful"]
  random_num = randrange(0,9)
  fortune1 = list[random_num]
  space = full_name.find(" ")
  name = full_name[:space]
  if name[-1] == "s":
    print(f"{name}' Question: {q_answered} ")
  else:
    print(f"{name}'s Question: {q_answered} ")
    print()
  print(f"Magic 8-Ball's answer: {fortune1} ")


  
def shipping():
  weight = float(input("What is your package weight in pounds? "))
  if weight <= 2:
    grnd = (weight*1.50+20)
    grndpr = (125)
    drone = (weight*4.5)
  elif weight > 2 and weight <= 6:
    grnd = (weight*3+20)
    grndpr = (125)
    drone = (weight*9)
  elif weight > 6 and weight <= 10:
    grnd = (weight*4+20)
    grndpr = (125)
    drone = (weight*12)
  else:
    grnd = (weight*4.75+20)
    grndpr = (125)
    drone = (weight*14.25)
  print(f"The price of ground shipping is ${grnd:.2f}" ) 
  print(f"The price of premium ground shipping is ${grndpr:.2f}" ) 
  print(f"The price of drone shipping is ${drone:.2f}" ) 
  if grnd < grndpr and grnd < drone:
    print(f"To save the most money, you should choose ground shipping! ")
  elif grndpr < grnd and grndpr < drone:
    print(f"To save the most money, you should choose ground shipping premium! ")
  elif drone < grnd and drone < grndpr:
    print(f"To save the most money, you should choose drone shipping! ")


def main():
  name = input("What is your full name? ")
  qu = input("What is your question you like to answer? ")
  fortune(name, qu)
  shipping()
  
if __name__ == "__main__":
  main()