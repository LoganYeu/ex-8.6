#Logan Yeubanks, Linus Wiertalla
numbs = list()
while True:
    num = input("Enter a number ")
    if num == "done":
        break
    try:
        fnum = float(num)
        
    except:
        print("Make sure to enter a number")
        
    numbs.append(fnum)
    #print(numbs)
print ("Maximum:",max(numbs))
print ("Minimum:",min(numbs))
