# Get user input for base attack speed, bonus attack speed %, and level
base_attack_speed = float(input("Enter the base attack speed: "))
bonus_attack_speed_percent = float(input("Enter the bonus attack speed %: "))
level = int(input("Enter the level: "))

# Convert bonus attack speed % to decimal
bonus_attack_speed_decimal = bonus_attack_speed_percent / 100

# Compute current attack speed
current_attack_speed = base_attack_speed * (1 + (bonus_attack_speed_decimal * (level - 1)))

# Round current attack speed to the nearest three decimal places
current_attack_speed = round(current_attack_speed, 3)

# Display the result
print("The character's current attack speed is:", current_attack_speed)
