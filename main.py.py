#count = 0

#while count != 10:
    #count = count+ 1
    #print(count)

#for i in range(10, 0, -1):
    #print(i)
#print('Поехали!')

#num=int(input("введите столбец"))
#for i in range(1, 10):
    #c = i * num
    #print(i, "*", num, '=', c)

#name = input("введите имя")
#lastname = input ("введите фамилию")
#age = int(input("возраст"))


#if age > 18:
    #print("Ты уже взрослый!")
#else:
    #print("ТЫ ещё ребенок")
    
#for g in range(1, 10):
    #print("\n")
    #for i in range(1, 10):
      #print(i, "*", g, "=", g*i)

#i=0
#str='pointpoint'

#while i < len(str):
    #if str[i] == 'o' or str[i] == 't':
        #i += 1
        
    #print('sdawaw:', str[i])
    #i+=1


#while True:
    #answ=int(input('введите число:'))
    #if answ == 'exit':
        #break
    
    #trnum=5

    #tmp=int(answ)
    
    #if tmp>5:
        #print('меньше')
    #elif tmp<5:
        #print('больше')
    #elif tmp==5:
        #print('Ура')
    
    
#print(input().split())

#spi=str()

#while True:
    #if len(spi)==10:
        #break
    #else:
        #print('введите 10 чисел')
    #spi=input().split()
    #spi=list(map(int, spi))

#min=int()

#for i in range(len(spi)):
    #a=spi[0]
    #b=spi[i]
    #if a > b:
        #min=b
        #a=b
    #else:
        #min=a
#print(min)

#weekdays=['пон', 'втор']
#weekdays.insert(2, 'сред')=добвалять
#print(weekdays)

#weekdays.pop(1)=выводит, удаляет
#del=удаляет
#.extend=объеденяет
#mon, *_
#sorted=сортирует
#str_list=[]
#joined_str=''.join(str_list)

#nums_=[2, 2, 3, 4, 55,3]

#print(nums_.count(2))
#.lower()=уменьшает
#.starrwith('A')
#add=добавить в множест
#update=добавить
#.remove=удалить
#len=размер узнать
#.issubset =узнать подмножество ли иножества
#set=множества
#nlp= set([1, 2])
#cv= set([4, 5,])
#print(nlp-cv)
#~=возведение в степень

#tup=(1, 2, 3, 5, 5)
#print(tup)
#lst=list(tup)
#lst[3]=4
#tup=tuple(lst)

#tup=(1, 2, 2, 4, 5, 6, 6, 7, 6, 8)

#result=list()

#for i in tup:
    #if tup.count(i)>1:
        #result.append([i, tup.count(i)])

#print(result)

#def summa(num1, num2):
    #res=num1+num2
    #return res



#tup1=(1, 2, 2, 4, 5, 5, 2, 6)
#s=summa(2, 5)
#dt={(1+2):3, 1:3}
#print()
#de['']=de=словарь
#dic={(1, 2) : 'jjj', 'бежать' : 2}
#dic.update({1 : '1+1',
             #'бежать' : 4})
#print(dic)
#get=достать
#keys=коллекцию ключей извлекает
#values=коллекцию значений
#items=выводит словарь, но по отдельности
#dict=словарь
#append=добавляет в список
#num=[0]*8
#for i in range(1):
    #print([num]*2)
#n, m=map(int, input('Введи колво строк и колво сим. в строке').split())

#a=[]
#for i in range(n):
    #a.append(list(map(int, input().split())))
#print(a)
#z=[[1, 2, 3], [4, 5, 6]]
#for i in range(len(z)):
    #print(*z[i])


#n=int(input('Введите число'))
#m=int(input('введите число'))

#%s=строка
#%d=число
#format= для строк {}
#f={name}
#стек=LIFO
#randint=для случайных чисел
#import random
#print(random.randint(27,564))
#randrange=для шага
#import random
#print(random.randrange(0, 10, 3))
#random=для плав. точки
#import random
#print(random.random())
#uniform=для диопазона 
#import random
#print(random.uniform(3.4, 5.5))
#choice=рандом из списка
#random.shuffle=для перемешки
#random.sample(tr, 4)=из списка выбирает 4 чила на рандоме
#random.seed=рандом от заданного числа
#import random
#random.seed(a=None, wersion=2)
#-=разность во множетсве

#text = 'lorem ipsum dolor sit amet amet amet'
#text = text.split()
#max=0
#for i in text:
    #if max>len(i):
        #max=len(i)
#for i in text:
    #if len(i)==max:
        #print(i)
#d={'pi':3.14, 'e':2.71, 'fi':1.62}
#for value in d.values():
    #if value>2.5:
        #print(value)


#s=input('введите предложение:')
#count=0
#Vowel_letters=set('ёуеыаоэяию')
#for letters in s:
    #if letters in Vowel_letters:
        #count+=1
#print("Количество гласных равно:")
#print(count)
#Question=input("Кто разработал Пайтон?:")
#while Question:
    #if Question!="Гвидо ван Россум":
        #print("no")
       # break
    #elif Question=="Гвидо ван Россум":
        #print("Правильно!")
    

