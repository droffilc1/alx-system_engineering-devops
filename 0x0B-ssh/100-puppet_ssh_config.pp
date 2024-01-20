# using Puppet to make changes to a configuration file
include stdlib

file_line { 'Turn off passwd auth':
    ensure   => present,
    path     => '/etc/ssh/ssh_config',
    line     => '   PasswordAuthentication no'
    replace  => true,
}

file_line { 'Identiy file':
    ensure   => present,
    path     => '/etc/ssh/ssh_config',
    line     => '   IdentyFile ~/.ssh/school',
    replace  => true,
}
