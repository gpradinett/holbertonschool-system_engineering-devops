# script that fixes holberton error

exec { 'error-holberton':
  command => 'sed -i s/5/50000/ /etc/security/limits.conf',
  path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ]
}

exec { 'error-holberton-part2':
  command => 'sed -i s/4/40000/ /etc/security/limits.conf',
  path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ]
}
