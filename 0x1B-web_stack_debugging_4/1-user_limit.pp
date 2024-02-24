# Enables the user Holberton to login and open files without error

# Increases hard file limit for Holberton user
exec { 'increase-hard-file-limit':
  command => 'sed -i "/^holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Increases soft file limit for Holberton user
exec { 'increase-soft-file-limit':
  command => 'sed -i "/^holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
