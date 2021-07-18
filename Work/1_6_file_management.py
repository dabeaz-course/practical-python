# 1.6 File Management

f = open('foo.txt', 'rt')   # open for reading (text)
g = open('bar.txt', 'wt')   # open for writing (text)


data = f.read()   # read data
print(data)       # print data

f = open('foo.txt', 'rt')   # open for reading (text)
data = f.read(100)  # read 100 bytes


f.close()  # close handle (has to be done) otherwise file is locked.


# Read files so that the handle is closed automatically
# 
with open('foo.txt', 'rt') as file:
    data = file.read()
    # `data` is a string with all the text in `foo.txt`



    