# Adapted from: https:
def sqrt(x):
    # Inital guess
    z = 1.0
    # Keep getting a better estimate for the sqaure root
    # of x, until you are withtin two decimal places.
    while abs(z*z - z) >= 0.01:
        # Get a better approximation
        z -= (z*z - x) / (2*z)
    
    return z