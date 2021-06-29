# Reducer 2 Python script - Used to obtain accident count for each make and year

import sys

# Initialize accident count dictionary to keep track
acc_count_info = {}


# Flush out reducer key and values with function
def flush():
    """
    Output of function is to return combination of make and year as key and count as value.

    :return:
    """
    for key in acc_count_info.keys():
        print(f'{key}\t{acc_count_info[key]}')


# for line in sys.stdin:
#     line = line.strip()
#     make_year, acc_count = line.split('\t')
#     # Remove unnecessary characters
#     acc_count = int(acc_count.replace("'", "").replace("(", "").replace(")", ""))
#
#     # If vin is not present in dictionary, create a new entry
#     if make_year not in acc_count_info:
#         acc_count_info[make_year] = 0
#
#     acc_count_info[make_year] += acc_count
#
# # Flush output
# flush()

for line in sys.stdin:
    line = line.strip()
    make_year, acc_count = line.split('\t')
    print(make_year)  # TODO: Debug --> I have this: ('Mercedes', '2015)') --> Want this: (' Mercedes', ' 2015')
    # print(acc_count)
    # break

    acc_count = int(acc_count.replace("'", "").replace("(", "").replace(")", ""))  # Do I need this?
    # acc_count = int(acc_count)
    # acc_count = int(acc_count.replace("'", "").replace('(', '').replace(')', '').replace(',', '').replace(' ', ''))
    print(acc_count)

    # TODO: Debug ValueError.
    # ValueError: invalid literal for int() with base 10: "'A', '', ''"

    # Why do I have this as one of the possible counts? Maybe I need to look back to other Python scripts that
    # need editing.

    # print(acc_count)
    # break

    # if vin is not present in the dictionary create a new entry
    if make_year not in acc_count_info:
        acc_count_info[make_year] = 0

    acc_count_info[make_year] += acc_count

flush()
