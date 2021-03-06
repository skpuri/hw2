from MakeChange import *

import random

def main():
	denoms = [25,10,5,1]

	print 'Test one: expect [1,0,1,0]'
	stock = [2,0,1,2]
	change = 30
	a =  makechange(change, denoms, stock)
	print a

	print 'Test two: expect [0,4,0,0]'
	stock = [1,4,0,0]
	change = 40
	b =  makechange(change, denoms, stock)
	print b

	print 'Extra case: no change'
	stock = [0, 0, 0, 4]
	change = 5
	c =  makechange(change, denoms, stock)
	print c

	print 'Extra case: zero'
	stock = [0, 0, 0, 0]
	change = 10
	c =  makechange(change, denoms, stock)
	print c

	while True:
		denoms = [random.randrange(0, 50), random.randrange(0, 50),random.randrange(0, 50), random.randrange(0, 50)]
		stock = [random.randrange(0, 50), random.randrange(0, 50),random.randrange(0, 50), random.randrange(0, 50)]
		change = random.randrange(0,1000)
		result = makechange(change, denoms, stock)
		print '======================================='
		print 'dnm: ',denoms
		print 'stk: ',stock
		print 'chg: ', change
		print 'rst: ', result
		total = 0
		if result != None:
			for i in range(len(result)):
				total += denoms[i] * result[i]
			valid = change == total
			print 'vld: ', valid
			if not valid:
				raise ValueError()

if __name__ == '__main__':
	main()
