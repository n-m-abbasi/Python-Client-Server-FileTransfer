import socket
import zipfile
import os

HOST = '127.0.0.1'
PORT = 5001

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print("[INFO] Server is listening...")

conn, addr = server_socket.accept()
print(f"[INFO] Connected by {addr}")

num_files = int(conn.recv(1024).decode())
conn.send(b'ACK')
print(f"[INFO] Expecting {num_files} files...")

# پوشه‌ی ذخیره‌سازی فایل‌های دریافتی
save_dir = "received_files"
os.makedirs(save_dir, exist_ok=True)

received_files = []

for i in range(num_files):
    filename = conn.recv(1024).decode()
    conn.send(b'ACK')
    filesize = int(conn.recv(1024).decode())
    conn.send(b'ACK')

    # ذخیره با نام جدید در پوشه‌ی جدا
    save_path = os.path.join(save_dir, f"received_{i}_{filename}")
    with open(save_path, 'wb') as f:
        remaining = filesize
        while remaining > 0:
            data = conn.recv(min(1024, remaining))
            if not data:
                break
            f.write(data)
            remaining -= len(data)
    received_files.append(save_path)
    print(f"[SUCCESS] Received {filename} -> saved as {save_path}")

zip_filename = "files_bundle.zip"
with zipfile.ZipFile(zip_filename, 'w') as zipf:
    for file in received_files:
        zipf.write(file)

print("[INFO] Zip file created.")

with open(zip_filename, 'rb') as f:
    while True:
        data = f.read(1024)
        if not data:
            break
        conn.send(data)
conn.send(b'EOF')

print("[SUCCESS] Zip file sent back to client.")

conn.close()
server_socket.close()