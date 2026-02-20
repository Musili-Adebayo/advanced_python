# Task 1
#  Given the list below
# sales = [120,450,800,50,900,300]
# Write a Python code that classifies items in the list as Low, Medium, or High. 
# Also, do a count of items based on this classification and finally give a sum of items 
# in each classification
# Key: less than 300 – low
# >= 300 <= 700 medium
# > 700 that's high

sales = [120, 450, 800, 50, 900, 300]

# Initialize dictionaries to store counts and sums
classification = {}
count = {"Low": 0, "Medium": 0, "High": 0}
total = {"Low": 0, "Medium": 0, "High": 0}

for value in sales:
    if value < 300:
        category = "Low"
    elif 300 <= value <= 700:
        category = "Medium"
    else:
        category = "High"

    classification[value] = category
    count[category] += 1
    total[category] += value

print("Classification:", classification)
print("Count:", count)
print("Sum:", total)
