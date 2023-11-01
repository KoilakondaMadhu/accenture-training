# Problem Statement

# A washing machine works on the principle of Fuzzy System, the weight of clothes put inside it for washing is uncertain But based on weight measured by sensors, it decides time and water level which can be changed by menus given on the machine control area.

# For low level water, the time estimate is 25 minutes, where approximately weight is between 2000 grams or any nonzero positive number below that.

# For medium level water, the time estimate is 35 minutes, where approximately weight is between 2001 grams and 4000 grams.

# For high level water, the time estimate is 45 minutes, where approximately weight is above 4000 grams.

# Assume the capacity of machine is maximum 7000 grams

# Where approximately weight is zero, time estimate is 0 minutes.

# Write a function which takes a numeric weight in the range [0,7000] as input and produces estimated time as output is: "OVERLOADED", and for all other inputs, the output statement is



def washing_machine_time(weight):
    if weight < 0 or weight > 7000:
        return "INVALID INPUT"  # Weight is out of range

    if weight == 0:
        return "0 minutes"  # No clothes, no time needed

    if weight <= 2000:
        return "25 minutes"  # Low level water

    if weight <= 4000:
        return "35 minutes"  # Medium level water

    return "45 minutes"  # High level water

# Example usage:
weight = int(input("Enter the weight of clothes (0-7000 grams): "))
estimated_time = washing_machine_time(weight)
print(f"Estimated washing time: {estimated_time}")
