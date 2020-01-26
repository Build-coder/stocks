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

        for line in csv_reader:

            date = line['Date'].split('-')

            day = date[2]


            if day == last_days[0]:

                print(line)
                print()

                last_days.pop(len(last_days)*-1)

                print(last_days)





                if last_days == []:

                    break

if __name__ == '__main__':

    lst = []

    lst = get_last_days()

    print(lst)

    monthly_change(lst)
