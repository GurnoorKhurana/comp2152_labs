# Author: Gurnoor Khurana
# Assignment #1

# Defining Variables
gym_member = "Jordan Michaels"  # String
preferred_weight_kg = 22.7  # Float
highest_reps = 30  # Integer
membership_active = False  # Boolean

# Dictionary with workout stats; Data type is dictionary of strings to tuples of integers
workout_stats = {
    "Sam": (35, 40, 20),  # yoga, running, weightlifting
    "Taylor": (45, 35, 30),
    "Chris": (28, 50, 18)
}

# Calculates total workout minutes for each individual then adds it to the dictionary
for friend, workouts in workout_stats.items():
    total_minutes = sum(workouts)
    workout_stats[f"{friend}_Total"] = total_minutes

# Nested list with workout minutes; Data type is 2D list of integers
workout_list = [
    list(workouts) for workouts in workout_stats.values() if isinstance(workouts, tuple)
]

# Extracts and prints the minutes for yoga/running for all friends
yoga_running_minutes = [row[:2] for row in workout_list]  # First two columns (yoga and running)
print("Yoga and Running minutes for all friends:", yoga_running_minutes)

# Extracts and prints the minutes for weightlifting for the last two friends
weightlifting_minutes = [row[2] for row in workout_list[-2:]]  # Last column (weightlifting)
print("Weightlifting minutes for the last two friends:", weightlifting_minutes)

# Checks if any friend's total workout minutes are >= 120 and print a message
for friend, total_minutes in workout_stats.items():
    if isinstance(total_minutes, int) and total_minutes >= 120:
        print(f"Keep up the great work, {friend.split('_')[0]}!")

# Checks to see if inputted friend exists; If exists, prints workout minutes for each activity
friend_name = input("Enter a friend's name: ")

if friend_name in workout_stats:
    stats = workout_stats[friend_name]
    if isinstance(stats, tuple):
        total_minutes = sum(stats)
        print(f"{friend_name}'s workout minutes: Yoga: {stats[0]}, Running: {stats[1]}, Weightlifting: {stats[2]}")
        print(f"Total workout minutes: {total_minutes}")
else:
    print(f"Friend {friend_name} not found in the records.")

# Finds the friend with the highest and lowest total workout minutes
total_minutes_dict = {friend: total for friend, total in workout_stats.items() if isinstance(total, int)}

max_friend = max(total_minutes_dict, key=total_minutes_dict.get)
min_friend = min(total_minutes_dict, key=total_minutes_dict.get)

print(f"Friend with the highest total workout minutes: {max_friend.split('_')[0]}")
print(f"Friend with the lowest total workout minutes: {min_friend.split('_')[0]}")
