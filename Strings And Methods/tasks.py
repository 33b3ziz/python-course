# 1
name = "Mohamed"
age = 21
country = "Egypt"

print("Hello '%s', How You Doing \ \"\"\" Your Age Is \"%d\"\" + And Your Country Is: %s" % (name, age, country))

# 2
print("Hello '%s', How You Doing \ \n\"\"\" Your Age Is \"%d\"\" + \nAnd Your Country Is: %s" % (name, age, country))

# 3
name = 'Elzero'

print("Second Letter Is %s" % name[1])
print("Third Letter Is %s" % name[2])
print("Last Letter Is %s" % name[len(name) - 1])

# Needed Output
# Second Letter Is "l"
# Third Letter Is "z"
# Last Letter Is "o"

# 4
name = 'Elzero'
print(name[1:4])
print(name[0:6:2])
print(name[-2::-2])

# Needed Output
# "lze"
# "Ezr"
# "rzE"

# 5
name = "#@#@Elzero#@#@"

print(name.strip("#@"))

# Needed Output
# Elzero

# 6
num = "9"
num = "15"
num = "130"
num = "950"
# num = "1500"

print(num.zfill(4))

# Needed Output
# 0009
# 0015
# 0130
# 0950
# 1500

# 7
name_one = "Osama"
name_two = "Osama_Elzero"

print(name_one.rjust(20, "@"))
print(name_two.ljust(20, "@"))

# Needed Output
# @@@@@@@@@@@@@@@Osama
# @@@@@@@@Osama_Elzero

# 8
name_one = "OSamA"
name_two = "osaMA"

print(name_one.swapcase())
print(name_two.swapcase())

# Needed Output
# osAMa
# OSAma

# 9
msg = "I Love Python And Although Love Elzero Web School"

print(msg.count("Love"))

# Needed Output
# 2

# 10
name = "Elzero"

print(name.index("z"))
# Needed Output
# 2

# 11
msg = "I <3 Python And Although <3 Elzero Web School"

print(msg.replace("<3", "Love", 1))
# Needed Output
# I Love Python And Although <3 Elzero Web School

# 12
msg = "I <3 Python And Although <3 Elzero Web School"

print(msg.replace("<3", "Love"))
# Needed Output
# I Love Python And Although Love Elzero Web School

# 13
name = "Osama"
age = 38
country = "Egypt"

print(f"My Name Is {name}, And My Age Is {age}, And My Country Is {country}")
# Needed Output Using f""
# My Name Is Osama, And My Age Is 38, And My Country Is Egypt