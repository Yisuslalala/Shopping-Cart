from cart_things import products



N = len(products)
PRODUCTS_TO_PAY = []
PAYED_CARTS = []


# fun for add articles for a pay cart
def add_product(article: str) -> None:
    # show_products(products)
    if not check_existance(article):
        print(f"{article} is not in the product list")
    else:
        article_price = find_price(article)
        PRODUCTS_TO_PAY.append([article, article_price])
      
        
# function that print the articles in the cart
def cart_products(products: list) -> None:
    ordered_products = order_cart_list(products)
    n = len(ordered_products)
    for product in range(n):
        pro = ordered_products[product][0]
        pri = ordered_products[product][1] 
        print(pro, pri)
    
    final_cart_price = sum_prices(ordered_products)
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
    n = len(products)
    f = products[0][0]
    f_sliced = f[0:2]
    s = products[n - 1][0]
    
    print(f_sliced)
    print(s)
    
    
    pass
def main():
    exit = False
    while not exit: 
        print("Welcome to your cart program: ", end="\n * ")
        print("Please select one of the options", end="\n  ")
        print("1.- Mostrar el carrito", end="\n  ")
        print("2.- Agregar al carrito", end="\n  ") 
        # use show_products dentro de la condición para simular que se imprimen antes de 
        # agregar y una variable que se le pasará a add_product para agregar este mismo.
        print("3.- Pagar carrito") 
        # TODO Agregar a lista de carritos pagados 
        # (Primeras 2 letras del primer producto)+(fecha)+(últimas 3 letras del último producto)
        respuesta = int(input())
        if respuesta == 1:
            cart_products(PRODUCTS_TO_PAY)
            pass
        if respuesta == 2:
            show_products(products)
            product = str(input())
            add_product(product)
        if respuesta == 3:
            pay_cart(PRODUCTS_TO_PAY)
            
    # add_product("Melón")
    # print(PRODUCTS_TO_PAY)
    
    
    
if __name__ == "__main__":
    main()
    # print(PRODUCTS_TO_PAY)
    # melon_price = find_price("Melón")
    # print(melon_price)
    # add_product("Melón")
    # add_product("Cacahuates")
    # add_product("Chamarra")
    # add_product("Laptop")
    # print(PRODUCTS_TO_PAY) 
    # print(sum_prices(PRODUCTS_TO_PAY))
    # 
    # cart_products(PRODUCTS_TO_PAY)