from math import *

def calcDmgScalar(might, luck):

	critChance = (0.0117*luck+4.2084) / 100
	critMultiplier = 1 + (19.2918*log(luck+141.138)+19.9851) / 100

	regDmgMultiplier = 1 + ((might / 18) / 100)

	mightDamage = 1 * regDmgMultiplier


	regDmgChance = 1 - critChance

	avgDamage = (regDmgChance * mightDamage) + (critChance * critMultiplier * mightDamage)
	return avgDamage


def calcDmgIncreaseFromLuckIncrease(might, luck, newLuck):
	a = calcDmgIncrease(might, newLuck)
	b = calcDmgIncrease(might, luck)
	return a-b

def calcDmgIncreaseFromMightIncrease(might, newMight, luck):
	a = calcDmgIncrease(newMight, luck)
	b = calcDmgIncrease(might, luck)
	return a-b

def printOneToOneThresholdMinLuck():
	might = 0
	while True:
		if (calcDmgIncreaseFromMightIncrease(might, might + 1, 378+378) < calcDmgIncreaseFromLuckIncrease(might, 378+378, 378+378+1)):
			break

		might+=1
	print(might)
print(calcDmgScalar(4813+292, 1273))
print(calcDmgScalar(4813, 1273+278))