number_of_customers = 0
movie_title = ""
customer_name = ""

print("Hello\n","Please enter movie title: ")
movie_title = input()
print("Enter number of customers: ")
number_of_customers = int(input())

i = 0
for j in range(0, number_of_customers):
    print("Enter customer name" + str(j) + ": ")
    customer_name = input()
# while (i < number_of_customers):
#     print("Enter customer name" + str(i) + ": ")
#     customer_name = input()
#     i = i + 1

print("Report: \nMovie title: ", movie_title, "\nNumber of customers: ", number_of_customers)

# i = 0
# while (i < number_of_customers):
#     print("Customer", i, customer_name, "\n")
#     i += 1

for j in range(number_of_customers):
    print("Customer", j, customer_name, "\n")