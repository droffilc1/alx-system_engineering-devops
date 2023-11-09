Command line for the win
========================

-   Weight: 1

![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/324/06AChAO.png)

Background Context
------------------

[CMD CHALLENGE](https://alx-intranet.hbtn.io/rltoken/a83_NOBEtXgFr1Yqej0HYA "CMD CHALLENGE") is a pretty cool game challenging you on Bash skills. Everything is done via the command line and the questions are becoming increasingly complicated. It's a good training to improve your command line skills!

**This project is NOT mandatory** at all. It is 100% optional. Doing any part of this project will add a project grade of over 100% to your average. Your score won't get hurt if you don't do it, but if your current average is greater than your score on this project, your average might go down. Have fun!

Requirements
------------

### General

-   A `README.md` file, at the root of the folder of the project, is mandatory
-   This project will be manually reviewed.
-   As each task is completed, the name of that task will turn green
-   Create a screenshot, showing that you completed the required levels
-   Push this screenshot with the right name to GitHub, in either the PNG or JPEG format

More Info
---------

### Manual QA Review

**It is your responsibility to request a review for this project from a peer. If no peers have been reviewed, you should request a review from a TA or staff member.**

Tasks
-----

### 0\. First 九 tasks

#advanced

Complete the first 9 tasks.

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `command_line_for_the_win`
-   File: `0-first_9_tasks.jpg,0-first_9_tasks.png`

 Done? Help

### 1\. Reach חי completed tasks

#advanced

Complete the 9 next tasks, getting to 18 total.

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `command_line_for_the_win`
-   File: `1-next_9_tasks.jpg,1-next_9_tasks.png`

 Done? Help

### 2\. Reach the perfect cube, 27

#advanced

Complete the 9 next tasks, getting to 27 total.

**Repo:**

-   GitHub repository: `alx-system_engineering-devops`
-   Directory: `command_line_for_the_win`
-   File: `2-next_9_tasks.jpg,2-next_9_tasks.png`
# How To Use SFTP to Securely Transfer Files with a Remote Server

## How to Connect with SFTP

Establish an SFTP session by issuing the following command:
```bash
sftp username@your_server_ip_or_remote_hostname
```
Once you entered your password you will connect the the remote system and your prompt will change to an SFTP prompt.

## Transferring Local Files to the Remote System

Transferring files to the remote system works with a put command:
```bash
put /path/local_file /path/remote_file
```
