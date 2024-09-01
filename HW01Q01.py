chairs = '15' #Using '15' it will be treated as a string and repeat it 4  times.
# instead without the quotes 15 will be treated as integer and multiplied by 4
nails = 4
total_nails = chairs * nails
message = 'I need to buy {} nails'.format(total_nails)
print('You need to buy {} nails'.format(message)) #This will return  "You need to buy I need to buy 'x' nails" which doesn't make sense
#instead we should  put "message = 'I need to buy {} nails'.format(total_nails) print(.format(message))
#therefore the correct code is:
chairs = 15
nails = 4
total_nails = chairs * nails
message = 'I need to buy {} nails'.format(total_nails)
print(message)
