print("WELCOME TO THE IPV4 VALIDATOR")
print("\nThis program checks whether four numbers can form a valid IPv4 address.\n"
    "An IPv4 address contains four octets separated by dots.\n"
    "Each octet is an 8-bit value and must be between 0 and 255.\n"
    "Example: 192.168.1.10\n")

first_octet = int(input("Enter First Octet: "))
second_octet = int(input("Enter Second Octet: "))
third_octet = int(input("Enter Third Octet:  "))
fourth_octet= int(input("Enter Fourth Octet: "))

ip_address = (f"{first_octet}.{second_octet}.{third_octet}.{fourth_octet}")
print(f"\nIP Address: {ip_address}")

if (first_octet >= 0 and first_octet <=255 and second_octet >= 0 and 
    second_octet <= 255 and third_octet >= 0 and third_octet <=255 and 
    fourth_octet >= 0 and fourth_octet <= 255):
    print("Result: Valid IPv4 Address")
else:
    print("Result: Invalid IPv4 Address")