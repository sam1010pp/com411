"""
This module is responsible for processing the data.  Each function in this module will take a list of records,
process it and return the desired result.
"""
import tui

"""
Task 16 - 20: Write suitable functions to process the data.

Each of the functions below should follow the pattern:
- Take a list of records (where each record is a list of data values) as a parameter.
- Process the list of records appropriately.  You may use the module 'tui' to retrieve any additional information 
required from the user to complete the processing.
- Return a suitable result

The required functions are as follows:
- Retrieve the total number of records that have been loaded.
- Retrieve a record with the serial number as specified by the user.
- Retrieve the records for the observation dates as specified by the user.
- Retrieve all of the records grouped by the country/region.
- Retrieve a summary of all of the records. This should include the following information for each country/region:
    - the total number of confirmed cases
    - the total number of deaths
    - the total number of recoveries

 



# TODO: Your code here
"""# taking a list of records
list = {
        'confirmed': [],
        'deaths': [],
        'recoveries': []  #
    }
temp_serial_number = tui.serial_number()
#retriving serial number
if temp_serial_number:
    # is it a number
    if isinstance(temp_serial_number, int):
        # does it successfully refer to a row that exists in our records that is not 0 (row 0 contains column
        # titles)
        temp_serial_number = int(temp_serial_number)
        if tui.serial_number[temp_serial_number]:
            # everything seems fine, lets post the data
            tui.display_serial(temp_serial_number, serial_record[temp_serial_number], cols=[])







def grouping_by_country_region(grouping_records):
    return None