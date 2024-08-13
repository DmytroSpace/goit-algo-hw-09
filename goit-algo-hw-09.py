import timeit

def find_coins_greedy(sum, coins):                          # Функція жадібного алгоритму для підбору монет
    coins_count = {}                                        # Створюємо порожній словник 
    for coin in coins:                                      # Перебираємо монети, починаючи з найбільшого номіналу
        count = sum // coin                                 # Рахуємо, скільки разів можна взяти поточну монету
        if count > 0:
            coins_count[coin] = count                       # Запам'ятовуємо кількість разів використання
        sum -= coin * count                                 # Зменшуємо суму на кількість разів
        if sum == 0:                                        # Щойно сума для решти дорівнює 0 -> зупиняємо цикл
            break
    return coins_count

def find_min_coins(sum, coins):                             # Функція динамічного програмування    
    min_coins = [float('inf')] * (sum + 1)                  # Ініціалізуємо список для зберігання мінімальної кількості монет для кожної суми
    min_coins[0] = 0
    
    coin_count = [{} for _ in range(sum + 1)]               # Ініціалізуємо список для зберігання кількості монет для кожного номіналу
    
    for coin in coins:                                      # Перебираємо всі доступні монети
        for x in range(coin, sum + 1):                      # Знаходимо всі можливі суми від номіналу монети до заданої суми
            if min_coins[x - coin] + 1 < min_coins[x]:      # Перевіряємо, чи можна зменшити кількість монет для поточної суми за допомогою цієї монети
                min_coins[x] = min_coins[x - coin] + 1      # Оновлюємо кількість мінімальних монет для поточної суми    
                coin_count[x] = coin_count[x - coin].copy()
                coin_count[x][coin] = coin_count[x].get(coin, 0) + 1
    
    return coin_count[sum]

if __name__ == '__main__':
    cases = [([50, 25, 10, 5, 2, 1], 113)]                  # Визначаємо наш кейс: набір монет і сума
    functions = [find_coins_greedy, find_min_coins]         # Наші функції для перевірки

    for coins, cash_amount in cases:
        print(f"\n\tCase for {coins} and sum: {cash_amount}")
        for fun in functions:
            time = timeit.timeit(lambda: fun(cash_amount, coins), number=10000)
            print("Result for {}: {}".format(fun.__name__, fun(cash_amount, coins)))
            print("Time taken for {}: {:.6f} seconds".format(fun.__name__, time))
