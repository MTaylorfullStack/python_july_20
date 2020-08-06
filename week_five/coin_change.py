# Generate Coin Change
# Implement generateCoinChange(cents) that accepts a parameter for the number of cents, and
# computes how to represent that amount with the smallest number of coins. print the result.

# declare our function accept a parameter for number of cents
# create variables for our denominations
# loop until cents is 0
    # if cents is more than or equal 100
        # we can count a dollar
        # take 100 away from cents
    # elif cents is more than or equal 25
        # we can count a quarter
        # take 25 away from cents
    # elif cents is more than or equal 10
        # we can count a dime
        # take 10 away from cents
    # elif cents is more than or equal 5
        # we can count a nickel
        # take 5 away from cents
    # else
        # we can count a penny
        # take 1 away from cents
# return denomination in normal coin value

def coin_change(cents):
    change = {
        'dollars' : 0,
        'quarters' : 0,
        'dimes' : 0,
        'nickels' : 0,
        'pennies' : 0,
    }
    while cents > 0:
        if cents >= 100:
            change['dollars'] += 1
            cents -= 100
        elif cents >= 25:
            change['quarters'] += 1
            cents -= 25
        elif cents >= 10:
            change['dimes'] += 1
            cents -= 10
        elif cents >= 5:
            change['nickels'] += 1
            cents -= 5
        else:
            change['pennies'] += 1
            cents -= 1
    return change

print(coin_change(95415489))