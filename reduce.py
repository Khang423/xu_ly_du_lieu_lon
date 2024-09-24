import sys

current_customer_id = None
current_customer_name = None
orders = []

for line in sys.stdin:
    line = line.strip()
    customer_id, value = line.split("\t", 1)

    value_parts = value.split(",")
    record_type = value_parts[0]

    if customer_id != current_customer_id:
        # Chỉ in kết quả khi cả customer và order đều tồn tại
        if current_customer_id is not None and current_customer_name is not None:
            for order in orders:
                print(
                    f"{current_customer_id},{current_customer_name},{order[0]},{order[1]}"
                )

        current_customer_id = customer_id
        current_customer_name = None
        orders = []

    if record_type == "C":
        current_customer_name = value_parts[1]
    elif record_type == "O":
        order_id = value_parts[1]
        order_amount = value_parts[2]
        orders.append((order_id, order_amount))

# Xử lý bản ghi cuối cùng
if current_customer_id is not None and current_customer_name is not None:
    for order in orders:
        print(f"{current_customer_id},{current_customer_name},{order[0]},{order[1]}")
