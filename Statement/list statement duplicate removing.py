a = [55,87,90,55,98,21,98,76,100]
dub_items=set()
uniq_items=[]
for x in a:
    if x not in dub_items:
        uniq_items.append(x)
        dub_items.add(x)
print(dub_items)