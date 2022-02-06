from datetime import date, datetime

def get_today():
    return datetime.now().date()

class Person:
    def __init__(self, h, w, byear, bmonth, bday):
        self.height = float(h)
        self.weight = float(w)
        self.birthday = date(byear, bmonth, bday)

    def calc_bmi(self):
        print(f"BMIは{self.weight / (self.height ** 2)}です")

    def calc_elapsed_days(self):
        print(f"生まれてから{(get_today() - self.birthday).days}日です")

    def calc_days_to_birthday(self):
        today = get_today()
        this_year_bitrhday = self.birthday.replace(year=today.year)

        if this_year_bitrhday > today:
            # 今年の誕生日はまだ
            result = (this_year_bitrhday - today).days
        elif this_year_bitrhday == today:
            # 今日が誕生日
            print("誕生日おめでとうございます!")
            result = 365
        else:
            # 今年の誕生日はもう過ぎている
            next_year_birthday = self.birthday.replace(year=today.year+1)
            result = (next_year_birthday - today).days

        print(f"次の誕生日まであと{result}日です")


kawaemon = Person(1.72, 50.2, 2003, 7, 8)
kawaemon.calc_bmi()
kawaemon.calc_elapsed_days()
kawaemon.calc_days_to_birthday()
