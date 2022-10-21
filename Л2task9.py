def counting_money(salary, spend, months, inctease, need_money = 0):
    """ Расчет месяцев на текущий бюджет"""
    for money in range(months):
        if money > 0:
            spend *= 1 + inctease
        need_money += spend - salary

    print(round(need_money))

salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

counting_money(salary, spend, months, increase)



