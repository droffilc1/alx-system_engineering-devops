0x09. Web infrastructure design
===============================

# Task 2

## Explanations
- **For every additional element, why you are adding it:**
    - **3 firewalls:**
    This ensures that only authorized users and devices can establish connections, reducing the risk of unauthorized access and potential data breaches.
    - **1 SSL certificate:**
    To serve www.foobar.com over HTTPS, Secure Sockets Layer (SSL) ensures the encryption of data transmitted between clients and the server, providing data integrity and authentication.
    - **3 monitoring clients:**
    This enables us to watch computer metrics, record them, and emit an alert if something is unusual or that could make the computer not work properly happens. 
- **What are firewalls for:**
A Firewall is used to monitor and filter incoming and outgoing network traffic based on an organization's previously established security policies.
- **Why is the traffic served over HTTPS:**
To ensure data exchange is secure and encryption to secure data exchange between the client and the web server.
- **What monitoring is used for:**
Monitoring is used for watching computer metrics, record them, and emit an alert if something is unusual or that could make the computer not work properly happens.
- **How the monitoring tool is collecting data:**
The methods employed for data collection depend on the type of monitoring, the components being monitored, and the architecture of the system. Common methods used by monitoring tools to collect data are:
    - Agent-Based Monitoring
    - SNMP (Simple Network Management Protocol)
    - API-Based Integration
    - Log Parsing
- **Explain what to do if you want to monitor your web server QPS:**
To monitor web server QPS, select a tool like Prometheus, install its agent on the server, and configure QPS monitoring with set thresholds and alerts. Scale infrastructure and optimize configurations based on insights, adjusting monitoring configurations periodically. Monitor additional metrics like response time and error rates. Conduct load testing for simulated traffic scenarios. This proactive approach ensures real-time awareness of web server performance, aiding in timely adjustments and optimization to meet changing demands.

## Issues:
- **Why terminating SSL at the load balancer level is an issue:**
Terminating SSL certificate at the load balancer is an issue because if the master goes down, the Application cannot write to the database anymore.
- **Why having only one MySQL server capable of accepting writes is an issue:**
Having only one MYSQL server capable of accepting writes is an issue because this poses several significant issues, especially in terms of reliability, performance, and scalability.
- **Why having servers with all the same components (database, web server and application server) might be a problem:**
While having servers with identical components (database, web server, and application server) may seem straightforward, it can lead to certain challenges and limitations in terms of flexibility, scalability, and resource optimization.
