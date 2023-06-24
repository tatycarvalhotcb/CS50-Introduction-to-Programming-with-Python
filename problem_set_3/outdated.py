def iso_date_format():
    #set a variable with a list for months
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

    #loop through the input so the user can be reprompt when input is not valid
    while True:
        #set a variable with the user input, use strip to avoid extra spaces
        date = input("Date: ").strip()

        #check if date is in the mm/dd/yyyy format
        if "/" in date:
            try:
                #if true, separate the input with the / separator
                a_month, a_day, a_year = date.split("/")
                #set month, day and year to integers so it can be used in comparation operators
                a_month = int(a_month)
                a_day = int(a_day)
                a_year = int(a_year)

                #check month, day and year with the appropriate values needed
                if a_month <= 12 and a_day <= 31 and a_year != 0:
                    #if true, print the new format and break the loop
                    print(f"{a_year}-{a_month:02}-{a_day:02}")
                    break
                else:
                    continue
            #break the loop if error or inputted control-d
            except ValueError:
                continue
            except EOFError:
                break
        #check if date is in the "September 8, 1636" format
        elif "," in date:
            try:
                #set this variable input_date to False and set to true after if all the requirements met
                input_date = False
                #loop through the months list and check if input starts with any month in the months list
                for month in months:
                    if date.startswith(month):
                        #if true, separate the input with the space as a separator
                        b_month, b_day, b_year = date.split(" ")
                        #remove "," by replacing for empty value
                        b_day = b_day.replace(",", "")
                        #set day and year to integers so it can be used in comparation operators
                        b_day = int(b_day)
                        b_year = int(b_year)
                        #check if month is in months list
                        if b_month in months:
                            #if true, since the months are in a numeric order, get the index of the month inputted and sum 1 (index begins at 0)
                            number_month = months.index(b_month) + 1
                            #check day and year with the appropriate values needed
                            if b_day <= 31 and b_year != 0:
                                #if true, print the new format and set the variable input_date to True
                                print(f"{b_year}-{number_month:02}-{b_day:02}")
                                input_date = True
                    else:
                        continue
                #check if the variable input_date is true and break the loop
                if input_date:
                    break
            #break the loop if error or inputted control-d
            except ValueError:
                continue
            except EOFError:
                break

#call the function
iso_date_format()