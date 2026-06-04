#example of for loop on list 
countries = [
    "Germany", "Polynesia", "Malaysia", "Argentina", "India", 
    "Thailand", "Switzerland", "Micronesia", "Indonesia", "Canada", 
    "Greenland", "South Africa", "Kenya", "Italy", "Brazil", 
    "South Korea", "Ireland", "Melanesia", "Australia", "Iceland", 
    "Japan", "Spain", "Poland", "Mexico", "Scotland", 
    "England", "Egypt", "Finland", "New Zealand", "France","Egypt","U.A.E","South Korea"
]
count = 0
for item in countries:
    print(item)
    count = count + 1
print("no of countries",count)