# Increase Nginx open files limit

exec { 'modify_nginx':
	commnad => 'sed -i "s/15/4096/" /etc/default/nginx',
	path    => '/usr/local/bin/:/bin/',
}

exec { 'nginx_restart':
	command => 'sudo systemctl nginx restart',
	path    => '/etc/init.d/',
}
