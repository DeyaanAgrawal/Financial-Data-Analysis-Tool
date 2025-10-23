import numpy as np

#Data 
revenue = [14574.49, 7606.46, 8611.41, 9175.41, 8058.65, 8105.44, 11496.28, 9766.09, 10305.32, 14379.96, 10713.97, 15433.50]
expenses = [12051.82, 5695.07, 12319.20, 12089.72, 8658.57, 840.20, 3285.73, 5821.12, 6976.93, 16618.61, 10054.37, 3803.96]

profit = (np.array(np.subtract(revenue,expenses)))
profit_rounded = np.round(profit)

#print(profit_rounded)
tax = np.round(30/100*profit)
#print(tax)
profit_after_tax = np.round(profit - tax)
#print(profit_after_tax)

profit_margin = np.round(profit_after_tax/revenue, 2)
#print(profit_margin)

profit_after_tax_mean = np.round(np.mean(profit_after_tax))
#print(profit_after_tax_mean)

good_months = (profit_after_tax > profit_after_tax_mean)
#print(good_months)

bad_months = (profit_after_tax < profit_after_tax_mean)
#print(bad_months)

best_month = ((profit_after_tax == max(profit_after_tax)))
#print(best_month)

worst_month = ((profit_after_tax == min(profit_after_tax)))
#print(worst_month)

revenue_1000 = (np.divide(revenue, 1000)).astype(int)
expenses_1000 = (np.divide(expenses, 1000)).astype(int)
profit_1000 = (np.divide(profit, 1000)).astype(int)
profit_after_tax_1000 = (np.divide(profit_after_tax, 1000)).astype(int)

#Print Results 

print("Revenue : ")
print(revenue_1000)
print("Expenses : ")
print(expenses_1000)
print("Profit : ")
print(profit_1000)
print("Profit_after_tax :")
print(profit_after_tax_1000)
print("Good Months :")
print(good_months)
print("Bad Months :")
print(bad_months)
print("Best Month :")
print(best_month)
print("Worst Month :")
print(worst_month)