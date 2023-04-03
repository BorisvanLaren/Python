text = input("Write you text here: ")
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

for q in range (1):
    print(f"q: {q + 1},")
for i in range (1):
    print(f"q: {q + 1}, i: {i + 2}")
for w in range (1):
    print(f"q: {q + 1}, i: {i + 2}, w: {w + 3},")
for y in range (1):
    print(f"q: {q + 1}, i: {i + 2}, w: {w + 3}, y: {y + 4}")
for s in range (1):
    print(f"q: {q + 1}, i: {i + 2}, w: {w + 3}, y: {y + 4}, s: {s + 5}," )
print ("have no idea how to get rid of those letters")

import time
while True:
   print("I Love Phyton")
   time.sleep(3)
   print(" ..--=\/=--..")
   time.sleep(1)
   print("but its not easy")
   time.sleep(0.5)

