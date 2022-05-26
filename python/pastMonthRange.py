import datetime
from dateutil.relativedelta import relativedelta

month_amount = 22

today = datetime.date.today()
first_this_month = today.replace(day=1)
# https://thispointer.com/subtract-months-from-a-date-in-python/
calculated_past = first_this_month - relativedelta(months=month_amount)

print(first_this_month)
print(calculated_past.strftime("%Y-%m"))
print(first_this_month.year, first_this_month.month)
print(calculated_past.year, calculated_past.month)

# https://stackoverflow.com/a/5734564/18775205
def month_year_iter(start_year, start_month, end_year, end_month):
    # removed -1, because we need start-month exclusive and end month inclusive and not the other way around
    ym_start = 12 * start_year + start_month  # - 1
    ym_end = 12 * end_year + end_month  # - 1
    for ym in range(ym_start, ym_end):
        y, m = divmod(ym, 12)
        #yield y, m + 1
        yield '{0}-{1:0>2d}'.format(y, m + 1)


print('#' * 10)

for month in month_year_iter(calculated_past.year, calculated_past.month, today.year, today.month):
    print(month)
