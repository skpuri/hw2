from MakeChange import *

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

if __name__ == '__main__':
	main()
