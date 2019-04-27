a = "222,22"
b= (a.split(','))
print(b[1] + str(type(b[1])))

d = "23:off25:off"
if "on" in d:
    print("bbb")
for x in d:
    d = d.replace(":off", ",")

s = d.rstrip(",")
s = s.split(",off")
print(str(s) + str(type(s)))