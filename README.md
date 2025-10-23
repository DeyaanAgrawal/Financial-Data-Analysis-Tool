# Financial-Data-Analysis-Tool
A Python project analyzing business performance using NumPy

# Financial Data Analysis Tool (Python, NumPy)

This project analyzes monthly revenue and expenses to calculate profit, taxes, and profit margins using NumPy.  
It identifies good, bad, best, and worst performing months based on post-tax profit.

## Concepts Used
- NumPy arrays and vectorized operations  
- Basic financial analysis (profit, tax, margin)
- Logical indexing and comparison

##  How to Run
1. Clone or download this repository  
2. Run `financial_analysis.py` in any Python IDE or terminal  
3. View printed results in the console

## Example Output

Revenue : 
[14  7  8  9  8  8 11  9 10 14 10 15]
Expenses :
[12  5 12 12  8  0  3  5  6 16 10  3]
Profit :
[ 2  1 -3 -2  0  7  8  3  3 -2  0 11]
Profit_after_tax :
[ 1  1 -2 -2  0  5  5  2  2 -1  0  8]
Good Months :
[ True False False False False  True  True  True  True False False  True]
Bad Months :
[False  True  True  True  True False False False False  True  True False]
Best Month :
[False False False False False False False False False False False  True]
Worst Month :
[False False  True False False False False False False False False False]


Created by **Deyaan Agrawal**  
