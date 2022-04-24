# Connecting to a server executing a puppet command.

exec { 'echo "PasswordAuthentication no\nIdentityFile ~/.ssh/school" >> /etc/ssh/ssh_config':
    path    => '/usr/bin:/usr/sbin:/bin'
}