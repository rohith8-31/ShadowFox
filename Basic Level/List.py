# Initial list
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("Step 1 - Initial Justice League:")
print(justice_league)
print()

# 1. Count members
print("Step 2 - Number of members:")
print(len(justice_league))
print()

# 2. Add Batgirl and Nightwing
justice_league.extend(["Batgirl", "Nightwing"])
print("Step 3 - After adding Batgirl and Nightwing:")
print(justice_league)
print()

# 3. Move Wonder Woman to beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("Step 4 - Wonder Woman as leader:")
print(justice_league)
print()

# 4. Move Green Lantern between Aquaman and Flash
justice_league.remove("Green Lantern")
aquaman_index = justice_league.index("Aquaman")
justice_league.insert(aquaman_index + 1, "Green Lantern")
print("Step 5 - After separating Aquaman and Flash:")
print(justice_league)
print()

# 5. Replace with new team
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("Step 6 - New team:")
print(justice_league)
print()

# 6. Sort alphabetically
justice_league.sort()
print("Step 7 - Sorted list (alphabetical order):")
print(justice_league)
print("New leader:", justice_league[0])