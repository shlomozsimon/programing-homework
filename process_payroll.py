"""
Processes employee payroll information and creates
a pay stub for each employee.
"""

import utilities


# this function calculates the employee's base pay and overtime pay
def calculate_pay(hours, rate):
    """
    Calculates an employee's base pay and overtime pay.

    Args:
        hours (float): The number of hours worked.
        rate (float): The employee's hourly pay rate.

    Returns:
        tuple: The employee's base pay and overtime pay.
    """

    # checks if the employee worked overtime
    if hours > 40:
        base_pay = 40 * rate
        overtime_pay = (hours - 40) * rate * 1.5

    else:
        base_pay = hours * rate
        overtime_pay = 0

    return base_pay, round(overtime_pay, 2)


# this function creates a formatted pay stub for an employee
def create_pay_stub(name, hours, rate, base_pay, overtime_pay):
    """
    Creates a formatted pay stub for an employee.

    Args:
        name (str): The employee's name.
        hours (float): The number of hours worked.
        rate (float): The employee's hourly pay rate.
        base_pay (float): The employee's regular pay.
        overtime_pay (float): The employee's overtime pay.

    Returns:
        str: The formatted employee pay stub.
    """

    # calculates the employee's gross pay
    gross_pay = base_pay + overtime_pay

    # creates the employee's pay stub
    pay_stub = (
        f"Employee Name: {name}\n"
        f"   ----- Gross Pay Calculation ------\n"
        f"   Hours Worked: {hours:7.2f}\n"
        f"       Pay Rate: $ {rate:7.2f} per hour\n"
        f"       Base Pay: $ {base_pay:7.2f}\n"
        f"   Overtime Pay: $ {overtime_pay:7.2f}\n"
        f"      Gross Pay: $ {gross_pay:7.2f}\n"
        "\n"
        "-------------------- Cut Here -------------------------------\n"
        "\n"
    )

    return pay_stub


# this function processes one employee's information
def process_employee(line):
    """
    Processes one employee's payroll information.

    Args:
        line (str): A line containing the employee's name,
                    hours worked, and hourly pay rate.

    Returns:
        str: The employee's formatted pay stub.
    """

    # separates the employee's information
    name, hours, rate = line.strip().split(",")

    # converts hours and rate into floats
    hours = float(hours)
    rate = float(rate)

    # calculates the employee's pay
    base_pay, overtime_pay = calculate_pay(hours, rate)

    # creates and returns the employee's pay stub
    return create_pay_stub(
        name, hours, rate, base_pay, overtime_pay
    )


# this function processes the entire payroll file
def process_payroll(input_file, output_file):
    """
    Reads employee information and writes their pay stubs.

    Args:
        input_file: An open file containing employee information.
        output_file: An open file where pay stubs will be written.

    Returns:
        None.
    """

    # reads each line in the input file
    for line in input_file:

        
        # skips blank lines and comment lines
        if not line.strip() or line.startswith("#"):
            continue

        # processes the employee's information
        pay_stub = process_employee(line)

        # writes the pay stub to the output file
        output_file.write(pay_stub)


# this function runs the payroll program
def main():
    """
    Runs the payroll program.

    Args:
        None.

    Returns:
        None.
    """

    # gets the payroll input file
    input_file = utilities.get_file(
        "Enter the name of the payroll input file: "
    )

    # gets the name of the output file
    output_file_name = utilities.ask_user_str(
        "Enter the name of the payroll output file: "
    )

    # opens the output file and processes the payroll
    with input_file:
        with open(output_file_name, "w") as output_file:

            process_payroll(input_file, output_file)

    print("Payroll processing complete.")


if __name__ == "__main__":
    main()