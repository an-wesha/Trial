def odd(n):
  if n % 2 == 1:
    return True
  return False

while True:
    inp = input("Enter range of numbers in which you want to find even and odd: ")
    try:
        x = int(inp)
        break
    except:
        print("Invalid input. You can enter only positive integers.")

counto = 0
counte = 0
for i in range(x+1):
  if odd(i):
    print(str(i)+" is ODD")
    counto = counto + 1
  else:
    print(str(i)+" is EVEN")
    counte = counte + 1
print("There are " + str(counto) + " odd numbers and " + str(counte) + " even numbers in the given range.")
