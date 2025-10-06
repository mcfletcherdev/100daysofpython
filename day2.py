# Create a tip generator.
print('Welcome to the tip generator!')
amount = input('How much was your bill? ')
tipPercent = input('How much would you like to tip (%)? ')
tipAmount = int(amount) * int(tipPercent)/100
print('Your tip should be ' + str(tipAmount) + '.')