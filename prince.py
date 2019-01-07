frogList=['Alice', 'Bob', 'Frog']
def isPrince(frogList):
    for elem in frogList:
        if elem[0] == "F":
            return elem

print(isPrince(frogList))