hours = int(raw_input('Enter the number of hours you worked this week:'))
rate = int(raw_input('Enter your hourly rate:')) 

if hours <= 40:
    total = hours * rate
else:
    total = 40 * rate + (hours - 40) * (1.5 * rate)

print 'This is how much you will get paid this week.'
print "Your total pay is:"
print int(total)

