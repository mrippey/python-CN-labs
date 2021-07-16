# Add a Google-style docstring to the function below. Your docstring
# should at least describe what it does, what arguments it takes,
# and what it returns.

def km_to_miles(km):
    """km_to_miles Function.

    Args:
        km: The first parameter. For kilometers

    Returns:
        Conversion to miles by multiplying arg by 0.6
        output to miles

    """
    miles = km * 0.6
    return miles

print(km_to_miles.__doc__)
