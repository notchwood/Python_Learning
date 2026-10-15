# check for a persons stage in life based on age entered
age = 12
msg = "\nThe person is a"
if age == 0:
	stage_of_life = "is not born YET!"
elif age < 3:
	stage_of_life = "a baby"
elif age < 4:
	stage_of_life = "a toddler"
elif age < 13:
	stage_of_life = "a kid"
elif age < 20:
	stage_of_life = "a teen ager"
elif age < 65:
	stage_of_life = "an adult"
elif age >= 65:
	stage_of_life = "an elder"

print(msg, stage_of_life)