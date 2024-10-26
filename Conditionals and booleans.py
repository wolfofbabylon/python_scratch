language = input('Enter ProgLang : ')

progLang = ['Python', 'Java', 'C++']
Lang = ['English', 'Hindi', 'Spanish']


if (language in progLang):
    print('This a prog lang')

elif (language in Lang):
    print('This is language') 

else :
    print('Please enter a valid language!')