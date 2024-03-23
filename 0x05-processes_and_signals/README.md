## 0x05-processes_and_signals

### Mandatory(9)
1. File: 0-what-is-my-pid - Write a Bash script that displays its own PID.
2. File: 1-list_your_processes - Write a Bash script that displays a list of currently running processes
3. File: 2-show_your_bash_pid - write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process.
4. File: 3-show_your_bash_pid_made_easy - Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash.
5. File: 4-to_infinity_and_beyond - Write a Bash script that displays To infinity and beyond indefinitely.
6. File: 5-dont_stop_me_now - Write a Bash script that stops 4-to_infinity_and_beyond process using kill.
7. File: 6-stop_me_if_you_can - Write a Bash script that stops 4-to_infinity_and_beyond process.
8. File: 7-highlander - Write a Bash script that displays:
- To infinity and beyond indefinitely
- With a sleep 2 in between each iteration
- I am invincible!!! when receiving a SIGTERM signal
9. File: 8-beheaded_process - Write a Bash script that kills the process 7-highlander.

### Advanced(3)
1. File: 100-process_and_pid_file - Write a Bash script that:
- Creates the file /var/run/myscript.pid containing its PID
- Displays To infinity and beyond indefinitely
- Displays I hate the kill command when receiving a SIGTERM signal
- Displays Y U no love me?! when receiving a SIGINT signal
- Deletes the file /var/run/myscript.pid and terminates itself when receiving a SIGQUIT or SIGTERM signal

2. File: 101-manage_my_process, manage_my_process - 
* Write a manage_my_process Bash script that:
- Indefinitely writes I am alive! to the file /tmp/my_process
- In between every I am alive! message, the program should pause for 2 seconds

* Write Bash (init) script 101-manage_my_process that manages manage_my_process. (both files need to be pushed to git)

3. File: 102-zombie.c - Write a C program that creates 5 zombie processes.
