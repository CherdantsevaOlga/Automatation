year=2000
def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False
resultat=is_year_leap(year)
print('Год {year}:{resultat}')