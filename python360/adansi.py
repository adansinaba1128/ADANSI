print("Hello World")

myName = "Adansi"
myOccupation = "Childcare"
age = 24
isEmployed = True
isNotFromAfrica = False

print("Am Adansi ", myName)
print("My name is %s I am a %s" % (myName, myOccupation))

dataTypeOfName =type(myName)
print(type(myName))
print(type(age))
print(type(isEmployed))
print(type(isNotFromAfrica))

def sum (first, second):
  addition = (first, second)

def sum (first,second):
  addition = first + second
  return addition

print(sum(10, 5))




total = sum(10, 5)
total = sum(total, 20)
total = sum(total, 30)
total = sum(total,50)
print("The total is: ", total)


def calculate (action, firstNum, secondNumber):
  if action == "add":
    result = firstNum + secondNumber
    return result

  if action == "subtract" :
    result = firstNum - secondNumber
    return result



calcResult = calculate("subtract", 10, 5)

print("The result is: ", calcResult)

number = 1

for number in range(10) :
  print("Number: ", number)

names = [ "Adansi","David", "Kate", "Esi" ]
for name in names:
  print("Name is: ", name)


print("Our loop is done!")







