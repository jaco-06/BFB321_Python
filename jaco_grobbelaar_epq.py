#this model calculates the optimal batch size for a company so that total costs and holding inventory is minimalized.
#
import math

def calculate_epq(demand, setup, hold_cost, d_rate, p_rate):
    return math.sqrt((2 * demand * setup) / (hold_cost * (1 - d_rate / p_rate)))

annual_demand = 12000
setup_cost = 50
holding_cost = 2
daily_demand_rate = 40
daily_production_rate = 100000

epq = calculate_epq(annual_demand, setup_cost, holding_cost,
                     daily_demand_rate, daily_production_rate)
runs_per_year = annual_demand / epq
run_length_days = epq / daily_production_rate
max_inventory = epq * (1 - daily_demand_rate / daily_production_rate)

print("Optimal production quantity:", round(epq, 2))
print("Production runs per year:", round(runs_per_year, 2))
print("Length of each run (days):", round(run_length_days, 1))
print("Maximum inventory level:", round(max_inventory, 2))

#Q5.1 - Increasing the production rate reduced the optimal production quantity from 1000 to 866 units, it makes sense because a faster production rate will result into inventory that can be replenished quicker.
#Q5.2 - Because the EPQ model accounts for the inventory buildup during production runs, when production rate becomes so large the gradual eplenishment effect becomes negligible.
#  it provides a more accurate representation of the optimal production quantity compared to the EOQ model.