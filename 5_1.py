text = input("Write you text here: ")
for
if text.isupper():
    print(f"you typed upper case letters {len(text)}")
if text.islower():
    print(f"you typed lower case letters {len(text)}")
if text.isdigit():
    print(f"you typed digits {len(text)}")
    a = int(text)
    if a % 2 == 0:
        print ("Number id even")
    else:
        print ("number is odd")

print (f"you typed {len(text)} char")

