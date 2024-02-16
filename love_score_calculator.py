print("Welcome to Love Score calculator")

name_1=input("Your name ? ")
name_2=input("Your Partner name ? ")

combined_name=name_1.lower()+name_2.lower()

scores={}
container="truelove"

for _character in container:
    scores[_character]=combined_name.count(_character)

total_score=0
for _score in scores:
    total_score+=scores[_score]

print(f"Your Love Score is : {total_score}")
