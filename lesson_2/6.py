items = []
features = {"название": '', "цена": '', "количество": '', "ед.": ''}
analytic = {"название": [], "цена": [], "количество": [], "ед.": []}
cont = 'y'
count = 0

while cont.lower() != 'n':
    count += 1
    print(f'Введите характеристики товара №{count}')
    current_feature = features.copy()
    for f in features.keys():
        current_feature[f] = input(f'{f}:')
        analytic[f].append(current_feature[f])
    items.append((count, current_feature))
    cont = input('Продолжить ввод товаров?(y/n):')

print(items)
print(analytic)
