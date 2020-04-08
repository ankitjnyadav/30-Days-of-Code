'''
Problem Statement - https://www.hackerrank.com/challenges/30-nested-logic/problem
'''

def calc_fine(actual_date,expected_date):
    fine = 0
    actual_date,expected_date = actual_date.split(' '),expected_date.split(' ')
    actual_month,expected_month = int(actual_date[1]),int(expected_date[1])
    actual_day,expected_day = int(actual_date[0]),int(expected_date[0])
    actual_year,expected_year = int(actual_date[2]),int(expected_date[2])

    #print('{}-{}-{}'.format(actual_day,actual_month,actual_year))
    #print('{}-{}-{}'.format(expected_day, expected_month, expected_year))


    if expected_year <= actual_year:
        if expected_month == actual_month and expected_year == actual_year:
            fine = 15 * (actual_day-expected_day)
        elif expected_month < actual_month and expected_year == actual_year:
            fine = 500 * (actual_month-expected_month)
        elif expected_year < actual_year:
            fine = 10000
    print(fine)


actual_date = input('')
expected_date = input('')
calc_fine(actual_date,expected_date)
