TARIFF_11 = 0.244518
TARIFF_31 = 0.136928

print("Electricity bill estimator")

price_per_kWh_in_cents = -1
valid_tariff_type_entered = False
while not valid_tariff_type_entered:
    tariff_type = input("Which tarrif? 11 or 31: ")
    if tariff_type == "11":
        price_per_kWh_in_cents = TARIFF_11
        valid_tariff_type_entered = True
    elif tariff_type == "31":
        price_per_kWh_in_cents = TARIFF_31
        valid_tariff_type_entered = True
    else:
        print("invalid tariff type")


# price_per_kWh_in_cents = int(raw_input("Enter cents per kWh: "))
daily_use_in_kWh = int(input("Enter daily use in kWh: "))
number_days_in_billing_period = int(input("Enter number of billing days: "))

bill_total_in_cents = daily_use_in_kWh * price_per_kWh_in_cents * number_days_in_billing_period
bill_total_in_dollars = bill_total_in_cents / 100.0
print("Estimated bill: $" + str(bill_total_in_dollars))
