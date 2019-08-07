'''
Calculate the greatest common divisor (GCD) among a pair of values
Input: There will always be two integers passed to the solution
'''
# The most efficient way to calculate the GCD is probably
# with the euclidean algorithm (which is implemented here)
def Euclidean(x, y):
    maximum = max(x, y)
    minimum = min(x, y)
    if maximum % minimum == 0:
        return minimum
    left = maximum
    Q = minimum
    r = 1
    prev = r
    while r > 0:
        prev = r
        r = left % Q
        left = Q
        Q = r
    return prev
print(Euclidean(24, 100))
