# Add up and print the sum of the all of the minimum elements of each inner array:
qlist = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
# The expected output is given by:
# 4 + -1 + 9 + -56 + 201 + 18 = 175
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code.
#  Run through the UPER problem solving framework while going through your thought process.
total = 0
#loop through array
for item in qlist:
    #loop through sub arrays
    minimum = item[0]
    for num in item:
        if num < minimum:
            minimum = num
    #find minimum value in each sub array
    total += minimum
    #print sum
print(total)