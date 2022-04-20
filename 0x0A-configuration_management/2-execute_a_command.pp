# - Creating a manifest that kills killmenow process
# - exec resource
# - using pkill

exec { 'pkill killmenow':
    command => '/usr/bin/pkill -f killmenow',
}