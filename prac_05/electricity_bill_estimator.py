TARIFFS = {"11": 0.244518, "31": 0.136928, "35": 0.35, "70": 0.70, "99": 0.99}

print("Electricity bill estimator")

price_per_kWh_in_cents = -1
valid_tariff_type_entered = False
while not valid_tariff_type_entered:
    prompt = "Which tariff? " + " or ".join(TARIFFS.keys()) + ": "
    tariff_type = input(prompt)
    if tariff_type in TARIFFS.keys():
        price_per_kWh_in_cents = TARIFFS[tariff_type]
        valid_tariff_type_entered = True
    else:
        print("invalid tariff type")

daily_use_in_kWh = int(input("Enter daily use in kWh: "))
number_days_in_billing_period = int(input("Enter number of billing days: "))

bill_total_in_cents = daily_use_in_kWh * price_per_kWh_in_cents * number_days_in_billing_period
bill_total_in_dollars = bill_total_in_cents / 100.0
print("Estimated bill: $" + str(bill_total_in_dollars))
