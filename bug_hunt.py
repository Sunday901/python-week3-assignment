count = 1
total = 0

# BUG: The while loop header was missing a colon, so Python could not read the loop.
while count < 6:
    # BUG: The loop needed to keep going until it reached 5, so the stopping value was corrected.
    total = total + count
    count = count + 1

# BUG: The print statement tried to join a string and an integer; converting total to a string fixes the output.
print("Sum of 1 to 5 is: " + str(total))
