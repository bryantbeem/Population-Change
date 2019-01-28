###############################################################################
# Computer Project #5
#   define functions to open file, print headers, calculate delta and display lines
#   define main function to run program
#       open file
#       for loop defining continent and max values
#           for loop using i in range of 6
#               change year and delta within text file
#               calculate max delta for each continent
#           if statement calculating max delta of all continents
#       print results
##############################################################################

def open_file(): #function to open file
    '''
    Prompt user to enter a text file
    If text file is not found, print error and ask again
    If file is found, return the file
    '''
    text_file = input("Enter a file name:") #prompt to input a file name
    while True:
        try:
            return_file = open(text_file, 'r') #reads file
            return return_file #returns file
        except FileNotFoundError: #if file is not found
            print("Error. Please try again.") #print error
            text_file = input("Enter file name:") #prompt to input a file again
            
def print_headers(): #function to print headers
    '''
    Prints the main header (Maximum Poupoulation Change by Continent)
    Prints the next headers (Continent, Years, Delta)
    '''
    print("{:^50s}".format("Maximum Population Change by Continent")) #prints main header
    print("")
    print("{:<26s}{:>9s}{:>10}".format("Continent", "Years", "Delta")) #prints next headers

def calc_delta(line,col): #function to calculate delta
    '''
    Finds population number from one year on chart
    Finds population number from the proceding year (50 years later)
    Calculates the percentage change(delta) of population over the 50 years
    '''
    i = col -1 #changes column
    data_one = int(line[15+6*i:15+6*i+6])
    data_two = int(line[(15+6*i)+6:(15+6*i+6)+6])
    delta = (data_two - data_one) / data_one #calculates change between two values
    return delta #returns change value
    
def format_display_line(continent,year,delta): #function for display format
    '''
    Turns delta into a percentage and year into an integer
    max_values = (continent name, year-50, year, delta) in specified format
    returns max_values
    '''
    
    year =  int(year) 
    max_values = ("{:<26s}{:>4d}-{:<4d}{:>10.0%}".format(continent, year-50, year, delta)) #format for continent, years and delta
    return max_values #returns the format
    
    
def main(): #main function
    '''
    Where the functions are called for
    Prints the values that are calculated
    '''
    text_file = open_file() #calls for open file function
    text_file.readline() #reads the first line in file
    years=text_file.readline() 
    max_delta_total = 0 #start max delta at 0
    max_continent_total = '' #start max continent at empty string
    max_year_total = 0 #starts max years at 0
    print_headers() #calls for print headers function
    for line in text_file: 
        max_delta = 0#starts max delta at 0
        max_years=0 #start max years at 0
        continent = line[:15].strip() #strips continent line
        for i in range(6): #range of 6 for each column of data
            year = years[15+i*6:15+(i+1)*6] 
            delta = calc_delta(line,i+1) #sets delta equal to calculate delta function
            if delta > max_delta: #finds new max delta value
                max_delta = delta 
                max_years=int(year)
        print(format_display_line(continent,max_years+50,max_delta)) #prints display line function for each continent
        if max_delta > max_delta_total: #finds max continent, years, and delta of all data
            max_delta_total = max_delta
            max_continent_total = continent
            max_year_total = max_years
    print("") #skips a line
    print("Maximum of all continents:")
    print("{:<26s}{:>4d}-{:<4d}{:>9.0%}".format(max_continent_total,max_year_total, max_year_total+50,max_delta_total)) 
    #prints max continet,years and delta of all continents and years    
if __name__ == "__main__": #calls for main function
    main()