# Increase Nginx open files limit

exec { 'modify_nginx':
    command => 'sed -i "s/15/4096/" /etc/default/nginx',
    path    => '/usr/local/bin/:/bin/',
}

exec { 'nginx_restart':
    command => 'nginx restart',
    path    => '/etc/init.d/',
}
