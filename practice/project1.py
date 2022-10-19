 while 1:
        score0 += take_turn(strategy0(score0, score1), score1, dice)
        if abs(take_turn(strategy0(score0, score1), score1, dice) - strategy0(score0, score1)) == 2:
            score0 += 3
        if score0 >= goal:
            if is_swap(score0, score1):
                score0, score1 = score1, score0
            break
        score1 += take_turn(strategy1(score1, score0), score0, dice)
        if abs(take_turn(strategy1(score1, score0), score0, dice) - strategy1(score1, score0)) == 2:
            score1 += 3
        if is_swap(score1, score0):
                score0, score1 = score1, score0
        if score1 >= goal or score0 >= goal:
            break
#最开始写的problem5 的代码，又臭又长还一个变量用到底，
#理解题意不到位，回合制的正确写法要了解
