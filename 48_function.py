#  Keyword arguments in function

def getMerit(maths, english, history, drawing):
    print(maths, english, history, drawing)
    total = maths + english
    return total

maths = 48
english = 40
history = 45
drawing = 35

# total = getMerit(maths, english, history, drawing)
print('Total= ', getMerit(history=history, drawing=drawing, maths=maths, english=english))

