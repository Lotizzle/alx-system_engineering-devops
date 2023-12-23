# This manifest installs flask and other required packages.

# Installs Python 3.8.10
package { 'python3.8':
  ensure => present,
}

# Installs pip
package { 'python3-pip':
  ensure => present,
}

# Installs Flask 2.1.0
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip',
  require  => Package['python3-pip'],
}

# Installs Werkzeug 2.1.1
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip',
  require  => Package['python3-pip'],
}
