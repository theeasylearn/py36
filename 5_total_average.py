# write a program to make total of 5 subject marks and calculate average and display total and average

science = input("Enter science marks")
maths = input("Enter maths marks")
gujarati = input("Enter gujarati marks")
social = input("Enter social study marks")
hindi = input("Enter hindi marks")

#convert marks into integer 
science = int(science)
maths = int(maths)
gujarati = int(gujarati)
social = int(social)
hindi = int(hindi)

#process 
sum = science + maths + gujarati + social + hindi 
average = sum / 5
print("total = ",sum," Average = ",average)


