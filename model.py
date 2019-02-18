# Чтобы использовать эту модель, на компьютере должен быть установлен язык программировани Python, который можно скачать отсюда: https://www.python.org/downloads/
# Дальше, открываешь приложение "Терминал" в утилитах и переходишь в папку (в самом терминале), в которой лежит файл model.py
# Чтобы запустить оценку, введи комманду и нажми Enter: python3 model.py
# Следуй инструкциям и наслаждайся 🥳

INCREASE_FOR_CREATIVES = 1.3
INCREASE_FOR_RATING = 1.1
INCREASE_FOR_PUSH = 1.3
INCREASE_FOR_SIZE_ANDROID_100_500 = 1.1
INCREASE_FOR_SIZE_IOS_150_500 = 1.1
INCREASE_FOR_SIZE_500_1000 = 1.2
INCREASE_FOR_SIZE_OVER_1000 = 1.3
INCREASE_FEBRUARY_NOVEMBER = 1.3
INCREASE_DECEMBER = 2

MIN_BUDGET_FACEBOOK = 1500
MIN_BUDGET_GOOGLE = 1500
MIN_BUDGET_MYTARGET = 1000
MIN_BUDGET_INAPP = 1000
MIN_BUDGET_VIDEONETWORKS = 1500
MIN_BUDGET_TWITTER = 3000
MIN_BUDGET_SNAPCHAT = 2000
MIN_BUDGET_YANDEX = 1000
MIN_BUDGET_PINTEREST = 1500
MIN_BUDGET_DSP = 2000
MIN_BUDGET_ASA = 2000

VOLUME_COEFFICIENTS = {
        "Facebook": 1,
        "Google": 1.17,
        "myTarget": 1.33,
        "In-App": 1.17,
        "Видеосети": 0.5,
        "Twitter": 0.5,
        "Snapchat": 0.17,
        "Яндекс": 0.67,
        "Pinterest": 0.17,
        "DSP": 1.33,
        "ASA": 0.5
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
        "Pinterest": 1000,
        "DSP": 2000,
        "ASA": 2000
    }


