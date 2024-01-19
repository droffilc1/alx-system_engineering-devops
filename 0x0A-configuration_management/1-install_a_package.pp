# Using Puppet to install flask from pip3
package {'flask':
    ensure   => '2.1.0',
    provider => 'pip3',
}

package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}

package { 'Python':
  ensure   => '3.8.10',
  provider => 'pip3',
}
