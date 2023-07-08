from cart_things import products
from datetime import datetime


N = len(products)
PRODUCTS_TO_PAY = []
PAYED_CARTS = []


# fun for add articles for a pay cart
def add_product(article: str) -> None:
    if not check_existance(article):
        print(f"{article} is not in the product list")
    else:
        article_price = find_price(article)
        PRODUCTS_TO_PAY.append([article, article_price])
      
        
# function that print the articles in the cart
def cart_products() -> None:
    ordered_products = order_cart_list(PRODUCTS_TO_PAY)
    n = len(ordered_products)
    for product in range(n):
        pro = ordered_products[product][0]
        pri = ordered_products[product][1] 
        print(pro, pri)
    
    final_cart_price = sum_prices(PRODUCTS_TO_PAY)
    print(f"El total del carrito es: {final_cart_price}")


# function for sum all products that need to be paid for
def sum_prices(products: list):
    sum_prices = 0
    n = len(products)
    for price in range(n):
        sum_prices += products[price][1]

    return sum_prices
    
    
# fun for check if a input is in a product list
def check_existance(article: str) -> bool:
    for product in range(N):
        if products[product][0] == article:
            return True
    return False
      
                
# fun for find the price of an article
def find_price(article: str) -> int: 
    for product in range(N):
        if products[product][0] == article:
            return products[product][1]
         
               
# fun for print only products
def show_products(products: list) -> None:
    for product in range(N):
        print(products[product][0])


# fun that uses bubble sort to order the list of products
# use the order algorithm that you know
def order_cart_list(products: list) -> list:
    products_ordered = products
    n = len(products_ordered)
    for i in range(n):
        for j in range(n - 1 - i):
            if products_ordered[j] > products_ordered[j + 1]:
                tmp = products_ordered[j]
                products_ordered[j] = products_ordered[j + 1]
                products_ordered[j + 1] = tmp
                
    return products_ordered

# fun that makes the id and check of payment
def pay_cart(products: list) -> None:
    pay_products = order_cart_list(products)
    n = len(pay_products)
    f = pay_products[0][0]
    f_sliced = f[0:2]
    s = pay_products[n - 1][0]
    s_n = len(s)
    s_sliced = s[s_n - 3: s_n]
    day = datetime.now()
    id = f_sliced + " " + str(day) + " " + s_sliced
    print(id)
    PAYED_CARTS.append(id)
    PRODUCTS_TO_PAY = []
    print(PRODUCTS_TO_PAY)

def show_payed_carts() -> None:
    for cart in PAYED_CARTS:
        print(cart)
   
   
def main():
    exit = False
    while not exit: 
        print("Welcome to your cart program: ", end="\n * ")
        print("Please select one of the options", end="\n  ")
        print("1.- Mostrar el carrito", end="\n  ")
        print("2.- Agregar al carrito", end="\n  ") 
        print("3.- Pagar carrito", end="\n  ")
        print("0.- Para salir")
       
        respuesta = int(input())
        if respuesta == 1:
            cart_products()
            
        if respuesta == 2:
            show_products(products)
            product = str(input("Introduce el producto que desea: "))
            add_product(product)
            
        if respuesta == 3:
            pay_cart(PRODUCTS_TO_PAY)
            PRODUCTS_TO_PAY.clear()
        
        if respuesta == 0:
            show_payed_carts()
            exit = True
            


if __name__ == "__main__":
    main()