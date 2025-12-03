import re #regular expressions module

patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

email_mal = "algo"
email_bien = "correofalso123@gmail.com"

print(re.match(patron, email_mal))  # None
print(re.match(patron, email_bien))
