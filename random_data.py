import random
import string

# Hàm sinh tên khách hàng ngẫu nhiên với số ký tự xác định
def generate_random_name(length=10):
    return ''.join(random.choices(string.ascii_letters, k=length))

# Hàm sinh customerid duy nhất
def generate_unique_customerid(existing_ids):
    while True:
        customerid = "KH"+str(random.randint(1000, 999999))
        if customerid not in existing_ids:
            return customerid

# Hàm sinh orderid duy nhất
def generate_unique_orderid(existing_ids):
    while True:
        order_id = "DH"+str(random.randint(1000, 9999999))
        if order_id not in existing_ids:
            return order_id

# Hàm sinh dữ liệu ngẫu nhiên và xuất ra 2 file riêng biệt
def generate_custom_data(num_customers=100000, num_orders=200000):
    customer_ids = set()  # Tập hợp để lưu trữ các customerid duy nhất

    with open("customers.txt", "w") as customer_file, open("orders.txt", "w") as order_file:
        # Tạo dữ liệu khách hàng
        for _ in range(num_customers):
            customerid = generate_unique_customerid(customer_ids)
            customer_name = generate_random_name()
            customer_file.write(f"{customerid},{customer_name}\n")
            customer_ids.add(customerid)  # Thêm customerid vào tập hợp để kiểm tra trùng lặp

        # Tạo dữ liệu đơn hàng
        order_ids = set()  # Tập hợp để lưu trữ các orderid duy nhất
        for _ in range(num_orders):
            order_id = generate_unique_orderid(order_ids)
            customerid = random.choice(list(customer_ids))  # Chọn ngẫu nhiên 1 customerid từ danh sách đã có
            total_amount = random.randint(1, 9999999)
            order_file.write(f"{order_id},{customerid},{total_amount}\n")
            order_ids.add(order_id)  # Thêm orderid vào tập hợp để kiểm tra trùng lặp

generate_custom_data(num_customers=100000, num_orders=1000000)
