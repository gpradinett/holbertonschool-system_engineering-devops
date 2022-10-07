# Nginx sevidor with Error
exec {'Error':
        command  => 'sed -i "s/15/1500/g" /etc/default/nginx; sudo service nginx restart',
        provider => shell,
}
