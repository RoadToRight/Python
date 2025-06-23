text = "My name is sameer"
# 01-2-3456-7-89-10-11 12 13 14 15 16 spaces also count

new_text = text.upper()
print(new_text)
print(text.lower())
print(text.title())
print(text.lstrip())
print(text.rstrip())
print(text.rstrip())
print(text.find("name"))
print(text.replace("name", "named"))
new_text2 = "name" in text
new_text3 = "name" not in text
print(new_text2)
print(new_text3)
