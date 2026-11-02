
# import the necessary functions from utilities
from utilities import ask_user_str, get_user_choice, get_csv_file


def get_search_type():
    # ask the user how they want to search
    search_type = get_user_choice(
        "Search by invoice id (id) or customer last name (lname)? ",
        ["id", "lname"] # valid choices for the search type
    )

    return search_type


def find_sales(search_type, search_term):

    # get the sales data from the csv file
    sales_records = get_csv_file(r"C:\Users\SHLOMO SIMON\Desktop\programing homework\sales_data.csv")

    # determine which column to search
    if search_type == "id":
        search_column = "invoice_id"
    else:
        search_column = "customer_last_name"

    # keep track of how many records match
    record_count = 0

    # search through each record in the file
    for record in sales_records:

        # check if the search term matches the selected column
        if record[search_column].lower() == search_term.lower():

            # print the matching record without the field names, just the values separated by commas
            print(",".join(record.values()))

            # increase the number of matching records
            record_count += 1

    # print the number of matching records
    print("{} records found.".format(record_count))


def main():

    # get the type of search from the user
    search_type = get_search_type()

    # ask the user for their search term
    search_term = ask_user_str("Enter your search term: ")

    # search the sales records
    find_sales(search_type, search_term)


if __name__ == "__main__":
    main()
