import wizcoin

purse = wizcoin.WizCoin(2, 5, 99, 'purse') # The ints are passed to __init__().
print(purse.name)
print('G:', purse.galleons, 'S:', purse.sickles, 'K:', purse.knuts)
print('Total value:', purse.value())
print('Weight:', purse.weightInGrams(), 'grams')

print()

coinJar = wizcoin.WizCoin(13, 0, 0, 'coinjar') # The ints are passed to __init__().
print(coinJar.name)
print('G:', coinJar.galleons, 'S:', coinJar.sickles, 'K:', coinJar.knuts)
print('Total value:', coinJar.value())
print('Weight:', coinJar.weightInGrams(), 'grams')