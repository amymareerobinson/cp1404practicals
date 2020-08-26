"""
CP1404 2020 - Practice & Extension
Student Name: Amy Robinson
Program - Electricity Bill
"""

# print("Electricity bill estimator")
#
# cents_per_kWh = float(input("Enter cents per kWh: "))
# daily_use_kWh = float(input("Enter daily use in kWh: "))
# number_billing_days = int(input("Enter number of billing days: "))
#
# estimated_bill = (cents_per_kWh/100) * daily_use_kWh * number_billing_days
#
# print(f"Estimated bill: ${estimated_bill:.2f}")


print("Electricity bill estimator 2.0")

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

tariff = int(input("Which tariff? 11 or 31: "))
if tariff == 11:
    tariff = TARIFF_11
else:
    tariff = TARIFF_31

daily_use_kWh = float(input("Enter daily use in kWh: "))
number_billing_days = int(input("Enter number of billing days: "))

estimated_bill = tariff * daily_use_kWh * number_billing_days

print(f"Estimated bill: ${estimated_bill:.2f}")
