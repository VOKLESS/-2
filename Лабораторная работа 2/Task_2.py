from calendar import month

money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

bud = money_capital + salary
month = 1

while bud > spend:
    if month != 1:
        spend = spend * (increase+1)
        #print(f" Бюджет на {month} месяц: {bud}; Расходы в текущем месяце: {spend}")
        bud = (bud + salary) - spend
        month += 1
    elif month == 1:
        #print(f" Бюджет на {month} месяц: {bud}; Расходы в текущем месяце: {spend}")
        bud = (bud + salary) - spend
        month += 1



print ("Количество месяцев, которое можно протянуть без долгов:", month-1)
