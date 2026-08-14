file = open("c:/Users/user/Downloads/geek.txt.txt", "r")
content = file.read()
print("file name:", file.name)
print("mode:", file.mode)
print("is closed?:", file.closed)
print(content)

# file.close()
print("is closed?:", file.closed)

file2 = open("c:/Users/user/Downloads/geek.txt.txt", "w")
txt = []
lenght = len(txt)
while lenght <= 5:
    txt += input(f"enter text {lenght + 1} :")

# for text in txt:
#     if len(txt) <= 5:
#         txt += input(f"enter text {len(txt) + 1} :")