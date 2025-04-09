#!/usr/bin/
def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount if the discount is 20% or higher.
    
    Parameters:
    price (float): The original price of the item.
    discount_percent (float): The discount percentage to be applied.
    
    Returns:
    float: The final price after applying the discount (if applicable), otherwise the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
def main():
    try:
        price = float(input("Enter the original price: "))
        discount_percent = float(input("Enter the discount percent: "))
        
        final_price = calculate_discount(price, discount_percent)
        
        if discount_percent >= 20:
            print(f"Final price after {discount_percent}% discount is: ${final_price}")
            
        else:
            print(f"No discount applied. original price: ${final_price}")
            
    except ValueError:
        print("Enter a valid number")

if __name__ == "__main__":
    main()    