import re
def no_1():
    file = open("tt", "r")
    push = open("ss","w")
    # print(file.readline())
    # print(file.readlines())
    push.write("{")
    no_1 = file.readline()
    ls1= re.sub(" +"," ",no_1).split(" ")
    id = ls1[1]+":"
    len = ls1[2]
    type = ls1[4]
    time = ls1[6]
    no_1_write = "{len:"+len+",type:"+type+",time:"+time+","
    push.write(ls1[1]+":")
    push.write(no_1_write.replace("\n",""))
    print(ls1[1]+":")
    print(no_1_write.replace("\n",""))

n = 0
s = "atcg"
b = "tagc"
trantab = str.maketrans(s, b)
c = "aaaatttt"
print(c.translate(trantab))

for i in range(0,3):
    print(i)
