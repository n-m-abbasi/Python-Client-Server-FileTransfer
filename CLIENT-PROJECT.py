import socket
import os

HOST = '127.0.0.1'
PORT = 5001

# لیست فایل‌هایی که می‌خوای بفرستی
files_to_send = ['file1.txt', 'file2.txt', 'file3.txt']

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# تعداد فایل‌ها
client_socket.send(str(len(files_to_send)).encode())
client_socket.recv(1024)

for filename in files_to_send:
    # نام فایل
    client_socket.send(filename.encode())
    client_socket.recv(1024)

    # اندازه فایل
    filesize = os.path.getsize(filename)
    client_socket.send(str(filesize).encode())
    client_socket.recv(1024)

    # ارسال محتوا
    with open(filename, 'rb') as f:
        remaining = filesize
        while remaining > 0:
            data = f.read(1024)
            if not data:
                break
            client_socket.send(data)
            remaining -= len(data)
    print(f"[SUCCESS] {filename} sent ({filesize} bytes)")

# دریافت فایل زیپ از سرور
with open("received_bundle.zip", 'wb') as f:
    while True:
        data = client_socket.recv(1024)
        if data == b'EOF':
            break
        f.write(data)

print("[SUCCESS] Zip file received from server.")

client_socket.close()