#from tkinter import*
#root=Tk()
#root.title('приложение')
#root.geometry('500x200')
#label(text='s').pack()
#Entry=
#Button=
#root.mainloop()
#from tkinter import*
#def button_l():
    #l['text']=str(int(a.get())*2)
#root=Tk()
#root.title('Приложение')
#root.geometry('500x400')
#a=Entry(root, width=15, bg='black', fg='cyan', font='consolas')
#Wa.pack()
#Button(root, text='умножить на 2', width=15, height=2, bg='white', command=button_l).pack()
#l=Label(root, width=15, bg='black', fg='cyan', font='consolas')
#l.pack()
#root.mainloop()

#from tkinter import*
#from tkinter import messagebox

#def button_1():
    #messagebox.showinfo('Результат', int(a.get())*int(b.get()))
#def button_2():
    #messagebox.showinfo('Результат', int(a.get())+int(b.get()))
#root=Tk()
#root.title('Приложение')
#root.geometry('500x300')
#b=Entry(root, width=10, bg='white', fg='red', font='consolas')
#b.pack()
#a=Entry(root, width=10, bg='white', fg='red', font='consolas')
#a.pack()
#Button(root, text='*', width=10, height=2, bg='white', command=button_1).pack()
#Button(root, text='+', width=10, height=2, bg='white', command=button_1).pack()
#root.mainloop()
#eval('89*23')
       
#from tkinter import*
#import random

#score, max_score=0, 20
#size_x, size_y=1280, 700

#def put():
    #global b

    #b=Button(root, text='Нажми', activebackground='red', command=click)
    #b.place(x=random.randint(10, size_x), y=random.randint(2, size_y))

#def click():
    #global score
    #b.destroy()
    #if score<=max_score:
        #score+=1
        #put()
    #else:
        #Label(root, text='Поздравляем\n Вы выйграли').place(relx=0.5, rely=0.5)

#root=Tk()
#root.title('Игра')
#root.geometry(f'{size_x}x{size_y}')
#root.resizable(False, False)
#put()
#root.mainloop()

#from tkinter import *
#import random

#btns = [
#"C", "DEL", "*", "=",
#"1", "2", "3", "/",
#"4", "5", "6", "+",
#"7", "8", "9", "-",
#"(", "0", ")", "X^2"
#]

#def set_value(formula):
    #if formula == '':
        #lbl['text']='0'
    #else:
        #lbl['text'] = str(eval(formula))


#def logicalc(operation):
    #if operation == "C":
        #set_value('')
    #elif operation == "DEL":
        #set_value(lbl['text'][0:-1])
    #elif operation == "X^2":
        #set_value(str((eval(lbl["text"]))**2))
    #elif operation == "=":
        #set_value(lbl["text"])
    #else:
        #if lbl['text'] == "0":
            #lbl["text"] = ""
        #lbl["text"] = lbl['text']+operation

#root = Tk()
#root["bg"] = "black"
#root.geometry("485x550+200+200")
#root.title("Калькулятор")
#root.resizable(False, False)
#lbl = Label(text='0', font=("Consolas", 21, "bold"), bg="black", foreground="white")
#lbl.place(x=11, y=50)
#x = 10
#y = 140
#for bt in btns:
    #com = lambda x=bt: logicalc(x)
    #b = Button(root, text=bt, bg="white", font=("Consolas", 15), command=com).place(x=x, y=y, width=115,  heigh=79)
    #x += 117
    #if x > 400:
        #x = 10
        #y += 81

#root.mainloop()

#import time
#import math, os
#print(math.cos(3.14))
    
#from roman import *

#t = ['IV', 'LVIII', 'MCMXCIV', 'XCIX', 'LXXX', 'LXIX']

#print(t)

#for i in t:
    #print(i, '->', roman_to_int(i))
    #a=[4, 58, 1994, 26, 99, 69, 80]

#for i in a:
    #print(i, '->',int_to_roman(i))

#'r'-чтение

def read_from_file(filename):
    file = open(filename, 'r')
    names = tuple(file.readline()[:-1].split(','))
    data = []
    for line in file:
        line = line.split(',')
        data.append((int(line[0]), str(line[1]), line[2], int(line[3]), int(line[4]), line[5][:-1]))
    names_str = ''.join([str(each).ljust(15) for each in names])
    print(names_str)
    for tup in data:
        tup_str = ''.join([str(each).ljust(15) for each in tup])
        print(tup_str)
    return names, data


#def delete_from_file(file_name, names, data):
    
    
    


def new_data(file_name):
    new_data = []
    file = open(file_name, 'a')
    i = 0
    while i <= 5:
        new = input()
        new_data.append(new)
        i += 1
    file.write(','.join(new_data) + '\n')


names, data = read_from_file('C:\Users\Пользователь\AppData\Local\Programs\Python\Python311')
print("Ввести данные?")
print("1) Yes")
print("2) No")
answer = input()
if answer == '1':
    new_data('data.csv')
else:
    print("Удалить данные?")
    print("1) Yes")
    print("2) No")
    answer = input()
    if answer == '1':
        delete_from_file('C:\Users\Пользователь\AppData\Local\Programs\Python\Python311', names, data)
    else:
        exit()
