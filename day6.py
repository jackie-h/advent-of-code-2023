def day6(races):
    print('Day 6: Wait For It')

    result = 1

    for (t,d) in races:
        print('race',t,d)
        wins = 0
        start_speed = 1
        rd = d + t
        print(rd / t , int(rd / t))
        start_speed = int(rd / t)
        print('start speed', start_speed)
        while start_speed < t and wins == 0:
            distance = (t-start_speed) * start_speed
            print(start_speed, distance)
            if distance > d:
                wins += 1
            else:
                start_speed += 1
        first_win = start_speed

        # wins = 0
        # start_speed = t - 1
        # while wins == 0:
        #     distance = (t - start_speed) * start_speed
        #     print(start_speed, distance)
        #     if distance > d:
        #         wins += 1
        #     else:
        #         start_speed -= 1

        last_win = t - first_win
        print('wins', first_win, last_win)
        total_wins = (last_win - first_win) + 1
        print('total wins', total_wins)
        result = result*total_wins
    print(result)
    return result


if __name__ == '__main__':
    races_test = [(7,9),(15,40),(30,200)]
    assert day6(races_test) == 288

    races = [(51,377),(69,1171),(98,1224),(78,1505)]
    assert day6(races) == 131376

    races_test2 = [(71530,940200)]
    assert day6(races_test2) == 71503

    races2 = [(51699878,377117112241505)]
    #assert day6(races2) == 34123437

#d = s * (t - s)
#d = s*t - s^2

