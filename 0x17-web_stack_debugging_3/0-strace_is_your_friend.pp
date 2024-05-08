 # Using strace, find out and fix Apache 500 error using Puppet.

exec {'fix_typo':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => ['/bin','/usr/bin']
}
