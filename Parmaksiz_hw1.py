#Parmaksiz Leonid
#Задача 1


#В Вышке научились измерять душевную боль... (Это правда: Источник)
# определитель душевной боли

a = float(input('Оцените силу вашей душевной боли по шкале от 0 до 10: '))
if a < 0.7:
    print('Кажется, вы испытываете легкое огорчение. Как человек в короткой поездке в метро, забывший дома наушники')
elif 0.7 <= a <= 4.2:
    print('Вы встревожены - почти как человек, которому придется звонить по телефону, и это в эпоху мессенджеров! То самое чувство, когда начинаете нервно репетировать в голове диалог...')


#Solution  1

self_pain = int(input('Оцените силу вашей душевной боли целым числом по шкале от 0 до 10: '))
if self_pain < 1:
    print('Рад за вас! Можете ущипнуть себя чтобы вспомнить, что такое боль :-)')
elif 1 <= self_pain <= 3:
    print('Вы встревожены - почти как человек, которому придется звонить по телефону, и это в эпоху мессенджеров!')
elif 4 <= self_pain <= 6:
    print('Ого! Ничего не говори, это жжет огонь в груди. Срочно отрпавтесь развеятся в караоке или выговориться!')
elif 7 <= self_pain <= 9:
    print('Это уже серьезно.Вам сейчас сложно, понимаю. Но не забывайте что и это пройдет')
elif 10 <= self_pain :    
    print('Шутки в сторону! Срочно позвоните друзьям и обратитесь к специалисту! (тем не менее надеюсь вы пошутили и просто слишком устали)')  

# Using fucnction
def pain_assesment(pain):
    if pain < 1:
      print('Рад за вас! Можете ущипнуть себя чтобы вспомнить, что такое боль :-)')
    elif 1 <= pain <= 3:
      print('Вы встревожены - почти как человек, которому придется звонить по телефону, и это в эпоху мессенджеров!')
    elif 4 <= pain <= 6:
      print('Ого! Ничего не говори, это жжет огонь в груди. Срочно отрпавтесь развеятся в караоке или выговориться!')
    elif 7 <= pain <= 9:
      print('Это уже серьезно.Вам сейчас сложно, понимаю. Но не забывайте что и это пройдет')
    elif 10 <= pain :    
      print('Шутки в сторону! Срочно позвоните друзьям и обратитесь к специалисту! (тем не менее надеюсь вы пошутили и просто слишком устали)')  
#test
pain_assesment(-4)
pain_assesment(11)
pain_assesment(5)


#task 2

#Поработаем с шуточными предсказаниями для абитуриентов студентов
#В hse_prediction должны храниться короткие предсказания, 
hse_prediction = [
    ['Слушайте каждого. Идеи приходят отовсюду.'],
    ['Скоро контрольная точка по нелюбимому предмету('],
    ['В новом году обещаю себе смотреть не больше трех серий сериала за раз'],
    ['Угостите преподавателя конфеткой!'],
    ['Хорошие новости придут к вам по  Яндекс почте.'],
    ['Что ни делается - все к лучшему, и даже первая пара, ожидающая Вас в обновлённом расписании.'],
    ['Делайте то, чего просит душа и тело - не идите на пары!'],
    ['Пора собирать чемоданы: Вас ждет экспедиция на Сахалин!'],
    ['Пришло время сдать все долги.'],
    ['Вы не получите автомат по физре в следующем полугодии.'],
    ['В новом году обещаю себе спать'],
    ['Если вы ждали знака - то ВОТ ОН! Срочно участвуйте в ближайшей конференции!'],
    ['Вам повысят стипендию на 1000 рублей в этом году.'],
    ['Ураааааааааааа! Завтра одни только  лекции!'],
    ['Все лучшее происходит,когда Вас нет на паре!'],
    ['На мобильность только в Питер'],
    ['В новом году обещаю себе защитить диссертацию'],
    ['В новом году обещаю себе запомнить имена одногруппников'],
    ['Через час Вы снова проголодаетесь. Шоколад можно найти в магазине.']
        ]
        

# Solution 2
import random
pred2=hse_prediction
rem_ny = [['В новом году обещаю себе смотреть не больше трех серий сериала за раз'], ['В новом году обещаю себе спать'],['В новом году обещаю себе защитить диссертацию'],['В новом году обещаю себе запомнить имена одногруппников']]
 
for i in rem_ny:
  pred2.remove(i)

print(pred2)
print(*random.choice(hse_prediction))

#task 3 

#Алиса коллекционирует открыткм, которые она получила из разных стран от друзей. 
#Сейчас ее архив выглядит вот так:

postcards = {
    "Maria": "London",
    "Lorenzo": "Milan",
    "Oleg": "Canberra",
    "Hans": "Calgary",
    "Mark": "Milan",
    "Alex": "Krakow",
    "Julia": "Murmansk"

}

#Однажды Алиса показала Вам свою бумажную коллекцию, и Вы заметили неточности:
#1. В архиве не хватает двух открыток: от Петры из Парижа и от Ивана из Москвы. Добавьте их в архив Алисы.
# 2. Открытка, присланная Олегом на самом деле не из Канберры, а из Сиднея. Исправьте город на верный, изменив значение по ключу в словаре.
# 3 Алиса говорит, что в ее коллекции более 10 уникальных городов. 


# Solution 3
print(postcards,type(postcards)) 

#lost
lost_cards= {
  "Petra":"Paris",
  "Ivan":"Moscow"}

# check-add-check
print(postcards)
postcards.update(lost_cards)
print(postcards)

#error fix
print(postcards.keys())
postcards['Oleg'] = "Sidney"
print(postcards)

#unique
postcards.values()
card_cities=set(postcards.values())
print(len(card_cities))

#compare
postcards.values()
print(card_cities)

#final
len(card_cities)
print(*card_cities)

