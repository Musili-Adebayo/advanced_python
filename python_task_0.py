# print challenge - Print the following text using a single print statement: 
# "Your Learning Path: 
# - Python Baics
# - Data Engineering
#  - AI"
print("""Your Learning Path:
\t-Python Baics
\t-Data Engineering
\t -AI""")

# A sample use case
print("---------------------------")
price_shirt = 20
price_pants = 30

qty_shirt = 2
qty_pants = 1

total_shirt = price_shirt * qty_shirt
total_pants = price_pants * qty_pants
subtotal = total_shirt + total_pants
print("Subtotal:", subtotal)
discount = 0.1 * subtotal
final_total = subtotal - discount
print("Final Total:", final_total)

print("---------------------------")
#working with variables
# print the following three lines.
#Add a variable  to make it dynamic.
# info@datamusiliadebayo.com
# support@musiliadebayo.com
# www.musiliadebayo.com

name = "musiliadebayo"
print("info@", name, ".com")
print("support@", name, ".com")
print("www.", name, ".com")