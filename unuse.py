import re


def matchuser(id, semester):
    if (re.findall(r'BCSS2018', id) and (semester == 1)):
        print("Yes")
    else:
        print("No")

matchuser('BCSS2018022',1)