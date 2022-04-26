def get_days_later(days):
  """ Helper function to format days later"""
  if days == 1:
      return "(next day)"
  elif days > 1:
      return f"({days} days later)"
  return ""

def add_time(start, duration, args=False):
    week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    [Time, Meridiem] = start.split(" ")
    [Start_Hour, colon, Start_Minutes] = Time.partition(":")
    [Duration_Hour, colon, Duration_Minutes] = duration.partition(":")

    Updated_Hour = int(Start_Hour) + int(Duration_Hour)
    Updated_Minutes = int(Start_Minutes) + int(Duration_Minutes)
    Upcoming_Day = 0


    if Updated_Minutes >= 60:
        Updated_Hour += int(Updated_Minutes / 60)
        Updated_Minutes = int(Updated_Minutes % 60)
        if Updated_Hour == 0:
            Updated_Hour = 12

    if Updated_Hour or Updated_Minutes:
        if Meridiem == "PM" and Updated_Hour > 12:
            if Updated_Hour % 24 >= 1.0:
                Upcoming_Day += 1

        if Updated_Hour >= 12:
                hours_Left = Updated_Hour / 24
                Upcoming_Day += int(hours_Left)

        total_Hours = Updated_Hour
        while True:
            if total_Hours < 12:
                break
            if total_Hours > 0:
                if Meridiem == "AM":
                    Meridiem = "PM"
                elif Meridiem == "PM":
                    Meridiem = "AM"
                total_Hours -= 12

    remaining_Hours = int(Updated_Hour) % 12 or int(Start_Hour) + 1
    remaining_Minutes = int(Updated_Minutes) % 60

    results = str(remaining_Hours) + ":" + str(remaining_Minutes).zfill(2) + f" {Meridiem}"
    print("Results=",results)

    if args:
        args = args.strip().lower()
        selected_day = int((week_days.index(args) + Upcoming_Day) % 7)
        current_day = week_days[selected_day]
        results += f', {current_day.title()} {get_days_later(Upcoming_Day)}'
    else:
        results = " ".join((results, get_days_later(Upcoming_Day)))

    return results.strip()