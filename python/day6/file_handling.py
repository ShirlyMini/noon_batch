# txt or log

#create new- open exsisting -update
# write-while create new file if the file is not present
# if file is present it will overwrite
# fh = open("test1.txt", "w")
# fh.write("this is line one1\n")
# fh.write("this is line two1\n")
# fh.write("this is line three1\n")
# fh.close()

# append-if file not present it will create and append
# # if file is present it will append
# fh = open("test2.txt", "a")
# fh.write("this is line one\n")
# fh.write("this is line two\n")
# fh.write("this is line three\n")
# fh.close()

# read - default mode
# if not file FileNotFoundError: [Errno 2] No such file or directory: 'test3.txt'
# fh = open("test3.txt")
# print(fh.read())#FileNotFoundError: [Errno 2] No such file or directory: 'test3.txt'
# fh = open("test2.txt")
# var = fh.read()
# print(var)
# print(type(var))

# print(fh.readline())
# print(fh.readline())
# print(fh.readline())
# print(fh.readline())

# list1= fh.readlines()
#
# for i in list1:
#     if "three" in i:
#         print(i)

####################################################33
# with statement
#fh = open("test1.txt", "w")
# with open("test3.txt", "w") as fh:
#     for i in range(10):
#         fh.write(str(i)+"\n")


#####################
# create a file print 1 to 10
# reverse and print in same file

with open("test4.txt", "w") as fh:
    for i in range(10):
        fh.write(str(i)+"\n")

with open("test4.txt") as fr:
    line_list = fr.readlines()

with open("test4.txt", "w") as fh:
    for line in line_list[::-1]:
        fh.write(line)

