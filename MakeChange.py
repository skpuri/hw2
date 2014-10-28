# MakeChange.py
# Alan Salazar Wink - 999868379
# Calculates the ammount of coins to be used as change

def makechange(atmchange, denoms, coinstock):
	try:
		return makechange2(atmchange, denoms, coinstock)
	except:
		return None

def makechange2(atmchange, denoms, coinstock):
	
	# No denoms or coinstock, stop
	if (not denoms and not atmchange) :
		return []
	
	# If there is no way to give the right change, exeption
	atmtotal = 0
	for i in range(len(denoms)): 
		atmtotal += denoms[i]*coinstock[i];
	# There is no coins to give that change
	if atmtotal < atmchange: 
		raise ValueError("NoCoins")
	
	# Remove a coin
	change = 0
	# If the change is greater than the coin value and there is stock
	while(atmchange >= denoms[0] and coinstock[0] > 0):
		# Remove a coin
		atmchange -= denoms[0]
		coinstock[0] -= 1
		change += 1

	while change >= 0:
		#Try to remove a coin from stock
		try:
			result = [change]
			result.extend(makechange(atmchange, denoms[1:], coinstock[1:]))
			return result
		except ValueError:
			# No coins to finish, put a coin back on stock until there is no coins removed
			if change > 0:
				# Remove a coin
				atmchange += denoms[0]
				coinstock[0] += 1
				change -= 1
			else:
				raise ValueError("NoCoins")
	
