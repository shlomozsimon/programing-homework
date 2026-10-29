from utilities import get_file


def main():
    # get the file with the sales numbers
    input_file = get_file("Enter sales file name: ")

    # ask the user what to name the file with the totals
    output_file_name = input("Enter name for total sales file: ")

    # open the output file to write the numbers and totals
    output_file = open(output_file_name, "w")

    # go through each row in the sales file
    for line in input_file:

        # split the row into a list of sales numbers
        sales = line.split()

        # start the total at zero for each row
        total = 0

        # add up all the sales numbers in the row
        for sale in sales:
            # remove the dollar sign and convert the number to a float
            amount = float(sale.replace("$", ""))
            total = total + amount

        # write each sales number to the output file
        for sale in sales:
            # remove the dollar sign and convert the number to a float
            amount = float(sale.replace("$", ""))

            # format the number to have two decimal places and line up
            output_file.write("$ " + format(amount, "8.2f") + "  ")

        # write the total for the row at the end
        output_file.write("$ " + format(total, "8.2f") + "\n")

    # close both files when finished
    input_file.close()
    output_file.close()

    # tell the user the file has been created
    print("Done writing totals to " + output_file_name)


if __name__ == "__main__":
    main()