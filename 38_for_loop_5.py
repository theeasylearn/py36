#write a program to calculate total score of team & findout maximum runs by player & his name  using dictionary and for loop 
score = { "Sanju Samson": 89, "Abhishek Sharma": 52, "Ishan Kishan": 54,"Hardik Pandya": 18,"Suryakumar Yadav": 0, "Tilak Varma": 8, "Shivam Dube": 26, "Axar Patel": 0, "Varun Chakravarthy": 0,"Jasprit Bumrah": 0, "Arshdeep Singh": 0}

total = 0
max = 0 
player = None 
for key in score:
    print(score[key])
    total = total + score[key]
    if max<score[key]:
        max = score[key] # 89
        player = key 

print("total score ",total)
print("Top Scorer ",player," and he made ",max)
