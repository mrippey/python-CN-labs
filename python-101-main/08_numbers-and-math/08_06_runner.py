# If a runner runs 10 miles in 30 minutes and 30 seconds,
# What is their average speed in kilometers per hour?
# (Tip: 1 mile = 1.6 km)


distance_in_miles = 10
runtime_in_sec = 210 

def get_runner_kmh(dist):
    km = dist * 1.6 
    return km

runners_distance_converted = get_runner_kmh(distance_in_miles)

runner_time = runtime_in_sec / 360


km_per_hour = runners_distance_converted * runner_time 

print(f'Km/h: {km_per_hour:.2f}')