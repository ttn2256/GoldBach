#  File: Goldbach.py

#  Description: Compute Goldbach's Conjecture 

#  Student Name: Tuan Nguyen


# check if a number is prime
def is_prime (n):
  limit = int (n ** 0.5) + 1
  divisor = 2
  while (divisor < limit):
    if (n % divisor == 0):
      return False
    divisor = divisor + 1
  return True


def main():
# prompt user enter lower limit

  ll = int(input('Enter the lower limit:'))
  while (ll % 2 !=0) or (ll<4):
    ll = int(input('Enter the lower limit:'))

# prompt user enter upper limit

  ul = int(input('Enter the upper limit:'))
  while (ul %2 !=0):
    ul = int(input('Enter the upper limit:'))

#check if lower smaller than upper

  while (ll>ul):
    ll = int(input('Enter the lower limit:'))
    ul = int(input('Enter the upper limit:'))


# run the outer loop and get even numbers from the range 
  for x in range (ll, ul+1, 2):
    print(x, end='')
# run the inner loop and check the numbers is prime or not 
    for n in range (2, int(x/2)+1):
# check the first nunber if it is a prime number
      if is_prime(n):
        p1 = n
# get the value of second number
        i = x - n
# check the second is prime number
        if is_prime(i):
          p2 = i
# print the result
          print (' =', p1, '+', p2, end ='')
    print('')


main()
