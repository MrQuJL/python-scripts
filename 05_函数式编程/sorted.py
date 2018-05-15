a = sorted([36,12,8,23,100])

print(a)

b = sorted([34,12,1,0,-22,99],key=abs)

print(b)

c = sorted(['bob','about','Zoo','Credit'])

print(c)

d = sorted(['bob','about','Zoo','Credit'],key=str.lower)

print(d)

e = sorted(['bob','about','Zoo','Credit'],key=str.lower, reverse=True)

print(e)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
	return t[0].lower()

L2 = sorted(L, key=by_name)
print(L2)

def by_score(t):
	return t[1]

L2 = sorted(L, key=by_score, reverse=True)
print(L2)











