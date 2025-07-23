def main():
    while True:
        date_str = input("Date: ").strip()
        try:
            formatted_date = convert_date(date_str)
            print(formatted_date)
            break
        except ValueError:
            pass

def convert_date(date_str):
    months = {
        "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
        "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
    }

    if '/' in date_str:
        splited_date = date_str.split('/')

        if len(splited_date) == 3:
            month_num = int(splited_date[0])
            day = int(splited_date[1])
            year = int(splited_date[2])
        else:
            raise ValueError
    elif ',' in date_str:
        splited_date = date_str.replace(',','').split()
        if len(splited_date) == 3:
            month = splited_date[0]
            day = int(splited_date[1])
            year = int(splited_date[2])

            if month in months:
                month_num = months[month]
            else:
                raise ValueError("Invalid month")
        else:
            raise ValueError("3 parts")
    else:
        raise ValueError("Wrong format")
    if 0 > day or day > 31:
        raise ValueError
    if not (1 <= month_num <= 12):
        raise ValueError
    return f"{year}-{month_num:02d}-{day:02d}"

if __name__ == "__main__":
    main()
