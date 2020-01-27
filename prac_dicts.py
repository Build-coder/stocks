
def find_dates():
    with open('stocks.csv','r') as csv_file:

        content = csv_file.readlines()

        dates = []

        for line in content:
            csv = line.split(',')
            date = csv[0]

            hyphen_free = date.split('-')

            dates.append(hyphen_free)

        dates.pop(len(dates)-1)
        dates.pop(0)

        dictReader = []

        for date in dates:
            Dict = {
                'Year': date[0],
                'Month': date[1],
                'Day': date[2],
            }

            dictReader.append(Dict)

        for date in dictReader:
            print(date['Month'], date['Day'])



if __name__ == '__main__':

    dates = find_dates()
