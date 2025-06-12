a, b, c = (map(int, input().split()))

k = float(a) # homozygous dominant
m = float(b) # heterozygous
n = float(c) # homozygous recessive

population_size = k + m + n

p_rr = (n*(n-1) + n*m + 0.25*m*(m-1))/(population_size*(population_size-1))
p_rr = round(1 - p_rr, 5)

print(p_rr)