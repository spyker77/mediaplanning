# Чтобы использовать эту модель, на компьютере должен быть установлен язык программировани Python, который можно скачать отсюда: https://www.python.org/downloads/
# Дальше, открываешь приложение "Терминал" в утилитах и доустанавливаешь следующие пакету через команды:
# 1) pip3 install numpy
# 2) pip3 install beautifultable
# Затем переходишь в папку (в самом терминале), в которой лежит файл months.py
# Чтобы запустить оценку, введи комманду и нажми Enter: python3 months.py
# Следуй инструкциям и наслаждайся 🍹

import re
import numpy
import datetime
import calendar
from beautifultable import BeautifulTable

INCREASE_FOR_CREATIVES = 1.3
INCREASE_FOR_RATING = 1.1
INCREASE_FOR_PUSH = 1.6
INCREASE_FOR_PUSH_VOLUME = 3
INCREASE_FOR_SIZE_ANDROID_100_500 = 1.1
INCREASE_FOR_SIZE_IOS_150_500 = 1.1
INCREASE_FOR_SIZE_500_1000 = 1.2
INCREASE_FOR_SIZE_OVER_1000 = 1.3
INCREASE_FEBRUARY_NOVEMBER = 1.3
INCREASE_DECEMBER = 2

VOLUME_COEFFICIENTS = {
        "Facebook": 1,
        "Google": 1.17,
        "myTarget": 1.10,
        "In-App": 1.23,
        "Видеосети": 0.93,
        "Twitter": 0.23,
        "Snapchat": 0.47,
        "Яндекс": 0.73,
        "ВКонтакте": 0.60,
        "ASA": 0.53
    }

BUDGET_BOTTOM = {
        "Facebook": 1500,
        "Google": 1500,
        "myTarget": 1000,
        "In-App": 1000,
        "Видеосети": 1500,
        "Twitter": 3000,
        "Snapchat": 2000,
        "Яндекс": 1000,
        "ВКонтакте": 1000,
        "ASA": 2000
    }


