points = (3,4)
colours = ("red", 'green', "blue", "yellow", "magenta")

var1, var2, var3, var4, var5 = colours
print(var1)
print(var2)
print(var3)
print(var4)
print(var5)


moreColours = ("silver", "gold")
combinedColours = colours + moreColours
print(colours)
print(moreColours)
print(combinedColours)
print(colours *2) #writes out the contents 2 times

subset = colours[:4]
print(subset)
subset2 = colours[2:]
print(subset2)

print(len(colours))
print(points[1])
#points[0] = 5 # doesn't work because we can't change after creation
print(points)
print(colours[1])
print(colours[-1])
print(colours)

votes = ("Yes", "No", "No", "No", "Yes")
print(votes.count("Yes")) # 2
print(votes.count("No")) # 3