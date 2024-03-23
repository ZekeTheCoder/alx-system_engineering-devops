# 0x0A-configuration_management

1. File: 0-create_a_file.pp - Using Puppet, create a file in /tmp.

Requirements:
File path is /tmp/school
File permission is 0744
File owner is www-data
File group is www-data
File contains I love Puppet

2. File: 1-install_a_package.pp - Using Puppet, install flask from pip3.

Requirements:

Install flask
Version must be 2.1.0

3. File: 2-execute_a_command.pp - Using Puppet, create a manifest that kills a process named killmenow.

Requirements:

Must use the exec Puppet resource
Must use pkill
