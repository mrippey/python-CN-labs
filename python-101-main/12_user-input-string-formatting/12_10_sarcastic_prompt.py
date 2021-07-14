# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

users_opinion = str(input('Your honest opinion: '))
print()

res = "".join(
    users_opinion[x].upper() if x % 2 != 0 else users_opinion[x].lower()
    for x in range(len(users_opinion))
)

print(f'My sarcastic opinion: {res}')