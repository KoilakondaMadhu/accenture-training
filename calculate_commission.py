
# Chain Marketing Organization has has a scheme for income generation, through which its members generate income for themselves. The scheme is such that suppose A joins the scheme and makes R and V to join this scheme then A is Parent Member of R and V who are child Members. When any member joins the scheme then the parent gets total commission of 10% from each of its child members.

# Child members receive commission of 5% respectively. If a Parent member does not have any member joined under him, then he gets commission of 5%.

# Take name of the members joining the scheme as input.

# Display how many members joined the scheme including parent

# member.Calculate the Total commission gained by each members in the scheme. The fixed amount for joining the scheme is Rs.5000 on which commission will be generated

# SchemeAmount = 5000

# Example 1: When there are more than one child members
# Amit
# Y

# Input: (Do not give input prompts.Accept values as follows.)
# //Enter parent Member as this
# //Enter Y if Parent member has child members
# otherwise enter N Rajesh.Virat //Enter names of child members of Amit in comma separated
# Output:(Final Output must be in format given below.)
# TOTAL MEMBERS:3
# COMISSION DETAILS
# Amit: 1000 INR
# Rajesh :250 INR
# Virat: 250 INR

# Example 2: When there is only one child member in the hierarchy

# Input:
# Amit
# Y











# Initialize scheme amount and commission rates
scheme_amount = 5000
parent_commission_rate = 0.10
child_commission_rate = 0.05

# Initialize lists to store member names and their commissions
member_names = []
member_commissions = []

# Function to calculate commission for a member
def calculate_commission(member_type, children_count):
    if member_type == "parent":
        return scheme_amount * parent_commission_rate * children_count
    elif member_type == "child":
        return scheme_amount * child_commission_rate
    else:
        return 0  # Invalid member type

# Input: Enter the names of members joining the scheme
while True:
    member_name = input("Enter the name of a member (or 'done' to finish): ")
    if member_name == "done":
        break
    member_type = input("Is this member a 'parent' or 'child'? ")
    children_count = int(input("Enter the number of children under this member: "))
    
    member_names.append(member_name)
    commission = calculate_commission(member_type, children_count)
    member_commissions.append(commission)

# Display the number of members who joined the scheme
total_members = len(member_names) + 1  # Include the parent member
print(f"Total members who joined the scheme: {total_members}")

# Display the commissions for each member
for i in range(total_members):
    print(f"{member_names[i]} earned a commission of Rs. {member_commissions[i]:.2f}")

# Calculate and display the total commission earned by all members
total_commission = sum(member_commissions)
print(f"Total commission earned by all members: Rs. {total_commission:.2f}")
