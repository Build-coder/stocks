# stocks

is to read it in
and isolate the last price of every month
and calculate the percentage change from the previous months price
youll want to use the "Adj Close" price

(p2 - p1)/(p1)
= return
or percentage change

so dec 31 2019 is 293.65
and nov 29 2019 is 267.25

293.65 - 267.25 = 26.40
26.40/267.25 = 0.0988

0.0988 * 100 = 9.88%
so close to a 10% increase in value?

yup looks right
thats a good monthly return!
put $1000 in get $1100 out

so with this exercise youll practice reading files, working with dates, and a little bit about finance 
and it can be built upon too

---------------------------------------------------------------------
1.) how do I isolate the last day of each month? just look for first of the month then go back 1
2.) subtract last month Adj Close with month prior to that = difference
3.) divide difference by month prior = pre_percentage
4.) pre_percentage multiply by 100 = percentage_change
5.) write each percentage_change to csv file?
