w=input()
W=w.lower()
Text=[]
while True:
    text=input()
    if text=='END_OF_TEXT':
        break
    Text.extend(text.split())
for i in range(len(Text)):
    Text[i]=Text[i].lower()
print('%d'%Text.count(W))
