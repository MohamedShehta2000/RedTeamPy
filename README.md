![9fdb52be-c410-45d2-bd50-d445e5cd2871](https://github.com/user-attachments/assets/389b2d2a-4c86-4edf-ab9d-b64d86fc60f7)
---

## Python Scripts Collection

This repository contains various Python scripts demonstrating different functionalities, ranging from basic file operations to object-oriented programming (OOP), threading, and hacking simulations. Below is an overview of each script:

---

### 1. **01.PythonBasic.py**
Basic operations in Python including:
- Reading from a file in Linux.
- Writing to a file in Linux.
- Executing Linux commands using Python.

---

### 2. **02.SmallProjectScan.py**
A simple project for scanning a domain using `nmap`:
- Asks the user for a domain name.
- Executes an `nmap` scan on the entered domain using the `os.system()` function.

---

### 3. **03.Generate_Keys.py**
Generates RSA keys using the `rsa` module:
- Creates a public and private key pair.
- Prints the keys to the console.

---

### 4. **04.Encrypt_with_Publickey.py**
Encryption using RSA public key:
- Generates a pair of public and private keys.
- Encrypts a test message using the public key.
- Prints the encrypted message.

---

### 5. **05.Python_For_Hacking.py**
A simple example of sending an HTTP GET request:
- Sends a GET request to a test website.
- Displays the response content and status code.

---

### 6. **06.Python_For_Hacking2.py**
An example of sending an HTTP POST request:
- Sends a POST request with a payload containing username and password.
- Prints the response content and status code.

---

### 7. **07.Python_OOP_1.py**
Basic Object-Oriented Programming concepts:
- Demonstrates list iteration and searching.
- Multiple function definitions with overloading.
- Basic OOP class examples including methods and object instantiation.

---

### 8. **08.Python_OOP_1.py**
Continuation of OOP concepts:
- Class definition and method calling.
- Using `__init__()` constructor.
- Demonstrates method chaining and object behavior.

---

### 9. **09.Python_OOP_2.py**
More OOP examples:
- Class constructors with and without parameters.
- Demonstrates default parameter values.

---

### 10. **10.Python_OOP_2.py**
Inheritance in Object-Oriented Programming:
- Demonstrates parent and child class relationships.
- Usage of `super()` to call parent class methods and constructors.

---

### 11. **Threading Examples**
- **Example 1:** Creates and starts two threads that print "Hello World" concurrently.
- **Example 2:** Creates a thread to print "Hello World" five times, using `.join()` to wait for completion.
- **Example 3:** Prints the current time five times using a thread, ensuring order with `.join()`.
- **Example 4:** Creates 10 threads to print numbers from 0 to 9, demonstrating concurrent execution.
- **Example 5:** Asks the user for their name and prints a greeting using a thread.

---

## Requirements
- Python 3.x
- Required modules:
  - `rsa` for RSA key generation and encryption.
  - `requests` for HTTP requests.

Install requirements using:
```sh
pip install rsa requests
```

---

## Usage
To run any of the scripts:
```sh
python3 script_name.py
```
Example:
```sh
python3 01.PythonBasic.py
```

---

## Notes
- Some scripts require Linux commands or tools (e.g., `nmap`).
- Make sure you have the necessary permissions to run network scans.
- These scripts are for educational purposes only. Use responsibly.

