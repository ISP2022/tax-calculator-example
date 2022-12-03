"""Income tax calculator for Thai income tax."""

from dataclasses import dataclass
from enum import Enum
from typing import List
from person import Person


class IncomeType(Enum):
    """Income categories. The string form it printed on tax form."""
    WAGES = "Ordinary"
    INTEREST = "Interest"
    DIVIDEND = "Dividend"

    def __str__(self):
        return self.value


@dataclass(frozen=True)
class Income:
    """The data for an income item, with tax withheld."""
    income_type:  IncomeType
    descripton:   str
    amount:       float
    tax_withheld: float


class TaxCalculator:
    """Summarize the income for a tax payer, compute and print tax statement."""
    
    def __init__(self, taxpayer: Person):
        """Initialize income tax calculator.
        :param taypayer: a Person paying tax on income
        """
        self.taxpayer = taxpayer
        # incomes is an array of income items.
        self.incomes: List[Income] = []

    def add_income(self, income: Income):
        """Record an income item.
        
        :param income: an Income object describing this income item
        """
        self.incomes.append(income)

    @property
    def total_income(self) -> float:
        """The total of all income."""
        return sum(income.amount for income in self.incomes)
    
    @property
    def total_tax_withheld(self) -> float:
        """The total tax withheld on all income items."""
        return sum(income.tax_withheld for income in self.incomes)

    @property
    def total_tax(self) -> float:
        """Compute the total amount of income tax for this taxpayer.
        :return: the total tax amount.
        """
        # total each type of income
        ordinary_income = self.sum_income_by_type(IncomeType.WAGES)
        interest_income = self.sum_income_by_type(IncomeType.INTEREST)
        dividend_income = self.sum_income_by_type(IncomeType.DIVIDEND)

        # Compute the income tax on net ordinary income (wages),
        # which is the sum of all wages minus a personal exemption.
        deduction = 60000
        income_tax = self.compute_ordinary_tax(ordinary_income - deduction)
        
        # The tax on interest income.
        # First 20,000 Baht pays 0 tax, above that the tax is 15%.
        interest_tax = 0.15*max(0, interest_income-20000)

        # The tax on dividend income. The tax is a 10% fixed rate.
        dividend_tax = 0.10*dividend_income

        # A person can treat dividends and interest as ordinary income
        # if it results in a lower total tax amount.  Check that.
        total_taxable_income = ordinary_income + dividend_income
        # if interest income <= 20,000 then its not taxed, so don't include it
        if interest_income > 20000:
            total_taxable_income += interest_income 
        # Apply the ordinary tax formula to combined income
        simplified_tax = self.compute_ordinary_tax(total_taxable_income - deduction)
        # Choose the tax computation that results in the lower tax.
        total_tax = income_tax + interest_tax + dividend_tax
        if simplified_tax < total_tax:
            return simplified_tax 
        return total_tax

    def compute_tax(self):
        """Compute amount of income tax owed or amount to refund.
        :return: the amount of tax due (> 0) or amount to refund (if < 0).
        """
        return self.total_tax - self.total_tax_withheld

    def print_tax(self):
        """Print the tax form."""
        print(f"Tax Report for {self.taxpayer.first_name} {self.taxpayer.last_name}")
        print('-' * 69)
        format = "{:40s} {:12,.2f} {:12,.2f}"
        print("{:40s} {:12s} {:12s}".format("Income Type", "Total Amount", "Tax Withheld"))
        for income_type in IncomeType:
            print(format.format(str(income_type)+" Income",
                                self.sum_income_by_type(income_type),
                                self.sum_tax_withheld_by_type(income_type))
            )
        # The total tax, total withheld, and amount due/refund
        tax_withheld = self.total_tax_withheld
        total_tax = self.total_tax
        tax_owed = total_tax - tax_withheld
        print(format.format("Total Tax & Total Tax Withheld", 
                            total_tax, tax_withheld))
        
        format2 = "{:40s} {:12,.2f}"
        # Does he get a tax refund or owe additional tax?
        if tax_owed >= 0:
            print(format2.format("Amount of Tax owed", tax_owed))
        else:
            print(format2.format("Amount of Tax overpaid", -tax_owed)) 

    def sum_income_by_type(self, income_category: IncomeType):
        """Compute total income for a given income category."""
        return sum(income.amount
                   for income in self.incomes 
                    if income.income_type == income_category)

    def sum_tax_withheld_by_type(self, income_category: IncomeType):
        """Compute total tax withheld a given income category."""
        return sum(income.tax_withheld 
                   for income in self.incomes 
                    if income.income_type == income_category)

    def compute_ordinary_tax(self, income: float):
        """Compute ordinary income tax.
        
        :param income: the net taxable income after deductions.
        """
        if income <= 150000:
            return 0
        if income <= 300000:
            return 0.05*(income - 150000)
        if income <= 500000:
            return 7500 + 0.10*(income - 300000)
        if income <= 750000:
            return 27500 + 0.15*(income - 500000)
        if income <= 1000000:
            return 65000 + 0.20*(income - 750000)
        if income <= 2000000:
            return 115000 + 0.25*(income - 1000000)
        if income <= 4000000:
            return 365000 + 0.30*(income - 2000000)
        # net income over 4,000,000
        return  965000 + 0.35*(income - 4000000)
