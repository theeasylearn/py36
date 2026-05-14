#write a program to calculate gst on given sales price. gst rate will 18%. display sale price, gst and bill price 
sales_price = float(input("Enter Sales price")) 
gst = float(input("Enter GST rate"))

#calculate gst amount 
gst = (sales_price * gst) / 100
bill_price = sales_price + gst 
print(f"Sales Price = {sales_price} \ngst = {gst} \n Bill Price = {bill_price}")

