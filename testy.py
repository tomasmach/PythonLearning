with open("text.txt", "a+" ) as file:
    file.seek(0)
    content = file.read()
    file.write(content)
    file.write(content)