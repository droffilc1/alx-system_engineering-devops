# Adds a custom HTTP header
exec { 'apt':
    command => '/usr/bin/apt update'
}

package { 'nginx':
    ensure => 'installed',
    name   => 'nginx',
}

file_line { 'append a line in nginx config file':
    path  => '/etc/nginx/nginx.conf',
    line  => "\tadd_header X-Served-By ${hostname};",
    after => 'http {',
}

exec { 'sudo service nginx restart':
    command => 'usr/sbin/service nginx restart',
}
