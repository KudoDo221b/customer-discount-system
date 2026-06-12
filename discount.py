def calculate_discount(donhangtruoc, donhanghtai=0):
    if donhangtruoc >= 50000000:
        return 0.1
    if donhangtruoc + donhanghtai >= 50000000:
        return 0.1
    return 0
