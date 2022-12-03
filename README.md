## Simplified Income Tax Calculator

Example code after applying refactorings.

### Types of Income and Tax Rates

There are 3 kinds of income: "wages" (*aka* ordinary), "dividend", and "interest".

| Income type | Tax                                        |
|-------------|--------------------------------------------|
| Wages       | 0 - 35% (see table below)                  |
| Interest    | 0 for first 20,000, 15% of amount > 20,000 |
| Dividend    | 10% tax on all dividends                   |

## Tax Rates for Ordinary Income

The tax is computed on "net income" which is ordinary income minus a 60,000 Bt personal exemption (deduction).

The tax on *net income* is:

| Net income         | Tax Rate        |
|--------------------|-----------------|
| 0 - 150,000        | zero            |
| 150,000 - 300,000  | 5% of amount above 150,000 |
| 300,000 - 500,000  | 7,500 + 10% of amount above 300,000 |
| 500,000 - 750,000  |27,500 + 15% of amount above 500,000 |
| 750,000 - 1,000,000 | 65,000 + 20% of amount above 1,000,000 |
| 1,000,000 - 2,000,000 | 115,000 + 25% of amount above 1,000,000 |
| 2,000,000 - 4,000,000 | 365,000 + 30% of amount above 2,000,000 |
| more than 4,000,000 | 965,000 + 35% of amount above 2,000,000 |

## Simplified Tax Computation

A person can elect to treat dividends and/or interest income as "ordinary" income and use the tax formula for ordinary income.  His tax liability is whichever computation results in lower tax.

If your interest income is below 20,000 Bt then it is tax exempt, hence you should never include it as "ordinary income".

Treating dividend income as ordinary income is helpful if your margin tax rate on ordinary income is 5%. For interest income the calculation is trickier, since if you treat interest as ordinary income you don't get the 20,000 Bt deduction. 


