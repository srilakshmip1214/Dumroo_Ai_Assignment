from datetime import date, timedelta

def get_dates(period):
    today = date.today()
    if period == "last_week":
        start = today - timedelta(days=today.weekday() + 7)
        end = start + timedelta(days=6)
    elif period == "next_week":
        start = today + timedelta(days=(7 - today.weekday()))
        end = start + timedelta(days=6)
    elif period == "this_week":
        start = today - timedelta(days=today.weekday())
        end = start + timedelta(days=6)
    else:
        start = None
        end = None
    return start, end
