def calculate_seconds_in_year():
    DAYS_IN_YEAR = 365
    HOURS_IN_DAY = 24
    MINUTES_IN_HOUR = 60
    SECONDS_IN_MINUTE = 60
    
    return DAYS_IN_YEAR * HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE


def main():
    seconds = calculate_seconds_in_year()
    print(f"There are {seconds} seconds in a year!")


if __name__ == "__main__":
    main()
