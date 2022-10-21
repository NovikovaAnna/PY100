def count_month(money_capital, spend, month=0):
    """ Расчет месяцев на фин.подушку и зп"""
    while money_capital >= spend:
        money_capital += salary - spend
        month += 1
        spend *= 1 + increase

    print(month)

money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
count_month(money_capital, spend)



