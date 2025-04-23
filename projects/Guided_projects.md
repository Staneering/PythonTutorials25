
---

# Cybersecurity Python Projects

## 1. Password Manager Application

### Concepts Covered:
- Variables and Data Types
- Functions
- File Handling
- OOP (Object-Oriented Programming)
- Encryption
- Exception Handling

### Project Overview:
Students will build a password manager application that allows users to securely store and retrieve their passwords for different accounts. The application should encrypt passwords before storing them and decrypt them when retrieved. The app will have basic functionalities like adding, editing, deleting, and listing passwords.

### Key Features:
- **User Authentication**: Users should be able to authenticate using a master password.
- **Password Storage**: Use encryption (e.g., AES) to store passwords securely.
- **Password Retrieval**: Decrypt and retrieve passwords when required.
- **Exception Handling**: Handle incorrect master passwords or invalid inputs.
- **OOP**: Organize the application with classes like `User`, `PasswordManager`, and `Encryption`.

### Guided Steps:
1. Set up a class `User` to handle user information and authentication.
2. Create an `Encryption` class that handles AES encryption and decryption for password storage.
3. Build a `PasswordManager` class to add, edit, delete, and retrieve passwords from a file (or a simple database).
4. Add exception handling for invalid input (e.g., weak passwords or failed authentication).
5. Test the program with various scenarios, such as incorrect master passwords and empty fields.

---

## 2. Simple Port Scanner

### Concepts Covered:
- Variables and Data Types
- Functions
- Control Structures (Loops, Conditionals)
- Exception Handling
- Networking (Socket Programming)

### Project Overview:
Students will create a simple port scanner that checks whether a particular port on a given host is open or closed. The port scanner will try connecting to various ports and report back the status.

### Key Features:
- **Port Scanning** using sockets.
- **Multithreading** (Optional) for faster scanning.
- **Exception Handling** for connection errors.
- **Reporting** open or closed ports.

### Guided Steps:
1. Create a `PortScanner` class that accepts a host IP and a range of ports.
2. Implement a function that attempts to open a socket connection to a given IP and port.
3. Use loops to iterate through a list of common ports (or user-defined ports).
4. Add exception handling for connection errors, like timeouts or unreachable hosts.
5. Optionally implement multithreading to make the scanner faster by checking multiple ports at once.

---

## 3. Log File Analyzer for Intrusion Detection

### Concepts Covered:
- Variables and Data Types
- Functions
- Control Structures (Loops, Conditionals)
- Regular Expressions (Regex)
- Exception Handling
- File Handling

### Project Overview:
Students will create a log file analyzer that scans server logs (e.g., web server logs) to detect suspicious activity or potential intrusions. The program will search for common attack patterns, such as multiple failed login attempts or SQL injection attempts.

### Key Features:
- **Log File Parsing**: Parse the log file and extract relevant information.
- **Regex**: Use regular expressions to detect malicious patterns (e.g., brute force, SQL injection).
- **Reporting**: List detected suspicious activities or failed login attempts.
- **Exception Handling**: Handle missing or malformed logs.

### Guided Steps:
1. Create a `LogAnalyzer` class that reads and parses log files.
2. Implement regex patterns to match malicious activity (e.g., SQL injection, failed login attempts).
3. Build a function that checks if any suspicious activity is detected and logs it.
4. Add exception handling for file errors (e.g., file not found).
5. Output a summary report of the analysis, showing how many suspicious events were detected.

---

## 4. Simple Network Chat Application (Client-Server)

### Concepts Covered:
- Variables and Data Types
- Functions
- OOP (Classes)
- Networking (Socket Programming)
- Exception Handling
- File Handling (Optional)

### Project Overview:
Students will build a simple chat application that allows multiple users to send messages to each other over a network. This application will consist of a server that handles multiple clients and a client that can send and receive messages.

### Key Features:
- **Socket Programming**: Use sockets for client-server communication.
- **Threading**: Handle multiple clients using multithreading.
- **OOP**: Organize the server and client into classes.
- **Exception Handling**: Handle connection errors and disconnections.

### Guided Steps:
1. Create a `ChatServer` class to accept incoming client connections.
2. Create a `ChatClient` class to allow users to send and receive messages.
3. Use threading to manage multiple clients connecting to the server simultaneously.
4. Implement exception handling for network issues, timeouts, and disconnections.
5. Optional: Add file logging for message history or store the last N messages in a file.

---

## 5. Simple Vulnerability Scanner for Web Applications

### Concepts Covered:
- Variables and Data Types
- Functions
- Networking (HTTP Requests)
- Regular Expressions (Regex)
- Exception Handling
- OOP

### Project Overview:
Students will create a web vulnerability scanner that checks websites for common vulnerabilities like SQL injection, cross-site scripting (XSS), or directory traversal. The scanner will attempt to find these vulnerabilities by making requests to the website and analyzing the responses.

### Key Features:
- **HTTP Requests**: Use Python’s `requests` module to interact with websites.
- **Regex**: Use regex to search for malicious patterns in responses.
- **Reporting**: Output a list of detected vulnerabilities.
- **Exception Handling**: Handle connection errors or unexpected responses.

### Guided Steps:
1. Create a `VulnerabilityScanner` class that accepts a target URL and scans for vulnerabilities.
2. Use `requests` to interact with the website and send requests to test for vulnerabilities (e.g., SQL injection, XSS).
3. Apply regex to analyze the response and detect common attack patterns.
4. Implement exception handling for network errors and invalid URLs.
5. Output a list of vulnerabilities detected along with suggestions for remediation.

---

## 6. Building a Custom Cybersecurity Module: Password Strength Checker

### Concepts Covered:
- Variables and Data Types
- Functions
- OOP (Object-Oriented Programming)
- Exception Handling
- Modules and Libraries

### Project Overview:
Create a custom Python module that checks the strength of a password based on customizable security criteria. The module will evaluate if a password meets basic security requirements such as length, uppercase letters, special characters, and numbers.

### Key Features:
- **Password Strength Scoring**
- **Regular Expressions (Regex)** for pattern matching
- **Customization for password criteria**
- **Exception Handling** for invalid passwords
- **Reusable module**

### Guided Steps:
1. Define a `PasswordStrengthChecker` class to check password criteria (length, numbers, special characters).
2. Create functions to evaluate the presence of uppercase letters, special characters, etc.
3. Implement exception handling for invalid inputs (e.g., empty passwords).
4. Add unit tests to ensure the password strength checker works for different types of passwords.
5. Package the code as a reusable Python module that can be imported into other projects.

---

### Conclusion

These projects will help you apply Python concepts from **basic syntax** to **advanced networking and security tools**. By the end of the course, you'll have a solid understanding of how to use Python for practical **cybersecurity tasks** such as **password management**, **port scanning**, **log file analysis**, and more.

---
