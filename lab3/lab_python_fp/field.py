goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'ковер', 'price': 300, 'color': 'black'},
    {'title': 'КОВЕР', 'price': 300, 'color': 'black'},
    {'title': 'Диван для отдыха', 'color': 'black'},
    {'title': 'Язвочка', 'color': 'black'}
]

def field(items, *args):
    # print(items[0])
    assert len(args) > 0
    # print('lol')
    ans = list()
    for dct in items:
        temp_dct = dict()
        for key in args:
            if key in dct.keys():
                temp_dct[key] = dct[key]
        ans.append(temp_dct)
    # print(ans)
    if len(args) > 1:
        return ans
    else:
        key0 = list(ans[0].keys())[0] # Ключ для поиска
        monster = sorted([ans[i][key0] for i in range(len(ans))], key= lambda x: x.lower())
        return [monster[i]  for i in range(len(monster) - 1) if monster[i].lower() != monster[i-1].lower()] + [monster[-1]]



# print(field(goods, 'title'))
# print(field(goods, 'title', 'price'))