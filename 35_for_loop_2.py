#write a program to display and count only that countries that ends with land
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
    if "land" in item:
        print(item)
        count = count + 1
print("no of countries end with land ",count)