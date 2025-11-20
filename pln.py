n = int(input("Enter No :"))
original = n
rev = 0
while n > 0:
    d = n % 10
    rev = rev * 10 + d
    n = n // 10
if original == rev:
    print("No is Palindrome")
else:
    print("No is not Palindrome")
