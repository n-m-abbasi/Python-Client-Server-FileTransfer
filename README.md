# Simple Client/Server File Transfer (Python)

This project implements a simple **Client/Server file transfer system** using **TCP sockets** in Python.  
The client sends multiple files to the server, the server stores them, bundles them into a ZIP archive, and sends the ZIP file back to the client.

This project was developed for the **Special Topics** course and demonstrates practical networking, file handling, and socket programming concepts.

---

## 🚀 Features

- TCP-based communication between client and server  
- Sending multiple files sequentially  
- Server-side file storage  
- Automatic ZIP creation on the server  
- Returning the ZIP file to the client  
- Chunk-based file transfer  
- ACK messages for synchronization  

---

## 🧩 Architecture Overview

```
Client  →  sends multiple files  →  Server
Server  →  bundles files into ZIP →  Client
```

The communication is fully bidirectional and uses simple ACK signals to ensure correct data transfer.

---

## 📁 Project Structure

```
project/
│
├── client.py
├── server.py
├── LICENSE
└── README.md
```

The folder `received_files/` is automatically created by the server and does not need to be included in the repository.

---

## ▶️ How to Run

### 1) Start the Server
Run the server first:

```bash
python server.py
```

The server listens on port **5001** for incoming connections.

### 2) Run the Client
After the server is running, start the client:

```bash
python client.py
```

The client will send all files listed in `files_to_send`.

---

## 📤 Client Behavior

The client:

- Sends the number of files  
- Sends each filename  
- Sends each file size  
- Sends file content in chunks  
- Receives the final ZIP file from the server  

The received ZIP file is saved as:

```
received_bundle.zip
```

---

## 📥 Server Behavior

The server:

- Receives the number of files  
- Receives each file and stores it in `received_files/`  
- Creates a ZIP archive containing all received files  
- Sends the ZIP file back to the client  
- Closes the connection  

The generated ZIP file is:

```
files_bundle.zip
```

---

## 🧪 Example Server Output

```
[INFO] Server is listening...
[INFO] Connected by ('127.0.0.1', 50312)
[INFO] Expecting 3 files...
[SUCCESS] Received file1.txt -> saved as received_files/received_0_file1.txt
[SUCCESS] Received file2.txt -> saved as received_files/received_1_file2.txt
[SUCCESS] Received file3.txt -> saved as received_files/received_2_file3.txt
[INFO] Zip file created.
[SUCCESS] Zip file sent back to client.
```

---

## 🔒 Security Notes (Optional Improvements)

- Add checksum validation  
- Limit maximum file size  
- Block dangerous file types  
- Use TLS for encrypted communication  
