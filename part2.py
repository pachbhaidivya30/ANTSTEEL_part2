def production_per_month(production_rate_per_hour,no_of_working_days,utilization,Anticipated_product_mix):
    production_per_month=(production_rate_per_hour*no_of_working_days*(utilization/100)*(Anticipated_product_mix/100)*24)/12
    return production_per_month

def production_per_year(production_rate_per_hour,no_of_working_days,utilization,Anticipated_product_mix):
    production_per_year=(production_rate_per_hour*no_of_working_days*(utilization/100)*(Anticipated_product_mix/100)*24)
    return production_per_year

if __name__ == '__main__':
    production_rate_per_hour=float(input("Enter production rate per hoour in tons/m3: "))
    no_of_working_days=float(input("Enter the no. of working days per year: "))
    utilization=float(input("Enter the utilization in %: "))
    Anticipated_product_mix=float(input("Enter anticipated product mix in %: "))
    print("Production rate per month is: ",production_per_month(production_rate_per_hour,no_of_working_days,utilization,Anticipated_product_mix))
    print("Production rate per month is: ",production_per_year(production_rate_per_hour, no_of_working_days, utilization, Anticipated_product_mix))
    
    

