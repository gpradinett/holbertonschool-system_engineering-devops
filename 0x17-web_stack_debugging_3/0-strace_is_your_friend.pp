# script that fixes apache2 error

exec { 'error-apache2':
  command => 'sed -i s/phpp/php/ /var/www/html/wp-settings.php; sudo service apache2 restart',
  path    => [ '/bin/', '/sbin/' , '/usr/bin/', '/usr/sbin/' ]
}
