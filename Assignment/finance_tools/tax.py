def calculate_tax(income, tax_rate=0.2):
       """Calculate tax based on income and tax rate."""
       try:
           if not (isinstance(income, (int, float)) and isinstance(tax_rate, (int, float))):
               raise TypeError("Income and tax rate must be numbers")
           if income < 0 or tax_rate < 0:
               raise ValueError("Income and tax rate cannot be negative")
           return round(income * tax_rate, 2)
       except (TypeError, ValueError) as e:
           return str(e)