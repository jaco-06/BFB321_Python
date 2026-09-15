#abc helps a company to categorize their inventory based on usage value, which is calculated by multiplying the demand and cost of each SKU. The SKUs are then sorted in descending order of usage value, and cumulative percentages are calculated to assign tiers (A, B, C) based on the distribution of usage value.
skus = [
    {"sku": "BRK-100", "demand": 2000, "cost": 45},
    {"sku": "GSK-220", "demand": 1500, "cost": 30},
    {"sku": "BLT-010", "demand": 10000, "cost": 2},
    {"sku": "BRG-330", "demand": 800, "cost": 60},
    {"sku": "SEAL-500", "demand": 3000, "cost": 5},
    {"sku": "MTR-700", "demand": 50, "cost": 800},
    {"sku": "WSH-050", "demand": 20000, "cost": 0.5},
    {"sku": "CBL-900", "demand": 400, "cost": 25},
    {"sku": "BBL-600", "demand": 350, "cost": 15},
    {"sku": "CAZ-400", "demand": 200, "cost": 225},
]

def usage_value(demand, cost):
    return demand * cost

for item in skus:
    item["value"] = usage_value(item["demand"], item["cost"])

skus_sorted = sorted(skus, key=lambda item: item["value"], reverse=True)

total_value = sum(item["value"] for item in skus_sorted)

running_total = 0

for item in skus_sorted:
    running_total += item["value"]
    item["cum_pct"] = (running_total / total_value) * 100

def assign_tier(cum_pct):
    if cum_pct <= 70:
        return "A"
    elif cum_pct <= 90:
        return "B"
    else:
        return "C"

for item in skus_sorted:
    item["tier"] = assign_tier(item["cum_pct"])

for item in skus_sorted:
    print(item["sku"],
          "| value:", item["value"],
          "| cum %:", round(item["cum_pct"], 1),
          "| tier:", item["tier"])

tier_counts = {"A": 0, "B": 0, "C": 0}

for item in skus_sorted:
    tier_counts[item["tier"]] += 1

print(tier_counts)

#5.1 - The tier split changed slightly, Tier A increased from 4 to 5 items and C from 2 to 3 items, but the overall pattern remained the same.
#5.2 - A:4, B:2 and C:4, the split is more balanced and reflects the distribution of usage value across the SKUs.
#5.3 -  below

def classify_inventory(skus):

    for item in skus:
        item["value"] = item["demand"] * item["cost"]

    skus_sorted = sorted(
        skus,
        key=lambda item: item["value"],
        reverse=True
    )

    total_value = sum(item["value"] for item in skus_sorted)

    running_total = 0

    for item in skus_sorted:
        running_total += item["value"]
        item["cum_pct"] = (running_total / total_value) * 100

        if item["cum_pct"] <= 80:
            item["tier"] = "A"
        elif item["cum_pct"] <= 95:
            item["tier"] = "B"
        else:
            item["tier"] = "C"

    return skus_sorted
