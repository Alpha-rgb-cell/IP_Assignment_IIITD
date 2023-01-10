num = int(input("Enter a number between 0 and 99: "))

if num <= 20:
  if num == 0:
    print("zero")
  elif num == 1:
    print("one")
  elif num == 2:
    print("two")
  elif num == 3:
    print("three")
  elif num == 4:
    print("four")
  elif num == 5:
    print("five")
  elif num == 6:
    print("six")
  elif num == 7:
    print("seven")
  elif num == 8:
    print("eight")
  elif num == 9:
    print("nine")
  elif num == 10:
    print("ten")
  elif num == 11:
    print("eleven")
  elif num == 12:
    print("twelve")
  elif num == 13:
    print("thirteen")
  elif num == 14:
    print("fourteen")
  elif num == 15:
    print("fifteen")
  elif num == 16:
    print("sixteen")
  elif num == 17:
    print("seventeen")
  elif num == 18:
    print("eighteen")
  elif num == 19:
    print("nineteen")
  elif num == 20:
    print("twenty")

else:
  tens_digit = num // 10
  units_digit = num % 10

  if tens_digit == 2:
    print("twenty", end=" ")
  elif tens_digit == 3:
    print("thirty", end=" ")
  elif tens_digit == 4:
    print("forty", end=" ")
  elif tens_digit == 5:
    print("fifty", end=" ")
  elif tens_digit == 6:
    print("sixty", end=" ")
  elif tens_digit == 7:
    print("seventy", end=" ")
  elif tens_digit == 8:
    print("eighty", end=" ")
  elif tens_digit == 9:
    print("ninety", end=" ")

  if units_digit == 1:
    print("one")
  elif units_digit == 2:
    print("two")
  elif units_digit == 3:
    print("three")
  elif units_digit == 4:
    print("four")
  elif units_digit == 5:
    print("five")
  elif units_digit == 6:
    print("six")
  elif units_digit == 7:
    print("seven")
  elif units_digit == 8:
    print("eight")
  elif units_digit == 9:
    print("nine") 
    
