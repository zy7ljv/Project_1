from sys import argv

script, user_name, language = argv
prompt = ">"

print(f"Hi {user_name}, I'm the {script} script. I am speaking {language}")
print(f"I'd like to ask you a few questions in {language} please.")
print(f"do you like me {user_name}? Please in {language}.")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What kind of computer do you have {user_name}?")
computer = input(prompt)

print(f"Please teach me say Hello when you in {lives}.")
hello = input(prompt)

print(f"""
Alright, so {user_name}, you said {likes} about liking me,
you live in {lives}. you speak {language}, 
and Hello is {hello} in {language}.
And you have a {computer} computer. Nice!
""")