class App:

    android_rates = {
        "Facebook": 1,
        "Google": 1,
        "myTarget": 0.95,
        "In-App": 0.9,
        "Видеосети": 1.15,
        "Twitter": 1.1,
        "Snapchat": 0.95,
        "Яндекс": 1,
        "ВКонтакте": 0.9
    }

    ios_rates = {
        "Facebook": 1,
        "Google": 1.07,
        "myTarget": 0.95,
        "In-App": 0.9,
        "Видеосети": 1.15,
        "Twitter": 1.1,
        "Snapchat": 0.95,
        "Яндекс": 1,
        "ВКонтакте": 0.9,
        "ASA": 1.5
    }

    def select_platform(self):
        # Limit the range of platforms if there is no need to count both.
        print("\nПриступим к оценке приложений? 😜")
        print("\n1) Давай сразу определимся с тем, сколько платформ будем считать:")
        print("– если только Android, то поставь 0")
        print("– если только iOS, то поставь 1")
        print("– если Android и iOS, то поставь 2")

        while True:
            platform = int(input("Будем считать -> "))

            if platform == 0:
                android_platform = True
                ios_platform = False
            elif platform == 1:
                android_platform = False
                ios_platform = True
            elif platform == 2:
                android_platform = True
                ios_platform = True
            else:
                print("Похоже кто-то ошибся с ответом. Повторим? 😉")
                continue

            return android_platform, ios_platform

    def choose_model(self):
        # Correct rates and volumes according to the CPA model if necessary.
        android_platform, ios_platform = self.select_platform()
        print("\n2) Давай укажем модель работы, к которой рекламодатель привязал KPI?")
        print("– если CPM, то поставь 1")
        print("– если CPI, то поставь 2")
        print("– если CPA, то поставь 3")

        while True:
            try:
                model = input("Модель работы -> ").lower()
                if model == "1":
                    pass
                elif model == "2":
                    pass
                elif model == "3":
                    pass
                else:
                    print("Указанная модель – это точно одна из CPI, CPA или CPM?")
                    continue

                return android_platform, ios_platform, model

            except ValueError:
                print("Убедись, чтобы в конверсии было указано число!")
                continue

    def start_calculate(self):
        # Calculate new rates and volumes based on input.
        android_platform, ios_platform, model = self.choose_model()

        if model == "3":
            print("\nЧто ж, клиент хочет работать по CPA, тогда мне нужны данные по конверсии из установки в целевое действие! (например, 15)")
            conversion = float(
                input("Процент конверсии -> ").replace(",", "."))/100
        else:
            pass

        print("\n3) Какая ставка и дневной объем получились при настройке кампании в Facebook?")

        while True:
            try:
                if android_platform == True:
                    base_rate_android = float(
                        input("Получившаяся ставка для Android -> ").replace(",", "."))
                    new_android_rates = {}
                    for key, value in self.android_rates.items():
                        new_value = round((value * base_rate_android), 2)
                        new_android_rates[key] = new_value

                    android_volume = float(
                        input("Получившийся объем для Android -> ").replace(",", "."))
                    new_android_volumes = {}
                    for key, value in VOLUME_COEFFICIENTS.items():
                        new_value = round((value * android_volume), 2)
                        new_android_volumes[key] = new_value
                else:
                    new_android_rates = {}
                    new_android_volumes = {}

                if ios_platform == True:
                    base_rate_ios = float(
                        input("Получившаяся ставка для iOS -> ").replace(",", "."))
                    new_ios_rates = {}
                    for key, value in self.ios_rates.items():
                        new_value = round((value * base_rate_ios), 2)
                        new_ios_rates[key] = new_value

                    ios_volume = float(
                        input("Получившийся объем для iOS -> ").replace(",", "."))
                    new_ios_volumes = {}
                    for key, value in VOLUME_COEFFICIENTS.items():
                        new_value = round((value * ios_volume), 2)
                        new_ios_volumes[key] = new_value
                else:
                    new_ios_rates = {}
                    new_ios_volumes = {}

                if model == "3":
                    for key, value in new_android_rates.items():
                        new_android_rates[key] = round(
                            (value / conversion), 2)
                    for key, value in new_ios_rates.items():
                        new_ios_rates[key] = round(
                            (value / conversion), 2)
                    for key, value in new_android_volumes.items():
                        new_android_volumes[key] = round(
                            (value * conversion), 2)
                    for key, value in new_ios_volumes.items():
                        new_ios_volumes[key] = round(
                            (value * conversion), 2)
                else:
                    pass

                return new_android_rates, new_ios_rates, model, android_platform, ios_platform, new_android_volumes, new_ios_volumes

            except ValueError:
                print("Похоже кто-то ошибся с введенным значением. Повторим? 😉")
                continue


    def specify_budget(self):
        # Limited budget may affect futher estimations.
        new_android_rates, new_ios_rates, model, android_platform, ios_platform, new_android_volumes, new_ios_volumes = self.start_calculate()
        print("\n4) Давай укажем бюджет кампании. Если бюджет неограниченный и считаем по максимуму, тогда жми Enter.")

        answer = "".join(input("Бюджет -> "))
        if answer == "":
            budget = 999999999999
        else:
            budget = int(answer)

        return new_android_rates, new_ios_rates, model, android_platform, ios_platform, new_android_volumes, new_ios_volumes, budget

    def check_creatives(self):
        # Correct rates due to creatives.
        new_android_rates, new_ios_rates, model, android_platform, ios_platform, new_android_volumes, new_ios_volumes, budget = self.specify_budget()
        print("\n5) Можем ли мы использовать свои креативы, чтобы повысить конверсию? (да/нет)")

        while True:
            answer = input("Ответ -> ").lower()

            if answer == "да":
                break
            elif answer == "нет":
                for key, value in new_android_rates.items():
                    new_android_rates[key] = round(
                        (value * INCREASE_FOR_CREATIVES), 2)
                for key, value in new_ios_rates.items():
                    new_ios_rates[key] = round(
                        (value * INCREASE_FOR_CREATIVES), 2)
                break
            else:
                print("Похоже кто-то ошибся с ответом. Повторим? 😉")
                continue

        return new_android_rates, new_ios_rates, model, android_platform, ios_platform, new_android_volumes, new_ios_volumes, budget

    def check_store_rating(self):
        # Correct rates if stores' rating lower than 4.
        new_android_rates, new_ios_rates, model, android_platform, ios_platform, new_android_volumes, new_ios_volumes, budget = self.check_creatives()
        print("\n6) А как обстоят дела с рейтингом приложения? (например, 4.4)")

        while True:
            try:
                if android_platform == True:
                    android_rating = float(
                        input("Рейтинг у Android версии -> ").replace(",", "."))
                    if 3 <= android_rating < 4:
                        for key, value in new_android_rates.items():
                            new_android_rates[key] = round(
                                (value * INCREASE_FOR_RATING), 2)
                    elif android_rating < 3:
                        print("Уууу... Все плохо 😢 . Похоже мы не можем взять это приложение, сперва нужно накрутить рейтинг в Google Play!")
                    else:
                        pass
                else:
                    pass

                if ios_platform == True:
                    ios_rating = float(
                        input("Рейтинг у iOS версии -> ").replace(",", "."))
                    if 3 <= ios_rating < 4:
                        for key, value in new_ios_rates.items():
                            new_ios_rates[key] = round(
                                (value * INCREASE_FOR_RATING), 2)
                    elif ios_rating < 3:
                        print(
                            "Уууу... Все плохо 😢 . Похоже мы не можем взять это приложение, сперва нужно накрутить рейтинг в App Store!")
                    else:
                        pass
                else:
                    pass

                return new_android_rates, new_ios_rates, model, android_platform, ios_platform, new_android_volumes, new_ios_volumes, budget

            except ValueError:
                print("Похоже кто-то ошибся с введенным значением. Повторим? 😉")
                continue

    def check_app_size(self):
        # Correct rates according to the sizes mentioned in https://bit.ly/2TpCoF5.
        new_android_rates, new_ios_rates, model, android_platform, ios_platform, new_android_volumes, new_ios_volumes, budget = self.check_store_rating()
        print("\n7) Давай укажем размер приложения в мегабайтах? (например, 70)")

        while True:
            try:
                if android_platform == True:
                    android_size = float(
                        input("Размер Android версии -> ").replace(",", "."))
                    if 100 <= android_size < 500:
                        for key, value in new_android_rates.items():
                            new_android_rates[key] = round(
                                (value * INCREASE_FOR_SIZE_ANDROID_100_500), 2)
                    elif 500 <= android_size < 1000:
                        for key, value in new_android_rates.items():
                            new_android_rates[key] = round(
                                (value * INCREASE_FOR_SIZE_500_1000), 2)
                    elif 1000 <= android_size:
                        for key, value in new_android_rates.items():
                            new_android_rates[key] = round(
                                (value * INCREASE_FOR_SIZE_OVER_1000), 2)
                    else:
                        pass
                else:
                    pass

                if ios_platform == True:
                    ios_size = float(
                        input("Размер iOS версии -> ").replace(",", "."))
                    if 150 <= ios_size < 500:
                        for key, value in new_ios_rates.items():
                            new_ios_rates[key] = round(
                                (value * INCREASE_FOR_SIZE_IOS_150_500), 2)
                    elif 500 <= ios_size < 1000:
                        for key, value in new_ios_rates.items():
                            new_ios_rates[key] = round(
                                (value * INCREASE_FOR_SIZE_500_1000), 2)
                    elif 1000 <= ios_size:
                        for key, value in new_ios_rates.items():
                            new_ios_rates[key] = round(
                                (value * INCREASE_FOR_SIZE_OVER_1000), 2)
                    else:
                        pass
                else:
                    pass

                return new_android_rates, new_ios_rates, model, android_platform, ios_platform, new_android_volumes, new_ios_volumes, budget

            except ValueError:
                print("Похоже кто-то ошибся с введенным значением. Повторим? 😉")
                continue

    def check_for_push(self):
        # Correct rates if it's a push-campaign.
        new_android_rates, new_ios_rates, model, android_platform, ios_platform, new_android_volumes, new_ios_volumes, budget = self.check_app_size()
        print("\n8) Это будет push-кампания (вывод нового продукта в ТОП за месяц) или нет? (да/нет)")

        while True:
            push = input("Ответ -> ").lower()

            if push == "да":
                print(
                    f"Тогда ставки будут увеличены на {int((INCREASE_FOR_PUSH*100)-100)}%, ведь нам придется собрать почти весь возможный трафик за период.")
                for key, value in new_android_rates.items():
                    new_android_rates[key] = round(
                        (value * INCREASE_FOR_PUSH), 2)
                for key, value in new_ios_rates.items():
                    new_ios_rates[key] = round((value * INCREASE_FOR_PUSH), 2)
                for key, value in new_android_volumes.items():
                    new_android_volumes[key] = round(
                        (value * INCREASE_FOR_PUSH_VOLUME), 2)
                for key, value in new_ios_volumes.items():
                    new_ios_volumes[key] = round(
                        (value * INCREASE_FOR_PUSH_VOLUME), 2)
            elif push == "нет":
                print(
                    "Отлично, можно не гадать о степени увеличения ставок. Работаем в обычном режиме!")
            else:
                print("Похоже кто-то ошибся с ответом. Повторим? 😉")
                continue

            return new_android_rates, new_ios_rates, model, android_platform, ios_platform, new_android_volumes, new_ios_volumes, budget

    def consider_period(self):
        # Correct rates if the start is on high season.
        new_android_rates, new_ios_rates, model, android_platform, ios_platform, new_android_volumes, new_ios_volumes, budget = self.check_for_push()
        print("\n9) Укажи номера месяцев, в которые будем продвигаться. Например: 3, 4, 5")
        print("Январь – 1\nФевраль – 2\nМарт – 3\nАпрель – 4\nМай – 5\nИюнь – 6\nИюль – 7\nАвгуст – 8\nСентябрь – 9\nОктябрь – 10\nНоябрь – 11\nДекабрь – 12")

        while True:
            try:
                months = input("Ответ -> ")
                which_months = list(map(int, re.findall('\\b\\d+\\b', months)))

                return new_android_rates, new_ios_rates, model, android_platform, ios_platform, new_android_volumes, new_ios_volumes, which_months, budget

            except ValueError:
                print("Похоже кто-то ошибся с введенным значением. Повторим? 😉")
                continue

    def check_regions(self):
        # Exclude sources that are not relevant to targeting.
        new_android_rates, new_ios_rates, model, android_platform, ios_platform, new_android_volumes, new_ios_volumes, which_months, budget = self.consider_period()
        print("\n10) Будет ли продвижение WW? (да/нет)")

        while True:
            worldwide = input("Ответ по WW -> ").lower()

            if worldwide == "нет":

                print("\nБудет ли продвижение в СНГ? (да/нет)")
                cis = input("Ответ по СНГ -> ").lower()
                if cis == "нет":
                    cis_sources = ("myTarget", "Яндекс", "ВКонтакте")
                    for key in cis_sources:
                        if key in new_android_rates:
                            new_android_rates.pop(key)
                            new_android_volumes.pop(key)
                        else:
                            pass
                        if key in new_ios_rates:
                            new_ios_rates.pop(key)
                            new_ios_volumes.pop(key)
                        else:
                            pass
                elif cis == "да":
                    pass
                else:
                    print("Похоже кто-то ошибся с ответом. Повторим? 😉")
                    continue

                print("\nБудет ли продвижение в США? (да/нет)")
                usa = input("Ответ по США -> ").lower()
                if usa == "нет":
                    usa_sources = ("Twitter", "Snapchat", "Pinterest")
                    for key in usa_sources:
                        if key in new_android_rates:
                            new_android_rates.pop(key)
                            new_android_volumes.pop(key)
                        else:
                            pass
                        if key in new_ios_rates:
                            new_ios_rates.pop(key)
                            new_ios_volumes.pop(key)
                        else:
                            pass
                elif usa == "да":
                    pass
                else:
                    print("Похоже кто-то ошибся с ответом. Повторим? 😉")
                    continue

            elif worldwide == "да":
                pass
            else:
                print("Похоже кто-то ошибся с ответом. Повторим? 😉")
                continue

            return new_android_rates, new_ios_rates, model, android_platform, ios_platform, new_android_volumes, new_ios_volumes, which_months, budget

    def choose_tracker(self):
        # Correct sources if they are limited by tracking system.
        new_android_rates, new_ios_rates, model, android_platform, ios_platform, new_android_volumes, new_ios_volumes, which_months, budget = self.check_regions()
        print("\n11) Рекламодатель будет использовать треккинговую систему AppsFlyer, Adjust, Kochava или Tune? (да/нет)?")

        while True:
            tracker = input("Ответ -> ").lower()

            if tracker == "да":
                pass
            elif tracker == "нет":
                print("\n🚨  Хм, тут сложнее... Каждый трекер индивидуален, так что по итогу рекомендую еще проверить, поддерживает ли он указанные источники!")
            else:
                print("Похоже кто-то ошибся с ответом. Повторим? 😉")
                continue

            return new_android_rates, new_ios_rates, model, android_platform, ios_platform, new_android_volumes, new_ios_volumes, which_months, budget

    def show_results(self):
        # This is the final step of estimation.
        new_android_rates, new_ios_rates, model, android_platform, ios_platform, new_android_volumes, new_ios_volumes, which_months, budget = self.choose_tracker()

        models = {
            "1": "CPM",
            "2": "CPI",
            "3": "CPA"
        }

        months = {
            1: "Январь",
            2: "Февраль",
            3: "Март",
            4: "Апрель",
            5: "Май",
            6: "Июнь",
            7: "Июль",
            8: "Август",
            9: "Сентябрь",
            10: "Октябрь",
            11: "Ноябрь",
            12: "Декабрь"
        }

        now = datetime.datetime.now()

        if android_platform == True:
            # Count total volumes for Android.
            volumes_all_together = []
            for month in which_months:
                number_of_days_in_month = int(
                    calendar.monthrange(now.year, month)[1])
                if month == 2 or month == 11:
                    volumes = [int((volume / INCREASE_FEBRUARY_NOVEMBER) * number_of_days_in_month) for key, volume in new_android_volumes.items()]
                    volumes_all_together.append(volumes)
                elif month == 12:
                    volumes = [int((volume / INCREASE_DECEMBER) * number_of_days_in_month) for key, volume in new_android_volumes.items()]
                    volumes_all_together.append(volumes)
                else:
                    volumes = [int(volume * number_of_days_in_month) for key, volume in new_android_volumes.items()]
                    volumes_all_together.append(volumes)

            budgets = {}
            n = 0
            for volume in numpy.sum(volumes_all_together, axis=0):
                if n <= len(new_android_rates) - 1:
                    key = list(new_android_rates.keys())[n]
                    rate = list(new_android_rates.values())[n]
                    if model == "1":
                        budgets[key] = (volume * rate) / 1000
                    else:
                        budgets[key] = volume * rate
                    n += 1

            android_budget = sum(budgets.values())

        else:
            pass

        if ios_platform == True:
            # Count total volumes for iOS.
            volumes_all_together = []
            for month in which_months:
                number_of_days_in_month = int(
                    calendar.monthrange(now.year, month)[1])
                if month == 2 or month == 11:
                    volumes = [int((volume / INCREASE_FEBRUARY_NOVEMBER) * number_of_days_in_month) for key, volume in new_ios_volumes.items()]
                    volumes_all_together.append(volumes)
                elif month == 12:
                    volumes = [int((volume / INCREASE_DECEMBER) * number_of_days_in_month) for key, volume in new_ios_volumes.items()]
                    volumes_all_together.append(volumes)
                else:
                    volumes = [int(volume * number_of_days_in_month) for key, volume in new_ios_volumes.items()]
                    volumes_all_together.append(volumes)

            budgets = {}
            n = 0
            for volume in numpy.sum(volumes_all_together, axis=0):
                if n <= len(new_ios_rates) - 1:
                    key = list(new_ios_rates.keys())[n]
                    rate = list(new_ios_rates.values())[n]
                    if model == "1":
                        budgets[key] = (volume * rate) / 1000
                    else:
                        budgets[key] = volume * rate
                    n += 1

            ios_budget = sum(budgets.values())

        else:
            pass

        # Count total budget and check if there is a need to decrease volumes in order to fit the limited budget.
        if android_platform == True & ios_platform == True:
            total_budget = android_budget + ios_budget
        elif android_platform == True:
            total_budget = android_budget
        elif ios_platform == True:
            total_budget = ios_budget

        # If budget limit exceeded then decrease volumes accordingly.
        print("\n🏆  Моя рекомендация будет следующей: 🏆")
        difference = budget / total_budget
        
        if android_platform == True:
            print("\n--- Android 🤖  ---")
            table_android = BeautifulTable()
            table_android.append_column(
                "Источник", [key for key, value in new_android_rates.items()])
            table_android.append_column(
                f"Ставка {models[model]}", [(str(rate)).replace(".", ",") for key, rate in new_android_rates.items()])

            # Count total volumes for Android.
            volumes_all_together = []
            for month in which_months:
                number_of_days_in_month = int(
                    calendar.monthrange(now.year, month)[1])
                if month == 2 or month == 11:
                    if difference < 1:
                        volumes = [int(((volume / INCREASE_FEBRUARY_NOVEMBER) * number_of_days_in_month) * difference) for key, volume in new_android_volumes.items()]
                    else:
                        volumes = [int(((volume / 1000) / INCREASE_FEBRUARY_NOVEMBER) * number_of_days_in_month) if model == "1" else int((volume / INCREASE_FEBRUARY_NOVEMBER) * number_of_days_in_month) for key, volume in new_android_volumes.items()]
                    volumes_all_together.append(volumes)
                    table_android.append_column(months[month], volumes)
                elif month == 12:
                    if difference < 1:
                        volumes = [int(((volume / INCREASE_DECEMBER) * number_of_days_in_month) * difference) for key, volume in new_android_volumes.items()]
                    else:
                        volumes = [int(((volume / 1000) / INCREASE_DECEMBER) * number_of_days_in_month) if model == "1" else int((volume / INCREASE_DECEMBER) * number_of_days_in_month) for key, volume in new_android_volumes.items()]
                    volumes_all_together.append(volumes)
                    table_android.append_column(months[month], volumes)
                else:
                    if difference < 1:
                        volumes = [int((volume * number_of_days_in_month) * difference) for key, volume in new_android_volumes.items()]
                    else:
                        volumes = [int((volume / 1000) * number_of_days_in_month) if model == "1" else int(volume * number_of_days_in_month) for key, volume in new_android_volumes.items()]
                    volumes_all_together.append(volumes)
                    table_android.append_column(months[month], volumes)

            budgets = {}
            n = 0
            for volume in numpy.sum(volumes_all_together, axis=0):
                if n <= len(new_android_rates) - 1:
                    key = list(new_android_rates.keys())[n]
                    rate = list(new_android_rates.values())[n]
                    if model == "1":
                        budgets[key] = (volume * rate) / 1000
                    else:
                        budgets[key] = volume * rate
                    n += 1

            table_android.append_column(
                "Всего без НДС", [int(spend) for key, spend in budgets.items()])
            print(table_android)

            print("\n")

            for key, spend in budgets.items():
                if spend < BUDGET_BOTTOM[key]:
                    shortage = BUDGET_BOTTOM[key] - spend
                    print(
                        f"🚨  Обрати внимание, что мы не добираем {int(shortage)} до минимального бюджета по {key} для Android!")
                else:
                    pass
        else:
            pass

        if ios_platform == True:
            print("\n--- iOS 🍏  ---")
            table_ios = BeautifulTable()
            table_ios.append_column(
                "Источник", [key for key, value in new_ios_rates.items()])
            table_ios.append_column(
                f"Ставка {models[model]}", [(str(rate)).replace(".", ",") for key, rate in new_ios_rates.items()])

            # Count total volumes for iOS.
            volumes_all_together = []
            for month in which_months:
                number_of_days_in_month = int(
                    calendar.monthrange(now.year, month)[1])
                if month == 2 or month == 11:
                    if difference < 1:
                        volumes = [int(((volume / INCREASE_FEBRUARY_NOVEMBER) * number_of_days_in_month) * difference) for key, volume in new_ios_volumes.items()]
                    else:
                        volumes = [int(((volume / 1000) / INCREASE_FEBRUARY_NOVEMBER) * number_of_days_in_month) if model == "1" else int((volume / INCREASE_FEBRUARY_NOVEMBER) * number_of_days_in_month) for key, volume in new_ios_volumes.items()]
                    volumes_all_together.append(volumes)
                    table_ios.append_column(months[month], volumes)
                elif month == 12:
                    if difference < 1:
                        volumes = [int(((volume / INCREASE_DECEMBER) * number_of_days_in_month) * difference) for key, volume in new_ios_volumes.items()]
                    else:
                        volumes = [int(((volume / 1000) / INCREASE_DECEMBER) * number_of_days_in_month) if model == "1" else int((volume / INCREASE_DECEMBER) * number_of_days_in_month) for key, volume in new_ios_volumes.items()]
                    volumes_all_together.append(volumes)
                    table_ios.append_column(months[month], volumes)
                else:
                    if difference < 1:
                        volumes = [int((volume * number_of_days_in_month) * difference) for key, volume in new_ios_volumes.items()]
                    else:
                        volumes = [int((volume / 1000) * number_of_days_in_month) if model == "1" else int(volume * number_of_days_in_month) for key, volume in new_ios_volumes.items()]
                    volumes_all_together.append(volumes)
                    table_ios.append_column(months[month], volumes)

            budgets = {}
            n = 0
            for volume in numpy.sum(volumes_all_together, axis=0):
                if n <= len(new_ios_rates) - 1:
                    key = list(new_ios_rates.keys())[n]
                    rate = list(new_ios_rates.values())[n]
                    if model == "1":
                        budgets[key] = (volume * rate) / 1000
                    else:
                        budgets[key] = volume * rate
                    n += 1

            table_ios.append_column("Всего без НДС", [int(spend) for key, spend in budgets.items()])
            print(table_ios)

            print("\n")

            for key, spend in budgets.items():
                if spend < BUDGET_BOTTOM[key]:
                    shortage = BUDGET_BOTTOM[key] - spend
                    print(
                        f"🚨  Обрати внимание, что мы не добираем {int(shortage)} до минимального бюджета по {key} для iOS!")
                else:
                    pass
        else:
            pass
        

    def launch_whole_process(self):
        self.show_results()
        print("\nТеперь осталось уточнить про hard или soft KPI и запрещенные источники (или недоступные по ГЕО) + не забудь учесть в оценке долю внешней сети партнеров.\nУдачи! 🤞\n")


