def calculate_discount(price,discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
price = float(input("enter the original price: "))
discount_percent =float(input("enter the dicount_percentage: "))
final_price = calculate_discount(price, discount_percent)
if discount_percent >= 20:
    print("discount appllied!")
    print("final_price", final_price)
else:
    print("no dicount applied!")
    print("original_price", price)