class App:

    android_rates = {
        "Facebook": 1,
        "Google": 1,
        "myTarget": 0.9,
        "In-App": 0.9,
        "Видеосети": 1.1,
        "Twitter": 1.1,
        "Snapchat": 1,
        "Яндекс": 1,
        "DSP": 0.9,
        "ASA": 1
    }

    ios_rates = {
        "Facebook": 1,
        "Google": 1.1,
        "myTarget": 0.9,
        "In-App": 0.9,
        "Видеосети": 1.05,
        "Twitter": 1.1,
        "Snapchat": 1,
        "Яндекс": 1,
        "DSP": 0.9,
        "ASA": 1
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
        nandroid_platform, ios_platform = self.select_platform()
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

                return nandroid_platform, ios_platform, model

            except ValueError:
                print("Убедись, чтобы в конверсии было указано число!")
                continue

    def start_calculate(self):
        # Calculate new rates and volumes based on input.
        android_platform, ios_platform, model = self.choose_model()

        if model == "3":
            print("\nЧто ж, клиент хочет работать по CPA, тогда мне нужны данные по конверсии из установки в целевое действие! (например, 15)")
            conversion = float(input("Процент конверсии -> ").replace(",", "."))/100
        else:
            pass

        print("\n3) Какая ставка и объем получились при настройке кампании в Facebook?")

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
                    new_android_volume = {}
                    for key, value in VOLUME_COEFFICIENTS.items():
                        new_value = round((value * android_volume), 2)
                        new_android_volume[key] = new_value
                else:
                    new_android_rates = {}
                    new_android_volume = {}

                if ios_platform == True:
                    base_rate_ios = float(
                        input("Получившаяся ставка для iOS -> ").replace(",", "."))
                    new_ios_rates = {}
                    for key, value in self.ios_rates.items():
                        new_value = round((value * base_rate_ios), 2)
                        new_ios_rates[key] = new_value

                    ios_volume = float(
                        input("Получившийся объем для iOS -> ").replace(",", "."))
                    new_ios_volume = {}
                    for key, value in VOLUME_COEFFICIENTS.items():
                        new_value = round((value * ios_volume), 2)
                        new_ios_volume[key] = new_value
                else:
                    new_ios_rates = {}
                    new_ios_volume = {}

                if model == "3":
                    for key, value in new_android_rates.items():
                        new_android_rates[key] = round(
                            (value / conversion), 2)
                    for key, value in new_ios_rates.items():
                        new_ios_rates[key] = round(
                            (value / conversion), 2)
                    for key, value in new_android_volume.items():
                        new_android_volume[key] = round(
                            (value * conversion), 2)
                    for key, value in new_ios_volume.items():
                        new_ios_volume[key] = round(
                            (value * conversion), 2)
                else:
                    pass

                return new_android_rates, new_ios_rates, model, android_platform, ios_platform, new_android_volume, new_ios_volume

            except ValueError:
                print("Похоже кто-то ошибся с введенным значением. Повторим? 😉")
                continue

    def check_creatives(self):
        # Correct rates due to creatives.
        new_android_rates, new_ios_rates, model, android_platform, ios_platform, new_android_volume, new_ios_volume = self.start_calculate()
        print("\n4) Можем ли мы использовать свои креативы, чтобы повысить конверсию? (да/нет)")

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

        return new_android_rates, new_ios_rates, model, android_platform, ios_platform, new_android_volume, new_ios_volume

    def check_store_rating(self):
        # Correct rates if stores' rating lower than 4.
        new_android_rates, new_ios_rates, model, android_platform, ios_platform, new_android_volume, new_ios_volume = self.check_creatives()
        print("\n5) А как обстоят дела с рейтингом приложения? (например, 4.4)")

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
                        print(
                            "Уууу... Все плохо 😢 . Похоже мы не можем взять это приложение, сперва нужно накрутить рейтинг в Google Play!")
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

                return new_android_rates, new_ios_rates, model, android_platform, ios_platform, new_android_volume, new_ios_volume

            except ValueError:
                print("Похоже кто-то ошибся с введенным значением. Повторим? 😉")
                continue

    def check_app_size(self):
        # Correct rates according to the sizes mentioned in https://bit.ly/2TpCoF5.
        new_android_rates, new_ios_rates, model, android_platform, ios_platform, new_android_volume, new_ios_volume = self.check_store_rating()
        print("\n6) Давай укажем размер приложения в мегабайтах? (например, 70)")

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

                return new_android_rates, new_ios_rates, model, android_platform, ios_platform, new_android_volume, new_ios_volume

            except ValueError:
                print("Похоже кто-то ошибся с введенным значением. Повторим? 😉")
                continue

    def check_for_push(self):
        # Correct rates if it's a push-campaign.
        new_android_rates, new_ios_rates, model, android_platform, ios_platform, new_android_volume, new_ios_volume = self.check_app_size()
        print("\n7) Это будет push-кампания (вывод нового продукта в ТОП за месяц) или нет? (да/нет)")

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
            elif push == "нет":
                print(
                    "Отлично, можно не гадать о степени увеличения ставок. Работаем в обычном режиме!")
            else:
                print("Похоже кто-то ошибся с ответом. Повторим? 😉")
                continue

            return new_android_rates, new_ios_rates, model, android_platform, ios_platform, new_android_volume, new_ios_volume

    def consider_season(self):
        # Correct rates if the start is on high season.
        new_android_rates, new_ios_rates, model, android_platform, ios_platform, new_android_volume, new_ios_volume = self.check_for_push()
        print("\n8) Есть несколько месяцев, старт в которых получается дороже обычного:")
        print(
            f"– если будем запускать кампанию в Феврале или Ноябре и на 1 месяц, тогда поставь {INCREASE_FEBRUARY_NOVEMBER}")
        print(
            f"– если будем запускать кампанию в Декабре и на 1 месяц, тогда поставь {INCREASE_DECEMBER}")
        print("– если будем запускать кампанию на других условиях, тогда поставь 0")

        while True:
            try:
                season = float(input("Ответ -> ").replace(",", "."))

                if season == INCREASE_FEBRUARY_NOVEMBER:
                    for key, value in new_android_rates.items():
                        new_android_rates[key] = round(
                            (value * INCREASE_FEBRUARY_NOVEMBER), 2)
                    for key, value in new_ios_rates.items():
                        new_ios_rates[key] = round(
                            (value * INCREASE_FEBRUARY_NOVEMBER), 2)
                elif season == INCREASE_DECEMBER:
                    for key, value in new_android_rates.items():
                        new_android_rates[key] = round(
                            (value * INCREASE_DECEMBER), 2)
                    for key, value in new_ios_rates.items():
                        new_ios_rates[key] = round(
                            (value * INCREASE_DECEMBER), 2)
                else:
                    pass

                return new_android_rates, new_ios_rates, model, android_platform, ios_platform, new_android_volume, new_ios_volume

            except ValueError:
                print("Похоже кто-то ошибся с введенным значением. Повторим? 😉")
                continue

    def check_regions(self):
        # Exclude sources that are not relevant to targeting.
        new_android_rates, new_ios_rates, model, android_platform, ios_platform, new_android_volume, new_ios_volume = self.consider_season()
        print("\n9) Будет ли продвижение WW? (да/нет)")

        while True:
            worldwide = input("Ответ по WW -> ").lower()

            if worldwide == "нет":

                print("\nБудет ли продвижение в СНГ? (да/нет)")
                cis = input("Ответ по СНГ -> ").lower()
                if cis == "нет":
                    cis_sources = ("myTarget", "Яндекс")
                    for key in cis_sources:
                        if key in new_android_rates:
                            new_android_rates.pop(key)
                        else:
                            pass
                        if key in new_ios_rates:
                            new_ios_rates.pop(key)
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
                        else:
                            pass
                        if key in new_ios_rates:
                            new_ios_rates.pop(key)
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

            return new_android_rates, new_ios_rates, model, android_platform, ios_platform, new_android_volume, new_ios_volume

    def choose_tracker(self):
        # Correct sources if they are limited by tracking system.
        new_android_rates, new_ios_rates, model, android_platform, ios_platform, new_android_volume, new_ios_volume = self.check_regions()
        print("\n10) Рекламодатель будет использовать треккинговую систему AppsFlyer, Adjust, Kochava или Tune? (да/нет)?")

        while True:
            tracker = input("Ответ -> ").lower()

            if tracker == "да":
                pass
            elif tracker == "нет":
                print("\n🚨  Хм, тут сложнее... Каждый трекер индивидуален, так что по итогу рекомендую еще проверить, поддерживает ли он указанные источники!")
            else:
                print("Похоже кто-то ошибся с ответом. Повторим? 😉")
                continue

            return new_android_rates, new_ios_rates, model, android_platform, ios_platform, new_android_volume, new_ios_volume

    def show_results(self):
        # This is the final step of estimation.
        new_android_rates, new_ios_rates, model, android_platform, ios_platform, new_android_volume, new_ios_volume = self.choose_tracker()
        print("\n🏆  Моя рекомендация будет следующей: 🏆")

        if android_platform == True:
            print("\n--- Android 🤖  ---")
            budgets = {}
            for key, rate in new_android_rates.items():

                if model == "1":
                    volume = int(new_android_volume[key])/1000
                else:
                    volume = int(new_android_volume[key])

                new_volume = format(int(new_android_volume[key]), ",d").replace(",", " ")
                spend = volume * rate
                new_spend = format(round(spend), ",d").replace(",", " ")
                budgets[key] = spend
                new_rate = (str(rate)).replace(".", ",")
                print(f"{key}:".ljust(15) + f"ставка – {new_rate} USD".ljust(25) + f"объем – {new_volume}".ljust(20) + f"бюджет – {new_spend} USD")

            print("\n")

            for key, spend in budgets.items():
                if spend < BUDGET_BOTTOM[key]:
                    difference = BUDGET_BOTTOM[key] - round(spend)
                    new_difference = format(difference, ",d").replace(",", " ")
                    print(f"🚨  Обрати внимание, что мы не добираем {new_difference} USD до минимального бюджета по {key} для Android!")
                else:
                    pass
        else:
            pass

        if ios_platform == True:
            print("\n--- iOS 🍏  ---")
            budgets = {}
            for key, rate in new_ios_rates.items():

                if model == "1":
                    volume = int(new_ios_volume[key])/1000
                else:
                    volume = int(new_ios_volume[key])

                new_volume = format(int(new_ios_volume[key]), ",d").replace(",", " ")
                spend = volume * rate
                new_spend = format(round(spend), ",d").replace(",", " ")
                budgets[key] = spend
                new_rate = (str(rate)).replace(".", ",")
                print(f"{key}:".ljust(15) + f"ставка – {new_rate} USD".ljust(25) + f"объем – {new_volume}".ljust(20) + f"бюджет – {new_spend} USD")
            
            print("\n")

            for key, spend in budgets.items():
                if spend < BUDGET_BOTTOM[key]:
                    difference = BUDGET_BOTTOM[key] - round(spend)
                    new_difference = format(difference, ",d").replace(",", " ")
                    print(f"🚨  Обрати внимание, что мы не добираем {new_difference} USD до минимального бюджета по {key} для iOS!")
                else:
                    pass
        else:
            pass

    def launch_whole_process(self):
        self.show_results()
        print("\nТеперь осталось уточнить про hard или soft KPI и запрещенные источники (или недоступные по ГЕО)\n+ не забудь учесть в оценке долю внешней сети партнеров.\nУдачи! 🤞\n")


class Landing:

    landing_rates = {
        "Facebook": 1,
        "Google": 1,
        "myTarget": 0.9,
        "Twitter": 1.4,
        "Snapchat": 1,
        "Яндекс": 1,
        "DSP": 0.9
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
        print("\n2) Какая ставка и объем получились при настройке кампании в Facebook?")

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
                new_landing_volume = {}
                for key, value in VOLUME_COEFFICIENTS.items():
                    new_value = round((value * landing_volume), 2)
                    new_landing_volume[key] = new_value

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
                    for key, value in new_landing_volume.items():
                        new_landing_volume[key] = round(
                            (value * conversion), 2)
                else:
                    print("Указанная модель – это точно одна из CPM, CPC или CPA?")
                    continue

                return new_landing_rates, new_landing_volume, model

            except ValueError:
                print("Похоже кто-то ошибся с введенным значением. Повторим? 😉")
                continue

    def check_creatives(self):
        # Correct rates due to creatives.
        new_landing_rates, new_landing_volume, model = self.start_calculate()
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

            return new_landing_rates, new_landing_volume, model

    def check_for_push(self):
        # Correct rates if it's a push-campaign.
        new_landing_rates, new_landing_volume, model = self.check_creatives()
        print("\n4) Это будет push-кампания (вывод нового продукта в ТОП за месяц) или нет? (да/нет)")

        while True:
            push = input("Ответ -> ").lower()

            if push == "да":
                print(
                    f"Тогда ставки будут увеличены на {int((INCREASE_FOR_PUSH*100)-100)}%, ведь нам придется собрать почти весь возможный трафик за период.")
                for key, value in new_landing_rates.items():
                    new_landing_rates[key] = round(
                        (value * INCREASE_FOR_PUSH), 2)
            elif push == "нет":
                print(
                    "Отлично, можно не гадать о степени увеличения ставок. Работаем в обычном режиме!")
            else:
                print("Похоже кто-то ошибся с ответом. Повторим? 😉")
                continue

            return new_landing_rates, new_landing_volume, model

    def consider_season(self):
        # Correct rates if the start is on high season.
        new_landing_rates, new_landing_volume, model = self.check_for_push()
        print("\n5) Есть несколько месяцев, старт в которых получается дороже обычного:")
        print(
            f"– если будем запускать кампанию в Феврале или Ноябре и на 1 месяц, тогда поставь {INCREASE_FEBRUARY_NOVEMBER}")
        print(
            f"– если будем запускать кампанию в Декабре и на 1 месяц, тогда поставь {INCREASE_DECEMBER}")
        print("– если будем запускать кампанию на других условиях, тогда поставь 0")

        while True:
            try:
                season = float(input("Ответ -> ").replace(",", "."))

                if season == INCREASE_FEBRUARY_NOVEMBER:
                    for key, value in new_landing_rates.items():
                        new_landing_rates[key] = round(
                            (value * INCREASE_FEBRUARY_NOVEMBER), 2)
                elif season == INCREASE_DECEMBER:
                    for key, value in new_landing_rates.items():
                        new_landing_rates[key] = round(
                            (value * INCREASE_DECEMBER), 2)
                else:
                    pass

                return new_landing_rates, new_landing_volume, model

            except ValueError:
                print("Похоже кто-то ошибся с введенным значением. Повторим? 😉")
                continue

    def check_regions(self):
        # Exclude sources that are not relevant to targeting.
        new_landing_rates, new_landing_volume, model = self.consider_season()
        print("\n6) Будет ли продвижение WW? (да/нет)")

        while True:
            worldwide = input("Ответ по WW -> ").lower()

            if worldwide == "нет":

                print("\nБудет ли продвижение в СНГ? (да/нет)")
                cis = input("Ответ по СНГ -> ").lower()
                if cis == "нет":
                    cis_sources = ("myTarget", "Яндекс")
                    for key in cis_sources:
                        if key in new_landing_rates:
                            new_landing_rates.pop(key)
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

            return new_landing_rates, new_landing_volume, model

    def show_results(self):
        # This is the final step of estimation.
        new_landing_rates, new_landing_volume, model = self.check_regions()
        print("\n🏆  Моя рекомендация будет следующей: 🏆")
        print("\n--- Лендинг 📄  ---")
        budgets = {}
        for key, rate in new_landing_rates.items():

            if model == "1":
                volume = int(new_landing_volume[key])/1000
            else:
                volume = int(new_landing_volume[key])

            new_volume = format(int(new_landing_volume[key]), ",d").replace(",", " ")
            spend = volume * rate
            new_spend = format(round(spend), ",d").replace(",", " ")
            budgets[key] = spend
            new_rate = (str(rate)).replace(".", ",")
            print(f"{key}:".ljust(15) + f"ставка – {new_rate} USD".ljust(25) + f"объем – {new_volume}".ljust(20) + f"бюджет – {new_spend} USD")

        print("\n")

        for key, spend in budgets.items():
            if spend < BUDGET_BOTTOM[key]:
                difference = BUDGET_BOTTOM[key] - round(spend)
                new_difference = format(difference, ",d").replace(",", " ")
                print(f"🚨  Обрати внимание, что мы не добираем {new_difference} USD до минимального бюджета по {key}!")
            else:
                pass

    def launch_whole_process(self):
        self.show_results()
        print("\nТеперь осталось уточнить про hard или soft KPI, запрещенные источники (или недоступные по ГЕО) и не забудь учесть в оценке долю внешней сети партнеров")
        print("+ сделай тест скорости загрузки здесь: https://testmysite.withgoogle.com/intl/ru-ru и если значение выше 5 сек, то рекомендуется оптимизация.\nУдачи! 🤞\n")


class Video:
    pass


print("\nПривеееет!\n\nДавай выберем, что будем продвигать: приложение или лендинг?")
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
