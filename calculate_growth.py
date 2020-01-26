
import csv

def get_last_days():

    with open('stocks.csv', 'r') as csv_file:

        csv_reader = csv.DictReader(csv_file)

        days = []
        last_days = []

        for line in csv_reader:

            day = int(line['Date'][8])*10+int(line['Date'][9])
            days.append(day)


        for i in range(len(days)):

            if days[i-1] > days[i]:

                date = days[i-1]

                last_days.append(str(date))

    csv_file.close()

    return last_days



def monthly_change(last_days):

    with open('stocks.csv', 'r') as csv_file:

        csv_reader = csv.DictReader(csv_file)

        adj_close = []

        for line in csv_reader:

            date = line['Date'].split('-')

            day = date[2]


            if day == last_days[0]:

                print(line['Adj Close'])
                #print(line['Avj Close'])
                print()

                adj_close.append(float(line['Adj Close']))

                last_days.pop(len(last_days)*-1)


                if last_days == []:

                    break

    value_change = calculate_change(adj_close)

    csv_file.close()

    return value_change



def calculate_change(adj_close):

    value_change = []

    for price in range(len(adj_close)-1):

        difference = adj_close[1] - adj_close[0]
        pre_percentage = difference / adj_close[0]
        percentage_change = pre_percentage * 100

        value_change.append(percentage_change)

        adj_close.pop(len(adj_close)*-1)

        #print(adj_close)

    return value_change


def print_change(change)

    for price in change:







if __name__ == '__main__':

    lst = []

    lst = get_last_days()

    #print(lst)

    change = monthly_change(lst)

    print(change)

