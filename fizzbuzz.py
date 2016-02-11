# Takes an integer input from command line and iterates from 1 to n printing "fizz" if it is a multiple of 2
# "buzz" if it is a multiple of 3 and "fizzbuzz" if number is multiple of 2 and 3.

# Input: An input n from command line
# Example execution: python fizzbuzz.py 10

from sys import argv
def fizzbuzz(n):
	idx = 1
	while idx<=n:
		if idx%2==0 and idx%3==0:
			print "fizzbuzz";
		elif idx%2==0:
			print "fizz";
		elif idx%3==0:
			print "buzz";
		else:
			print idx;
		idx = idx+1;

def __main__():
	n = int(argv[1]);
	fizzbuzz(n);
__main__()
