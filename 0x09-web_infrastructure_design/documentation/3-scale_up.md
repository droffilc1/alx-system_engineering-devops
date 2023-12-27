0x09. Web infrastructure design
===============================

# Task 2

## Explanations
- **For every additional element, why you are adding it:**
    - Splitting different components of a web application into their own servers is a common practice in modern web development. This approach, known as a **`microservices`** architecture, allows each component to be developed and scaled independently, which can improve the overall performance and reliability of the application.
    - In the case of an HAproxy load balancer, it is configured as a cluster when it is set up to distribute incoming traffic among multiple servers in a group, also known as a **`server farm`** or **`server pool`**. This can help to improve the performance and reliability of a system by ensuring that no single server is overwhelmed with too much traffic, and that requests can be routed to a different server if one becomes unavailable.

