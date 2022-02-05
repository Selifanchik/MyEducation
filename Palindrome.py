number = int(input())
num = number
num_palindrome = 0
while num > 0:
    num_palindrome = num_palindrome * 10 + num % 10
    num = num // 10
if number == num_palindrome:
    print('Palindrome')
else:
    print('No Palindrome')
