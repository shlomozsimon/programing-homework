from utilities import get_user_input


def calculate_base_pay(hours, rate):
    return hours * rate


def calculate_overtime_pay(hours, rate):
    if hours > 40:
        overtime_hours = hours - 40
        return overtime_hours * (rate * 0.5)
    else:
        return 0


def main():
    hours = get_user_input("Enter the number of hours worked: ", False)
    rate = get_user_input("Enter the hourly pay rate: ", False)

    base_pay = calculate_base_pay(hours, rate)
    overtime_pay = calculate_overtime_pay(hours, rate)

    total_wages = base_pay + overtime_pay

    print("Total wages for the week: $", format(total_wages, ".2f"))


if __name__ == "__main__":
    main()