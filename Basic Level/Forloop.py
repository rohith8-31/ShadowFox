import random

# Task 1: Die Rolling Simulation
print("Task 1 - Die Rolling Simulation:")
rolls = []
six_count = 0
one_count = 0
two_sixes_count = 0

for _ in range(20):
    roll = random.randint(1, 6)
    rolls.append(roll)
    
    if roll == 6:
        six_count += 1
    if roll == 1:
        one_count += 1
    if len(rolls) >= 2 and rolls[-1] == 6 and rolls[-2] == 6:
        two_sixes_count += 1

print("All rolls:", rolls)
print("Number of 6s rolled:", six_count)
print("Number of 1s rolled:", one_count)
print("Number of times two 6s rolled in a row:", two_sixes_count)
print()

# Task 2: Jumping Jacks Workout
print("Task 2 - Jumping Jacks Workout:")
total_jacks = 0
target = 100
set_size = 10

for _ in range(target // set_size):
    total_jacks += set_size
    print(f"Completed {set_size} jumping jacks. Total: {total_jacks}")
    
    tired = input("Are you tired? (yes/y or no/n): ").lower()
    
    if tired in ['yes', 'y']:
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").lower()
        if skip in ['yes', 'y']:
            print(f"You completed a total of {total_jacks} jumping jacks.")
            break
    else:
        remaining = target - total_jacks
        print(f"Remaining jumping jacks: {remaining}")
        
if total_jacks == target:
    print("Congratulations! You completed the workout!")