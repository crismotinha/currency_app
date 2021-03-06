from datetime import datetime, timedelta

def get_last_week(today) -> list: 
    week = []
    for day in range(1, 8):
        past_day = today - timedelta(days=day)
        week.append(past_day.strftime('%Y-%m-%d'))
    return week


if __name__ == "__main__":
    get_last_week()

