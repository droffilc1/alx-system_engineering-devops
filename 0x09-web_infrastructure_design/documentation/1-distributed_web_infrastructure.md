0x09. Web infrastructure design
===============================

# Task 1

## Explanations

- **For every additional element, why you are adding it:**
To improve its performance or handle higher workloads.
- **What distribution algorithm your load balancer is configured with and how it works:**
The Load Balancer has different algorithms for how it divides up the workload, such as:
    - Round Robin - Requests are sequenciaaly distributed to the next server in a circular manner.
    - Least Connections -Directs new requests to the server with the fewest active connections.
    - IP Hash - The IP address of the client is used to determine which server the request will be directed to after calculating the hash value based on client's IP addresses.
    - Least response time - Considers response time of servers and directs the response to the server with the lowest response time.
- **Is your load-balancer enabling an Active-Active or Active-Passive setup, explain the difference between both:**
Load balancers operates in either of these two modes:
    - Active-Active: All resources linked to the load balancer are active and running. It distributes traffic among resources using the selected distribution algorithm. This mode offers high scalability, utilization, and fault tolerance but can be complex to manage.
    - Active-Passive: In this mode, one resource runs while others are on standby. They come into play when the primary resource fails. While offering high availability, it has a failover time, causing brief service interruptions.
- **How a database Primary-Replica (Master-Slave) cluster works:**
A database Primary-Replica (Master-Slave) cluster aka master-slave is a database architecture divided into a master database and slave databases. The slave database serves as the backup for the master database. The master database is used for the write operations, while read operations may be spread on multiple slave databases.
- **What is the difference between the Primary node and the Replica node in regard to the application:**
The primary node handles all operations (CRUD), while the replica node is read-only

## Issues:
- **Where are SPOF:**
They are in DNS as there may be DNS spoofing attacks.
- **Security issues (no firewall, no HTTPS):**
    - Firewall - Absence of a firewall means less security based on preconfigured rules in the hardware or software, no analyzing data packets that request entry to the network.
    - HTTPS - The data exchange is not secure as we are using HTTP protocol switching to HTTPS ensures encryption to secure data exchange between the clinet and the web server.
- **No monitoring:**
Sotfware monitoring will watch computer metrics, record them, and emit an alert if something is unusual or that could make the computer not work properly happens.
