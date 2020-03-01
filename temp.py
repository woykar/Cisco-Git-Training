x = 'run'
y = 'fight'

z1 = 'brave'

if z1=='coward':
    print(x)
elif z1!='coward':
    print(y)


def main():
    password = input("Please enter your password::")
    if password=="student":
        student()
    elif password=="teacher":
        teacher()
    elif password=="headmaster":
        headmaster()
    elif password=="janitor":
        janitor()
    else:
        print("incorrect password")

def student():
    print("welcome student")
def teacher():
    print("welcome teacher")
def headmaster():
    print("welcome headmaster")
def janitor():
    print("welcome janitor")