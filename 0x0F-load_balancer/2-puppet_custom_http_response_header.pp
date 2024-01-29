# Adds a custom HTTP header
exec { 'apt-update':
    command => '/usr/bin/apt update',
    path    => ['/usr/bin', '/usr/sbin'],
}

package { 'nginx':
    ensure => 'installed',
    name   => 'nginx',
}

file_line { 'nginx-custom-header':
    path    => '/etc/nginx/nginx.conf',
    line    => "\tadd_header X-Served-By ${hostname};",
    after   => 'http {',
    require => Package['nginx'],
}

service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File_line['nginx-custom-header'],
}
