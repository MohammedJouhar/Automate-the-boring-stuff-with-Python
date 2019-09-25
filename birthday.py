# this code helps to maintian birthday day tracker, code asked user ask to input name and this will search in the dictionaries we created
# if thier name not available this will add to the dictionaries

birthday = {'jouhar': '13th March', 'zebu': '20th September', 'fathima': '11th Jan'}

while True:
    print('Type your name , in small letters only (& leave blank to quit)')
    name = input()

    if name in birthday:
        print('birthday of ' + name + ' is ' + birthday[name])

    elif name == '':
        break

    else:
        print('I dont have birthday information of ' + name)
        print('Type what his/her birthday ?')
        bday = input()
        birthday[name] = bday # this is to add , same as append
        print('Birthday database updated')


