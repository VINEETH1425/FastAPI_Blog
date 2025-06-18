# def total_price(price1 : float,price2: float) -> str:
def total_price(price1,price2:float) -> str:
    print(f'Price1 : {price1}, Price2 : {price2}, sum : {price1+price2}')
    return f'Total price : {price1+price2}'

sum = total_price('10.5',20.5)

# for checking this we can use mypy ex1.py