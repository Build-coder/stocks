import csv

def get_last_days():

    with open('stocks.csv', 'r') as csv_file:

        csv_reader = csv.DictReader(csv_file)

        days = []
        last_days = []
        count = 0
        tracker = []

        for line in csv_reader:

            day = int(line['Date'][8])*10+int(line['Date'][9])
            days.append(day)

        for i in range(len(days)):

            count = count + 1

            if days[i-1] > days[i]:

                count = count - 2

                tracker.append(count)

                print(tracker)
                #last_days.append(str(days[i-1]))

    csv_file.close()

    return last_days


def monthly_change(last_days):

    with open('stocks.csv', 'r') as csv_file:

        csv_reader = csv.DictReader(csv_file)

        for line in csv_reader:

            date = line['Date'].split('-')


            #for string in date:

                #print(date)

                #if string in last_days:

                    #print('Date: '+line['Date'], '  Adj Close: $'+line['Adj Close'])


if __name__ == '__main__':

    lst = []

    lst = get_last_days()

    print(lst)

    monthly_change(lst)


"""

    if new_line in avj_close_days:

        #print('Date: '+line['Date'], '  Adj Close: $'+line['Adj Close'])

"""
