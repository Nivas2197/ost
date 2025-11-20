Here we create a small code snippet to find whether the given no is palindrome or not
Algo:
1.Take input From User and Conver it to Integer
2.Declare a new variable original and save input value to it 
3.Assign rev=0
4.Run a while loop till n>0:
  4.1. calculate n%10 and store in new var d
  4.2. rev=rev*10+d
  4.3. make n=n//d
#This will run until n=0
5.Using If Else we compare original and rev:
  5.1 if original==rev:
      we print "Given no is palindrome"
  5.2 else:
      we are printing "Given mo is not palindrome"
End

How To Run:
1.We can Run this code in any online python interpretor
2.We can run code using Vs code(python extension)
3.We can install python on terminal then run 
