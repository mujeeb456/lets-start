menu={
    'latte':{
      'ingredients':{
        'milk':150,
        'water':200,
        'coffee':24,
      },
      'cost':150
    },
    "espresso":{
      'ingredients':{
        'water':50,
        'coffee':18,
      },
      "cost":100,
    },
    "cappuccino":{
      'ingredients':{
        'milk':250,
        'water':100,
        'coffee':24
      },
      'cost':200,
    },
}
resources={
  "water":500,
  "milk":200,
  "coffee":100,
}
def make_coffee(coffeename,ingre):
  for item in ingre:
    resources[item]-=ingre[item]
  print(f"here is you {coffeename}.!!!")
  
  
def payment_status(price,cost):
  if price>=cost:
    global profit
    profit+=cost
    change=price-cost
    print(f"here  is your {change} in change")
    return True
  else:
    print("sorry that is not enough money your money will be refunded")
    return False
    
def process_coins():
  five=int(input ('how many 5 rupees coins?: '))
  ten=int(input('how many 10 rupees coins?: '))
  twenty=int(input('how many 20 rupees coins?: '))
  total=five*5+ten*10+twenty*20
  return total
def check_resources(ordered):
  for item in ordered:
    if ordered[item]>resources[item]:
      print(f"sorry {item} is not available")
      return False
    else:
      return True
profit=0
repeat=True
while repeat:
  choice=input("what would you like to have:(latte,espresso,cappuccino?)")
  if choice=="off":
    repeat=False
  if choice=='report':
    for i in resources:
     print(f"{i}={resources[i]}")
    print(f"money={profit}")
  else:
    coffetype=menu[choice]
    print(coffetype)
    if check_resources(coffetype['ingredients']):
     payment=process_coins()
     if payment_status(payment,coffetype['cost']):
       make_coffee(choice,coffetype['ingredients'])
     
    