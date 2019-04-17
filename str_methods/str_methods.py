name = 'Swaroop' #Это объект строки
if name.startswith('Swa'):
    print('Да строка начинается на "Swa"')
if 'a' in name:
    print('Да строка содержит "a"')
if name.find('war') != -1:
    print('Да, строка содержит фрагмент "war"')
razdelitel = '_*_'
mylist = ['Бразилия','Россия','Индия','Китай']
print(razdelitel.join(mylist))
