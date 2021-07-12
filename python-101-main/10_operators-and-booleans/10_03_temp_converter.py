# Fahrenheit to Celsius:
# ----------------------
# Write the necessary code to convert a degree in Fahrenheit
# to Celsius and print it to the console. Use variable names!

# Conversion formula: C = (F - 32) * .5556


get_degree_farenheit = float(input('Enter degrees in fareneit: '))

conversion_to_celsius = (get_degree_farenheit - 32) * .5556

print(f'Degrees Celsius: {conversion_to_celsius:.2f}')


