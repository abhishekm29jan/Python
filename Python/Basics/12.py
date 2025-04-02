# Writing in a file
a = "Abhi is a rockstar"
with open("test.txt", "w") as f:
    f.write(a)
    f.write(" But sometimes he sings bad")

# Reading a file
# with open("test.txt","r") as f:
#    s = f.read()
#    print(s)
