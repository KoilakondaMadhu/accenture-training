# Read nine input values representing three values for each of the three categories
t1_1 = int(input())
t2_1 = int(input())
t3_1 = int(input())

t1_2 = int(input())
t2_2 = int(input())
t3_2 = int(input())

t1_3 = int(input())
t2_3 = int(input())
t3_3 = int(input())

# Create a list to store the averages of each category
avg = []

# Calculate the average for each category and append it to the avg list
avg.append((t1_1 + t1_2 + t1_3) // 3)
avg.append((t2_1 + t2_2 + t2_3) // 3)
avg.append((t3_1 + t3_2 + t3_3) // 3)

# Find the maximum average from the avg list
m = max(avg)

# Iterate through the avg list to find the category with the highest average
for i in range(3):
    if avg[i] == m:
        # Print the category with the highest average (add 1 to convert from 0-based to 1-based index)
        print(i + 1)
