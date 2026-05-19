# write a program to accept 24 hours format time from user. then display it in 12 hours format with am pm. 
time = int(input("Enter times"))
print(f"you have given {time}")
if time>12: # < > <= >= == !=
    time = time - 12 
    print(f"{time} PM")
else:
    print(f"{time} AM")

print("Good bye.")

