dateList = ['2019-01-01', '2019-01-02', '2019-02-01', '2020-03-01']

dates = {}


for date in dateList:
    thisDate = date.split('-')
    
    year = thisDate[0]
    month = thisDate[1]
    day = thisDate[2]
    
    try:
        dates[year][month] = {}
        dates[year][month][day] = {}
    except:
        dates[year] = {
            month : {
                day : {
                }
            }
        }
    
print(dates)
print(dates.keys())
for year in dates.keys():
    print('The months in ' + year + ' are: ' + str(dates[year].keys()))
