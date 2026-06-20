def calculate_emi(principal, rate, time):
       """Calculate EMI for a loan using the formula: EMI = P * r * (1+r)^n / ((1+r)^n - 1)."""
       try:
           if not (isinstance(principal, (int, float)) and isinstance(rate, (int, float)) and isinstance(time, (int, float))):
               raise TypeError("Principal, rate, and time must be numbers")
           if principal <= 0 or rate <= 0 or time <= 0:
               raise ValueError("Principal, rate, and time must be positive")
           monthly_rate = rate / (12 * 100)  # Convert annual rate to monthly decimal
           months = time * 12  # Convert years to months
           emi = principal * monthly_rate * (1 + monthly_rate)**months / ((1 + monthly_rate)**months - 1)
           return round(emi, 2)
       except (TypeError, ValueError) as e:
           return str(e)