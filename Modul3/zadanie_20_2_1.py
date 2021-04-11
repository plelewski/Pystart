def calc_elec_cost(hours_spent: float, consumption: float, price: float = 0.617):
    return hours_spent * consumption * price

print(calc_elec_cost(8, 0.5))
print(calc_elec_cost(1, 2))
