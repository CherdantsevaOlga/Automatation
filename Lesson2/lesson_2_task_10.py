
def bank(summ, years):
    for i in range(years):
        summ += summ * 0.10  
    return summ

result = bank(2500, 15)
print(result)