from datetime import datetime, timedelta

def get_last_week():
    d = datetime.today()
    week = []
    for day in range(1, 8):
        past_day = d - timedelta(days=day)
        week.append("{}-{}-{}".format(past_day.year, past_day.month, past_day.day))
    print (week)


if __name__ == "__main__":
    get_last_week()

