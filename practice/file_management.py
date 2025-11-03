# f = open('data.txt', 'r')


# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readlines())

# # for i in f:
# #     print(i.strip())

# f = open('data.txt', 'w')

# f.write("I am Mukul Malse")

f = open('data.txt', 'a')
# f.write("\n This is newly added line.")
# f.write("This is newly added line 2.")

lines = ["Aa\n", "Bb\n", "Cc\n"]

f.writelines(lines)
f.close()


