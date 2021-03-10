# By: Ameer Al-Shamaa
# On: 11/03/2021

def gstPrice(originalPrice):        # Construct the gstPrice function.
    originalPrice = float(originalPrice)    # Converts the input to a float
    gstPrice = round(originalPrice * 1.1, 2)    # Multiplies the non-GST price with the GST rate and round's to 2 decimal points.
    return gstPrice