class Landing:

    landing_rates = {
        "Facebook": 1,
        "Google": 1,
        "myTarget": 0.95,
        "Twitter": 1.1,
        "Snapchat": 0.95,
        "Яндекс": 1,
        "ВКонтакте": 0.9
    }

    def choose_model(self):
        # Define ads model.
        print("\nПриступим к оценке лендинга? 😜")
        print("\n1) Давай укажем модель работы, по которой будем работать? (CPM/CPC/CPA)")
        print("– если CPM, то поставь 1")
        print("– если CPC, то поставь 2")
        print("– если CPA, то поставь 3")

        while True:
            try:
                model = input("Модель работы -> ").lower()
                return model

            except TypeError:
                print("Указанная модель – это точно одна из CPM, CPC или CPA?")
                continue

    def start_calculate(self):
        # Calculate new rates and volumes based on input.
        model = self.choose_model()
        print("\n2) Какая ставка и дневной объем получились при настройке кампании в Facebook?")

        while True:
            try:
                base_rate = float(
                    input("Получившаяся ставка -> ").replace(",", "."))

                new_landing_rates = {}
                for key, value in self.landing_rates.items():
                    new_value = round((value * base_rate), 2)
                    new_landing_rates[key] = new_value

                landing_volume = float(
                        input("Получившийся объем-> ").replace(",", "."))
                new_landing_volumes = {}
                for key, value in VOLUME_COEFFICIENTS.items():
                    new_value = round((value * landing_volume), 2)
                    new_landing_volumes[key] = new_value

                if model == "1":
                    pass
                elif model == "2":
                    pass
                elif model == "3":
                    print("Что ж, клиент хочет работать по CPA, тогда мне нужны данные по конверсии из перехода в целевое действие! (например, 15)")
                    conversion = float(input("Процент конверсии -> ").replace(",", "."))/100
                    for key, value in new_landing_rates.items():
                        new_landing_rates[key] = round(
                            (value / conversion), 2)
                    for key, value in new_landing_volumes.items():
                        new_landing_volumes[key] = round(
                            (value * conversion), 2)
                else:
                    print("Указанная модель – это точно одна из CPM, CPC или CPA?")
                    continue

                return new_landing_rates, new_landing_volumes, model

            except ValueError:
                print("Похоже кто-то ошибся с введенным значением. Повторим? 😉")
                continue

    def check_creatives(self):
        # Correct rates due to creatives.
        new_landing_rates, new_landing_volumes, model = self.start_calculate()
        print("\n3) Можем ли мы использовать свои креативы, чтобы повысить конверсию? (да/нет)")

        while True:
            answer = input("Ответ -> ").lower()
            if answer == "да":
                pass
            elif answer == "нет":
                for key, value in new_landing_rates.items():
                    new_landing_rates[key] = round(
                        (value * INCREASE_FOR_CREATIVES), 2)
            else:
                print("Похоже кто-то ошибся с ответом. Повторим? 😉")
                continue

            return new_landing_rates, new_landing_volumes, model

    def check_for_push(self):
        # Correct rates if it's a push-campaign.
        new_landing_rates, new_landing_volumes, model = self.check_creatives()
        print("\n4) Это будет push-кампания (вывод нового продукта в ТОП за месяц) или нет? (да/нет)")

        while True:
            push = input("Ответ -> ").lower()

            if push == "да":
                print(
                    f"Тогда ставки будут увеличены на {int((INCREASE_FOR_PUSH*100)-100)}%, ведь нам придется собрать почти весь возможный трафик за период.")
                for key, value in new_landing_rates.items():
                    new_landing_rates[key] = round(
                        (value * INCREASE_FOR_PUSH), 2)
                for key, value in new_landing_volumes.items():
                    new_landing_volumes[key] = round(
                        (value * INCREASE_FOR_PUSH_VOLUME), 2)
            elif push == "нет":
                print(
                    "Отлично, можно не гадать о степени увеличения ставок. Работаем в обычном режиме!")
            else:
                print("Похоже кто-то ошибся с ответом. Повторим? 😉")
                continue

            return new_landing_rates, new_landing_volumes, model

    def consider_period(self):
        # Correct rates if the start is on high season.
        new_landing_rates, new_landing_volumes, model = self.check_for_push()
        print("\n5) Укажи номера месяцев, в которые будем продвигаться. Например: 3, 4, 5")
        print("Январь – 1\nФевраль – 2\nМарт – 3\nАпрель – 4\nМай – 5\nИюнь – 6\nИюль – 7\nАвгуст – 8\nСентябрь – 9\nОктябрь – 10\nНоябрь – 11\nДекабрь – 12")

        while True:
            try:
                months = input("Ответ -> ")
                which_months = list(map(int, re.findall('\\b\\d+\\b', months)))

                return new_landing_rates, new_landing_volumes, model, which_months

            except ValueError:
                print("Похоже кто-то ошибся с введенным значением. Повторим? 😉")
                continue

    def check_regions(self):
        # Exclude sources that are not relevant to targeting.
        new_landing_rates, new_landing_volumes, model, which_months = self.consider_period()
        print("\n6) Будет ли продвижение WW? (да/нет)")

        while True:
            worldwide = input("Ответ по WW -> ").lower()

            if worldwide == "нет":

                print("\nБудет ли продвижение в СНГ? (да/нет)")
                cis = input("Ответ по СНГ -> ").lower()
                if cis == "нет":
                    cis_sources = ("myTarget", "Яндекс", "ВКонтакте")
                    for key in cis_sources:
                        if key in new_landing_rates:
                            new_landing_rates.pop(key)
                            new_landing_volumes.pop(key)
                        else:
                            pass
                elif cis == "да":
                    pass
                else:
                    print("Похоже кто-то ошибся с ответом. Повторим? 😉")
                    continue

                print("\nБудет ли продвижение в США? (да/нет)")
                usa = input("Ответ по США -> ").lower()
                if usa == "нет":
                    usa_sources = ("Twitter", "Snapchat", "Pinterest")
                    for key in usa_sources:
                        if key in new_landing_rates:
                            new_landing_rates.pop(key)
                            new_landing_volumes.pop(key)
                        else:
                            pass
                elif usa == "да":
                    pass
                else:
                    print("Похоже кто-то ошибся с ответом. Повторим? 😉")
                    continue

            elif worldwide == "да":
                pass
            else:
                print("Похоже кто-то ошибся с ответом. Повторим? 😉")
                continue

            return new_landing_rates, new_landing_volumes, model, which_months

    def show_results(self):
        # This is the final step of estimation.
        new_landing_rates, new_landing_volumes, model, which_months = self.check_regions()

        models = {
            "1": "CPM",
            "2": "CPI",
            "3": "CPA"
        }

        months = {
            1: "Январь",
            2: "Февраль",
            3: "Март",
            4: "Апрель",
            5: "Май",
            6: "Июнь",
            7: "Июль",
            8: "Август",
            9: "Сентябрь",
            10: "Октябрь",
            11: "Ноябрь",
            12: "Декабрь"
        }

        now = datetime.datetime.now()

        print("\n🏆  Моя рекомендация будет следующей: 🏆")

        print("\n--- Лендинг 📄  ---")
        table_landing = BeautifulTable()
        table_landing.append_column(
            "Источник", [key for key, value in new_landing_rates.items()])
        table_landing.append_column(
            f"Ставка {models[model]}", [(str(rate)).replace(".", ",") for key, rate in new_landing_rates.items()])

        volumes_all_together = []
        for month in which_months:
            number_of_days_in_month = int(calendar.monthrange(now.year, month)[1])
            if month == 2 or month == 11:
                volumes = [int(((volume / 1000) / INCREASE_FEBRUARY_NOVEMBER) * number_of_days_in_month) if model == "1" else int((volume / INCREASE_FEBRUARY_NOVEMBER) * number_of_days_in_month) for key, volume in new_landing_volumes.items()]
                volumes_all_together.append(volumes)
                table_landing.append_column(months[month], volumes)
            elif month == 12:
                volumes = [int(((volume / 1000) / INCREASE_DECEMBER) * number_of_days_in_month) if model == "1" else int((volume / INCREASE_DECEMBER) * number_of_days_in_month) for key, volume in new_landing_volumes.items()]
                volumes_all_together.append(volumes)
                table_landing.append_column(months[month], volumes)
            else:
                volumes = [int((volume / 1000) * number_of_days_in_month) if model == "1" else int(volume * number_of_days_in_month) for key, volume in new_landing_volumes.items()]
                volumes_all_together.append(volumes)
                table_landing.append_column(months[month], volumes)

        budgets = {}
        n = 0
        for volume in numpy.sum(volumes_all_together, axis=0):
            if n <= len(new_landing_rates) - 1:
                key = list(new_landing_rates.keys())[n]
                rate = list(new_landing_rates.values())[n]
                budgets[key] = volume * rate
                n += 1

        table_landing.append_column("Всего без НДС", [int(spend) for key, spend in budgets.items()])
        print(table_landing)
        
        print("\n")

        for key, spend in budgets.items():
            if spend < BUDGET_BOTTOM[key]:
                difference = BUDGET_BOTTOM[key] - spend
                print(f"🚨  Обрати внимание, что мы не добираем {int(difference)} до минимального бюджета по {key} для iOS!")
            else:
                pass

    def launch_whole_process(self):
        self.show_results()
        print("\nТеперь осталось уточнить про hard или soft KPI, запрещенные источники (или недоступные по ГЕО) и не забудь учесть в оценке долю внешней сети партнеров")
        print("+ сделай тест скорости загрузки здесь: https://testmysite.withgoogle.com/intl/ru-ru и если значение выше 5 сек, то рекомендуется оптимизация.\nУдачи! 🤞\n")


class Video:
    pass


print("\nПривеееет 👋\n\nДавай выберем, что будем продвигать: приложение или лендинг?")
while True:
    response = input("Будем продвигать –> ").lower()

    if response == "приложение" or response == "прилажение" or response == "преложение" or response == "прелажение" or response == "прилу":
        app_estimate = App()
        app_estimate.launch_whole_process()
        break
    elif response == "лендинг" or response == "лэндинг" or response == "ленд" or response == "лэнд" or response == "лэндос" or response == "лендос":
        landing_estimate = Landing()
        landing_estimate.launch_whole_process()
        break
    # elif response == "видео" or response == "видос":
    #     landing_estimate = Video()
    #     landing_estimate.launch_whole_process()
    #     break
    else:
        print("Пожалуйста, проверь корректность введенного значения и попробуй снова!")
        continue
