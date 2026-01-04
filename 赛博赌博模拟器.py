import random
import time


print('\n' + '='*30)
balance = 2000
while balance> 0:
    print(f'当前余额：{balance}元')
    while True:
        n = int(input('投多少注？(输入0退出)'))
        if n == 0:
            print('感谢游玩，少侠再来')
            exit()
        elif 0< n*5 <= balance:
            break
        else:
            print(f'余额不足！你最多只能买{balance//5}注')
#购买
    balance -= n*5
    all_tickets = []
    for piece in range(1, n + 1):
        selected_red = sorted(random.sample(range(1, 36), 5))
        selected_blue = sorted(random.sample(range(1, 13), 2))
        all_tickets.append([selected_red, selected_blue])
        if n<=10:
            print(f'第{piece:0>2d}注', end=' ')
            for r in selected_red: print(f'\033[031m{r:0>2d}\033[0m', end=' ')
            for b in selected_blue: print(f'\033[034m{b:0>2d}\033[0m', end=' ')
    if n > 10: print(f'已购买{n}注，等待开奖')
#开奖
    print('\n' + '='*30)
    print('正在开奖，请稍后...', end='')
    for _ in range(3):
        time.sleep(0.3)
        print('.', end=' ', flush=True)
    win_red = sorted(random.sample(range(1, 36), 5))
    win_blue = sorted(random.sample(range(1, 13), 2))
    print('\n' + '='*30)
    print('中奖号码为：', end=' ')
    for w_r in win_red:
        time. sleep(0.3)
        print(f'\033[031m{w_r:0>2d}\033[0m', end=' ')
    for w_b in win_blue:
        time. sleep(0.3)
        print(f'\033[034m{w_b:0>2d}\033[0m', end=' ')
    print('\n' + '='*30)
    print('----兑奖结果----')
    special_prize = 0    # 特等奖
    second_prize = 0     # 二等奖
    not_bad = 0          # 还行
    too_bad = 0          # 太拉了
    current_win_money = 0
    for i, ticket in enumerate(all_tickets, 1):
        my_red, my_blue = ticket[0], ticket[1]
        red_hits = len(set(my_red) & set(win_red))
        blue_hits = len(set(my_blue) & set(win_blue))
        if red_hits == 5 and blue_hits == 2:
            special_prize += 1
            current_win_money += 1000000
        elif red_hits == 3 and blue_hits == 1:
            second_prize += 1
            current_win_money += 600
        elif red_hits + blue_hits >= 3:
            not_bad += 1
            current_win_money += 45
        else:
            too_bad += 1

#余额更新
    print('\n' + '='*30)
    print(f'【特等奖】：{special_prize} 注')
    print(f'【二等奖】：{second_prize} 注')
    print(f'【一等奖】：{not_bad} 注')
    print(f'【没中奖】：{too_bad} 注')
    print(f'赢得奖金{current_win_money}元')
    print('\n' + '='*30)
    balance = balance + current_win_money
print(f'破产咯')