from tabulate import tabulate
def calculateIncomeTax(income):
    totalIncome = income
    totalTax = 0
    taxOnFirstPart = 0/100 * 10000
    totalTax += taxOnFirstPart
    income = income - 10000
    
    if income > 0:
        taxOnSecondPart = 10/100 * 10000
        totalTax += taxOnSecondPart
        income-= 10000
        
    if income > 0 : 
        taxOnLastPart = 20/100 * income
        totalTax += taxOnLastPart
     
    # return totalTax
    
    col_names = ["Taxable Income", "Rate"]
    data = [["First 10,000", taxOnFirstPart], 
        ["Next 10,000", taxOnSecondPart], 
        ["Remainder", taxOnLastPart],
        ['Total Income: '+str(totalIncome),'Total tax: '+str(totalTax)]
        ]
    # print(tabulate(data, headers=col_names, tablefmt='fancy_grid'))
 
    
# calculateIncomeTax(500000)