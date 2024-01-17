## command_line_for_the_win

### Advanced Tasks(3)
1. File: 0-first_9_tasks.png - Complete the first 9 tasks.
2. File: 1-next_9_tasks.png - Complete the 9 next tasks, getting to 18 total.
3. File: 2-next_9_tasks.png - Complete the 9 next tasks, getting to 27 total.

#### Steps followed to use the SFTP command-line tool

1. Took screenshots of the completed levels and saved them on my local machine.
Open a terminal on my local machine from the same directory as the screenshoots.

2. Use the `sftp` command to connect to the remote host. Replaced username with my actual username, and hostname with the provided host address:
```
sftp username@hostname
```
Enter your password when prompted.

3. Once connected, navigated to the destination directory on the remote host. Using the `cd` command to change to that directory:
```cd /root/alx-system_engineering-devops/command_line_for_the_win/```

4. Use the `put` command to upload the screenshots from your local machine to the sandbox.
```put 0-first_9_tasks.png```
```put 1-first_9_tasks.png```
```put 2-first_9_tasks.png```

5. Verified the screenshots have been successfully transferred by checking the contents of the sandbox directory using `ls` command.
```ls```

6. Exit the SFTP session using the 'exit' command.
```exit```
