# Using Puppet to install flask from pip3
package {'flask':
    ensure   => '2.1.0',
    provider => 'pip',
}

package {'werkzeug':
    ensure => '2.1.1'
}
