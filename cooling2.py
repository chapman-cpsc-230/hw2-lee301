"""
File: cooling2.py

Copyright (c) 2016 Krystal Lee

License: MIT

<find cooling rate of tea of every minute>

"""

t = 0 #minutes
T_tea = 100 #degrees C, temperature of the tea
T_air = 20 #degrees C, temperature of the room
ks = 0.055/60 #by second-by-second
# - k(T_tea - T_air) #the rate of cooling on a second-by-second, reporting the results once for every minute

user_input = raw_input ("Enter the initial tea temperature in Celsius:")
T_tea= int(user_input)

user_input = raw_input ("Enter the room temperature in Celsius:")
T_air = int(user_input)

user_input = raw_input ("Enter the number of minutes for which the tea was cooling down:")
num_minutes = float(user_input)

t = 0

print "Temperature of the air: 20"
print "Number of minutes: 20"
print "Minute Temperature"

while t < 20:
    print "%3.1d   %4.1f"%(t, T_tea)
    T_tea -= ks*(T_tea - T_air)
    t += 1

print (t, T_tea)
