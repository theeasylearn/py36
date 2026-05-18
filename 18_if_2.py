#write a program to findout whether shape is portrait, landscape or square from given length and width.

length = int(input("Enter length of the shape"))
width = int(input("Enter width of the shape"))

if width>length:
    print("given shape is landscape")

if length>width:
    print("given shape is portrait")

if length==width:
    print("given shape is square")

print("good bye.")