huntpiloturi = input().strip()

i = huntpiloturi.find("<")
sub_string = huntpiloturi[:i]
l = sub_string.find("%22")
r = sub_string.rfind("%22")
if r > 0:
    print(huntpiloturi[l+3:r])
else:
    print(sub_string.replace('"', ""))