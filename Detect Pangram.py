alphabet='abcdefghijklmnopqrstuvwxyz'
pangram= 'Cwm fjord bank glyphs vext quiz'

result=set(alphabet).intersection(set(pangram.lower()))
if result==set(alphabet):
    print('It is a pangram')
else:print('It is not a pangram')
print(sorted(result))
