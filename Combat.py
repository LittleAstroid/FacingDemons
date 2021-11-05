import GUI
import random

def showstatus(player_object, enemy_object):

    GUI.linebreak(25)
    GUI.separetelines(player_object.name, enemy_object.name)
    GUI.separetelines('', '')
    GUI.lseparatelines(f'{player_object.health} / {player_object.max_health} HEALTH',
                       f'{enemy_object.health} / {enemy_object.max_health} HEALTH')
    GUI.lseparatelines(f'{player_object.dread} / 100 DREAD', '')
    GUI.separetelines('', '')
    GUI.linebreak(25)
    return GUI.choose(['Attack', 'Item', 'Run'])


def battle(player_object, enemy_object):

    is_over = False
    while not is_over:

        dec = showstatus(player_object, enemy_object)

        # If the player has 2 times the agility of the enemy, he will act two turns in a row and so on.
        if player_object.initiative >= enemy_object.initiative:
            for c in range(0, int(round((player_object.agility / enemy_object.agility)))):

                # player attacks
                player_object.update()

                if dec == 1:
                    damage, has_hit, is_crit = player_object.damage(enemy_object.defence, enemy_object.agility)

                    if not has_hit and not is_over:
                        GUI.linebreak(25)
                        print('You have missed!')
                        if player_object.dread > 50:
                            print('What a failure. . .')
                            player_object.dread += random.randint(5, 10)
                    else:
                        if is_crit and not is_over:
                            GUI.linebreak(25)
                            print('Critical hit!\n'
                                  'Not so bad. . .')
                            print(f'You hit {enemy_object.name} for {damage} damage!')
                            enemy_object.health -= damage
                            player_object.dread -= damage / 2
                        elif not is_crit and not is_over:
                            print(f'You hit {enemy_object.name} for {damage} damage!')
                            enemy_object.health -= damage
                    input()

                # player uses item
                if dec == 2:
                    GUI.showinventory()

                # players attempts to flee
                if dec == 3:
                    success = player_object.agility - enemy_object.agility + random.randint(-10, 10)

                    if success >= enemy_object.initiative * 1.25:
                        print("You've managed to escape!\n"
                              "What a coward. . .")
                        player_object += random.randint(5, 10)
                        input()
                        is_over = True
                        break

                # Checks if player's last attack killed the enemy.
                if enemy_object.health <= 0:
                    print(f'{enemy_object.name} is down!')
                    input()
                    is_over = True
                    break

            # Enemy's turn
            damage, has_hit, is_crit = enemy_object.damage(player_object.defence, player_object.agility)

            if not has_hit and not is_over:
                print(f'{enemy_object.name} has missed you!')
            elif is_crit and not is_over:
                print(f'Critical hit!')
                player_object.dread += damage / 2
                print(f'{enemy_object.name} has hit you for {damage} damage!')
                player_object.health -= damage
            elif not is_crit and not is_over:
                print(f'{enemy_object.name} has hit you for {damage} damage!')
                player_object.health -= damage
            input()

            if player_object.health <= 0:
                print(f'You are down!\n'
                      f'Hopeless loser. . .')
                input()
                is_over = True
                break

            player_object.pushgamestate()

        else:

            # If the enemy has 3 times the agility of the player, he acts 3 times in a row and so on.
            for c in range(0, int(round(enemy_object.agility / player_object.agility))):
                damage, has_hit, is_crit = enemy_object.damage

                if not has_hit:
                    print(f'{enemy_object.name} has missed you!')
                elif is_crit:
                    print(f'Critical hit!')
                    player_object.dread += damage / 2
                    print(f'{enemy_object.name} has hit you for {damage} damage!')
                    player_object.health -= damage
                else:
                    print(f'{enemy_object.name} has hit you for {damage} damage!')
                    player_object.health -= damage
                input()

                if player_object.health <= 0:
                    print(f'You are down!\n'
                          f'Hopeless loser. . .')
                    input()
                    is_over = True
                    break

                player_object.pushgamestate()

            # player attacks
            player_object.update()

            if dec == 1:
                damage, has_hit, is_crit = player_object.damage()

                if not has_hit:
                    GUI.linebreak(25)
                    print('You missed!')
                    if player_object.dread > 50:
                        print('What a failure. . .')
                        player_object.dread += random.randint(5, 10)
                else:
                    if is_crit:
                        GUI.linebreak(25)
                        print('Critical hit!\n'
                              'Not so bad. . .')
                        print(f'You hit {enemy_object.name} for {damage} damage!')
                        enemy_object.health -= damage
                        player_object.dread -= damage / 2
                    else:
                        print(f'You hit {enemy_object.name} for {damage} damage!')
                        enemy_object.health -= damage
                input()

                if enemy_object.health <= 0:
                    print(f'{enemy_object.name} is down!')
                    is_over = True
                    input()
                    break

            # player uses item
            if dec == 2:
                GUI.showinventory()

            # players attempts to flee
            if dec == 3:
                success = player_object.agility - enemy_object.agility + random.randint(-10, 10)

                if success >= enemy_object.initiative * 1.25:
                    print("You've managed to escape!\n"
                          "What a coward. . .")
                    player_object += random.randint(5, 10)
                    is_over = True
                    input()
                    break
