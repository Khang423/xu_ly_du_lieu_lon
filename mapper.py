import sys

for line in sys.stdin:
    line =line.strip() #xoá khoảng trắng ở đầu và cuối dòng
    parts = line.split(",")# tách dòng dữ liệu theo dấu ","

    if len(parts) == 2:
        customer_id = parts[0]
        customer_name = parts[1]
        print(f"{customer_id}\tC,{customer_name}")
    elif len(parts) == 3:                       
        order_id = parts[0]
        customer_id = parts[1]
        order_amount = parts[2]
        print(f"{customer_id}\tO,{order_id},{order_amount}")
