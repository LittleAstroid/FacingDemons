# Links. To which rooms each room links.
# Eventually this will be changed for a outside file.

links = {'bed': {'bedroom'}, 'bedroom': {'corridor'}}
from textwrap import dedent


def linebreak(n):
    print('=-' * n)


col = {'bla': '\033[1;30m', 'red': '\033[1;31m', 'gre': '\033[1;32m',
       'yel': '\033[1;33m', 'blu': '\033[1;34m', 'mag': '\033[1;35m',
       'cya': '\033[1;36m', 'whi': '\033[1;37m', 'cls': '\033[m'}
prompt = '> '


def gui(player_object):
    linebreak(25)
    print(f'{player_object.name:^25}')
    linebreak(25)


def readnum(n):
    cont = 0
    while True:
        try:
            dec = int(input(prompt))
        except (ValueError, TypeError):
            print(f"{col['red']}Invalid entry.{col['cls']}")
            cont += 1

            if cont >= 5:
                return 0
        else:
            if 0 <= dec <= n:
                return dec
            else:
                print(f"{col['red']}Invalid choice.{col['cls']}")
                continue


def choose(choices):
    cont = 1
    for c in choices:
        print(f'[ {cont} ] - {c}')
        cont += 1

    dec = readnum(cont - 1)
    return dec


def itemdesc(item_name):
    import csv
    file = open('item_list.csv', newline='\n')
    reader = csv.reader(file, delimiter=';')

    for line in reader:
        if line[0] == item_name:

            if line[2] == 'wea':
                linebreak(15)
                print(f'{line[0]:^30}')
                linebreak(15)
                print(line[5])
                print(f'Attack bonus: +{line[3]}\n'
                      f'Defence bonus: +{line[4]}')
                linebreak(15)
                dec = choose(['Equip', 'Quit'])

                if dec == 1:
                    gamestate = open('gamestate')
                    contents = gamestate.read()
                    contents = contents.split()
                    contents[2] = line[0]
                    contents = '\n'.join(contents)

                    gamestate.close()
                    gamestate = open('gamestate', 'w')
                    gamestate.write(contents)
                    gamestate.close()

                else:
                    return None

            elif line[2] == 'con':
                print(f'{line[0]:^15}')
                print(line[5])

                if int(line[3]) > 0:
                    print(f'Heals {line[3]} health points')
                elif int(line[3]) < 0:
                    print(f'Lowers {line[3].replace("-", "")} health points')

                if int(line[4]) < 0:
                    print(f'Lowers {line[4].replace("-", "")} dread points')
                elif int(line[4]) > 0:
                    print(f'Raises dread by {line[4]}')

                linebreak(15)
                dec = choose(['Use', 'Quit'])

                if dec == 1:
                    gamestate = open('gamestate')
                    contents = gamestate.read()
                    contents = contents.split()
                    contents[4] += line[4]
                    contents[5] += line[3]
                    contents = '\n'.join(contents)

                    gamestate.close()
                    gamestate = open('gamestate', 'w')
                    gamestate.write(contents)
                    gamestate.close()

                else:
                    return None


def showinventory():
    linebreak(25)
    print(f'{"Inventory":^50}')
    linebreak(25)

    inventory = open('inventory.csv')
    cont = 0
    items = []
    for line in inventory.readlines():
        cont += 1
        items.append(line.replace('\n', ''))

    items.append('Exit')
    items.append('Examine status')

    dec = choose(items)

    if dec == (cont + 1):
        return 0
    else:
        itemdesc(items[dec - 1])


# Automates the return of room names. Room names are always after the first two options and extra options come after
# them. If player chooses somewhere in between 2 and the last room option, this will automatically return the name.
def navigate(links, *extra):
    print('[ 1 ] - Analyse inventory\n'
          '[ 2 ] - Analyse surroundings')

    cont = 3
    for c in links:
        print(f'[ {cont} ] - Enter {c}')
        cont += 1
    roomceil = cont - 1

    for c in extra:
        print(f'[ {cont} ] - {c}')
        cont += 1

    dec = readnum(cont - 1)

    if dec == 1:
        showinventory()

    if dec == 2:
        return 2

    if 3 <= dec <= roomceil:
        match = 3

        for c in links:
            if dec == match:
                return c
            match += 1


def readroomdesc(name):
    text = open('room_desc')
    start_tag = str(name).upper() + '_START'
    end_tag = str(name).upper() + '_END'

    body = text.read()
    start_index = len(name) + 7 + body.find(start_tag)
    end_index = body.find(end_tag) - 1

    linebreak(15)
    print(dedent(body[start_index:end_index]))
    linebreak(15)

    text.close()


def separetelines(left, right):
    print(f'{left:^25}| {right:^24}')


def lseparatelines(left, right):
    print(f'{left:<25}| {right:<24}')
