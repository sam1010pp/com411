"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done using the appropriate functions in the module 'tui'
        any processing should be done using the appropriate functions in the module 'process'
        any visualisation should be done using the appropriate functions in the module 'visual'
"""


# Task 10: Import required modules
# TODO: Your code here
from _csv import reader

import process
import tui
import __main__
import visual
# Task 11: Create an empty list named 'covid_records'.
# This will be used to store the data read from the source data file.
# TODO: Your code here
covid_records = []

def run(retriaval_records=None, summarise_records=None, grouping_records=None):
    # Task 12: Call the function welcome of the module 'tui'.
    # This will display our welcome message when the program is executed.
    # TODO: Your code here
    tui.welcome()

    # Task 13: Load the data.
    # - Use the appropriate function in the module 'tui' to display a message to indicate that the data loading
    # operation has started.
    # - Load the data. Each line in the file should be a record in the list 'covid_records'.
    # You should appropriately handle the case where the file cannot be found or loaded.
    # - Use the appropriate functions in the module 'tui' to display a message to indicate how many records have
    # been loaded and that the data loading operation has completed.
    # TODO: Your code here
    operation = "Loading data\n"

    tui.progress(operation, 0)

    with open("data/covid_19_data.csv.csv") as csv_file:
        csv_reader = reader(csv_file)

        for row in csv_reader:
            covid_records.append(row)

    tui.progress(operation, 100)

    while True:
        # Task 14: Using the appropriate function in the module 'tui', display a menu of options
        # for the different operations that can be performed on the data (menu variant 0).
        # Assign the selected option to a suitable local variable
        # TODO: Your code here
        print("\nPlease select an option:")

        tui.menu(0)

        variant = int(input())

        # Task 15: Check if the user selected the option for processing data.  If so, then do the following:
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has started.
        # - Process the data (see below).
        # - Use the appropriate function in the module tui to display a message to indicate that the data processing
        # operation has completed.
        #
        # To process the data, do the following:
        # - Use the appropriate function in the module 'tui' to display a menu of options for processing the data
        # (menu variant 1).
        # - Check what option has been selected
        #
        #   - If the user selected the option to retrieve an individual record by serial number then
        #       - Use the appropriate function in the module 'tui' to indicate that the record retrieval process
        #       has started.
        #       - Use the appropriate function in the module 'process' to retrieve the record and then appropriately
        #       display it.
        #       - Use the appropriate function in the module 'tui' to indicate that the record retrieval process has
        #       completed.
        #
        #   - If the user selected the option to retrieve (multiple) records by observation dates then
        #       - Use the appropriate function in the module 'tui' to indicate that the records retrieval
        #       process has started.
        #       - Use the appropriate function in the module 'process' to retrieve records with
        #       - Use the appropriate function in the module 'tui' to display the retrieved records.
        #       - Use the appropriate function in the module 'tui' to indicate that the records retrieval
        #       process has completed.
        #
        #   - If the user selected the option to group records by country/region then
        #       - Use the appropriate function in the module 'tui' to indicate that the grouping
        #       process has started.
        #       - Use the appropriate function in the module 'process' to group the records
        #       - Use the appropriate function in the module 'tui' to display the groupings.
        #       - Use the appropriate function in the module 'tui' to indicate that the grouping
        #       process has completed.
        #
        #   - If the user selected the option to summarise the records then
        #       - Use the appropriate function in the module 'tui' to indicate that the summary
        #       process has started.
        #       - Use the appropriate function in the module 'process' to summarise the records.
        #       - Use the appropriate function in the module 'tui' to display the summary
        #       - Use the appropriate function in the module 'tui' to indicate that the summary
        #       process has completed.
        # TODO: Your code here
        if variant == 1:

            operation = "Data processing\n"

            tui.progress(operation, 0)

            print("Please select an option:")

            tui.menu(variant)

            option = int(input())
            if option == 1:
                operation_option_1 = "Serial number retrieval process\n"

                tui.progress(operation_option_1, 0)
            process.serial_number(tui.serial_number)
            tui.progress(operation_option_1, 100)
            if option == 2:
                operation_option_2 = "Serial number retrieval process\n"

                tui.progress(operation_option_2, 0)

                process.serial_by_criteria(tui.serial_number)

                tui.progress(operation_option_2, 100)

            if option == 3:
                operation_option_3 = "Grouping process\n"

                tui.progress(operation_option_3, 0)
                process.grouping_by_country_region(grouping_records)
                tui.progress(operation_option_3, 100)

            if option == 4:
                operation_option_4 = "Summary process\n"

                tui.progress(operation_option_4, 0)

                process.summarise_data(summarise_records)

                tui.progress(operation_option_4, 100)

            if option == 5:
                tui.menu(0)

            tui.progress(operation, 100)


        # Task 21: Check if the user selected the option for visualising data.
        # If so, then do the following:
        # - Use the appropriate function in the module 'tui' to indicate that the data visualisation operation
        # has started.
        # - Visualise the data by doing the following:
        #   - call the appropriate function in the module 'tui' to determine what visualisation is to be done.
        #   - call the appropriate function in the module 'visual'
        # - Use the appropriate function in the module 'tui' to display a message to indicate that the
        # data visualisation operation has completed.
        # TODO: Your code here
        elif variant == 2:

            operation = "Data visualisation\n"

            tui.progress(operation, 0)

            print("Please select an option:")

            tui.menu(variant)

            option = int(input())
            tui.progress(operation, 100)


        # Task 25: Check if the user selected the option for exporting data.  If so, then do the following:
        # - Use the appropriate function in the module 'tui' to retrieve the type of data to be exported.
        # - Check what option has been selected
        #
        # - Use the appropriate function in the module 'tui' to indicate that the export operation has started.
        # - Export the data (see below)
        # - Use the appropriate function in the module 'tui' to indicate that the export operation has completed.
        #
        # To export the data, you should demonstrate the application of OOP principles including the concepts of
        # abstraction and inheritance.  You should create suitable classes with appropriate methods.
        # You should use these to write the records (either all or only those for a specific country/region) to a JSON file.
        # TODO: Your code here
        elif variant == 3:

            operation = "Exporting data\n"

            tui.progress(operation, 0)

            print("Please select an option:")

            tui.menu(variant)

            option = int(input())

            if option == 1:
                pass

            if option == 2:
                pass

            if option == 3:
                tui.menu(0)

            tui.progress(operation, 100)


        # Task 26: Check if the user selected the option for exiting the program.
        # If so, then break out of the loop
        # TODO: Your code here
        elif variant == 4:
            tui.menu(4)

        # Task 27: If the user selected an invalid option then use the appropriate function of the
        # module tui to display an error message
        # TODO: Your code here
        else:
            tui.error("Invalid option selected.\n")

        pass  # can remove


if __name__ == "__main__":
    run()
