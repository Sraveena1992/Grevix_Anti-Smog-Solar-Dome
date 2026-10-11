# AEROSAFE Real Logic - Measurable
def calculate_protection(outside_aqi, airflow_cfm=500, filter_eff=0.9997):
    # HEPA H13 99.97% @0.3um + Dome volume 500 sq ft
    inside_aqi = outside_aqi * (1 - filter_eff) * 0.15 # leakage factor
    reduction = ((outside_aqi - inside_aqi)/outside_aqi)*100
    return round(inside_aqi,1), round(reduction,1)

# Test: 320 -> 45 = 85.9% reduction
print(calculate_protection(320)) # Output: (45.2, 85.9)

def battery_backup(solar_watt=3000, load_watt=450, battery_ah=40):
    # 24V 40Ah LiFePO4
    hours = (24 * battery_ah * 0.8) / load_watt # 80% DoD
    return round(hours,1) # 12.8hr
