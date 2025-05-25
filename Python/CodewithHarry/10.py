phy = int(input("Enter marks:"))
chem = int(input("Enter marks:"))
bio = int(input("Enter marks:"))

avg = (phy+chem+bio)/3
print(avg)
per = avg * 100
if(phy>33 and chem>33 and bio>33):
    if(per>33):
        print("PASS")
else:
    print("FAIL")