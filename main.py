"""Demonstrate use of Income Tax Calculator."""
from tax_calculator import *
from person import Person

if __name__ == '__main__':
    fatalai = ("1409900123456", "Fatalai", "Jon")
    tax_calc = TaxCalculator(fatalai)
    # income types are wages, interest, dividend, and other
    tax_calc.add_income("wages", "Kasetsart University", 290000, 10000)
    tax_calc.add_income("interest", "Bangkok Bank", 12000, 0)
    tax_calc.add_income("dividend", "SCC", 15000, 1500)
    tax_due = tax_calc.compute_tax()

    if tax_due > 0:
        print(f"You owe {tax_due:,.2f} Baht additional tax. Sorry." )
    else:
        print(f"Good news! You get a tax refund of {-tax_due:,.2f}.")
    
    print("")
    taksin = Person("3409900123456", "Taksin", "Shinawat")
    big_tax = TaxCalculator(taksin)
    big_tax.add_income("wages", "CEO salary", 8000000, 0)
    big_tax.add_income("dividend", "AIS",     4000000, 400000)
    big_tax.add_income("dividend", "Intouch", 4000000, 400000)
    big_tax.add_income("interest", "Bank of Dubai", 2000000, 0)

    tax_due = big_tax.compute_tax()

    if tax_due > 0:
        print(f"Sorry, you owe {tax_due:,.2f} Baht additional tax.")
    else:
        print(f"Good news! You get a tax refund of {-tax_due:,.2f}.")