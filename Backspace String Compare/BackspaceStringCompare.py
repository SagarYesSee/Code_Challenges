s = input("enter string 1: ")
t = input("enter string 2: ")

def backspaceCompare(s, t):
    s_new = ""
    t_new = ""
    for i in range(len(s)):
        if s[i] == "#":
            s_new = s_new[:-1]
        else:
            s_new += s[i]
    for j in range(len(t)):
        if t[j] == "#":
            t_new = t_new[:-1]
        else:
            t_new += t[j]
    return s_new == t_new

print(backspaceCompare(s, t))