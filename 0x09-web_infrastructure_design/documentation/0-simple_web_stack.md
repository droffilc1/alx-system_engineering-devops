0x09. Web infrastructure design
===============================

# Task 0

## Explanations

- **What is a server:**
 A server is a computer hardware or software accessible within a network that provides functionality
 for other programs or devices.
- **What is the role of the domain name:**
The domain name allows users to access websites without knowing the associated IP address of the websites
- **What type of DNS record www is in www.foobar.com:**
www is a canonical name (CNAME) type of DNS record
- **What is the role of the web server:**
The role of a web server is to deliver web pages through handling HTTP requests.
- **What is the role of the application server:**
An application server serves business logic to application programs through any number of protocols
- **What is the role of the database:**
A database's role is to create, edit, and maintain database files and records, enabling easier file and record creation, data entry, data editing, updating, and reporting.Also handles data storage, backup and reporting, multi-access control, and security.
- **What is the server using to communicate with the computer of the user requesting the website:**
The server uses HTTP protocol to communicate.

## Issues

- **Single Point of Failure (SPOF):**
The infrastrure design system has a flaw since it has no redundancy that can help prevent any SPOFs.Any failure causes the whole system to stop working.
- **Downtime when maintenance needed (like deploying new code web server needs to be restarted):**
In this infrastrure design system downtime will occur because we only have one server and one database, that is used to make the deployment and maintenance hence no way users will access the website during deployment or maintainance.
- **Cannot scale if too much incoming traffic:**
The infrastrure design system cannot scale if there is too much incoming traffic as one server will not be able to handle that hence the system will be overloaded.

