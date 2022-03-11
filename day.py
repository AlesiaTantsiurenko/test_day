def days(day):
    """
    Функция вычисляет следующий день недели.
    :param day: название дня недели.
    :return: название следующего дня недели.
    """
    list = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    if day.title() in list:
        if list.index(day.title()) == (len(list) - 1):
            return list[0]
        else:
            s = list.index(day.title())
            return list[s + 1]
    else:
        raise ValueError("Нет такого дня недели!")


def main():
    while True:
        day = input('Введите день недели (слово) ')
        next_day = None
        try:
            next_day = days(day)
        except ValueError:
            print('Нет такого дня недели!')
            print()
            continue
        print('День, который следует за ', day.title(), ':', next_day)
        break


main()
