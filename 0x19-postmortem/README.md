# Postmortem Report: Portfolio Website Outage - September 17, 2023

The following is the incident report for my portfolio website outage on the blog section that occurred on September 17, 2023. I understand this service issue has significantly impacted my website's functionality or user experience, and I apologize to everyone affected.

## Issue Summary
From 7:00 AM to 10:00 AM UTC, requests to Hashnode APIs resulted in 404 error responses, impacting the blog section of the website. The root cause was traced to a discontinued API endpoint change.

Timeline (all times Universal Time Coordinated):
- 7:00 AM: Endoint change
- 7:05 AM: Issue begins
- 9:26 AM: Get alerted 
- 9:30 AM: Server restarts begin
- 10:00 AM: 100% of traffic back online

## Root Cause

An API endpoint change at 7:19 AM resulted in an invalid address being specified, causing the blog section to malfunction and return 404 errors.

## Resolution and recovery

At 9:26 AM, a user alerted me to the issue, and by 9:40 AM, the root cause was identified. By 9:45 AM, full resolution was achieved.

## Corrective and Preventative Measures

In the recent days, I conducted a review and analysis of the issue.

The following are actions I will be taking to address the underlying causes of the issue and to help prevent recurrence and improve response times:

- Set up automated monitoring tools to regularly check the health and performance of the blog fetching system. This includes monitoring API endpoints, server status, and response times to detect any anomalies proactively.
- Stay proactive with regular maintenance tasks such as updating dependencies, patching security vulnerabilities, and optimizing performance.
- Implement redundancy and failover mechanisms to ensure resilience in case of server failures or network issues
- Develop a better mechanism for quickly delivering status notifications during incidents.
- I may consider migrating the blog to my own domain to avoid any issues in the future

I write it as a blog post on [Hashnode](https://cliffordmapesa.hashnode.dev/postmortem-report-portfolio-website-outage-september-17-2023)
