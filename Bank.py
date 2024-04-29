# Program bank that shows money in cent amount
# Author: Carlos Rigueti

a = int (input ("Enter amount1 (in cent):"))
b = int (input ("Enter amount2 (in cent):"))
sum  = (a + b)/100
formatted_result = "{:.2f}".format(sum)
print  (f" The sum of these is € {formatted_result}\n Thank you for purchasing with us.")
 
  


