import sys

print(sys.version)

# ================
a = [11, 12, 13, 20, 21, 22]

for i in a:
    print("in for loop")
else:
    print

# ========append() & extend()==============
x = [1, 4, 7, 8, 5]
y = [9, 8, 5, 2, 6]
print(y)
print(sorted(y))
x.extend(y)
print(x)
x.append(y)
print(x)

rev = reversed(x)
print(type(rev))
print(list(reversed(x)))
# =========Slicing of String =================
s = "VDS TECH Labs"
print(s[1:-1])

# Update dict
d1 = {'a': 1}
d2 = {'b': 2}
d1.update(d2)
print(d1)
# =========================
s1="This is simple string with many character"
print(set(s1))
print(len(set(s1)))