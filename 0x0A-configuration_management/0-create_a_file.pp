#Using Puppet, create a school file in /tmp.

file { 'create_a_file':
ensure  => 'file',
path    => '/tmp/school',
mode    => '0744',
group   => 'www-data',
owner   => 'www-data',
content => 'I love Puppet'
}
