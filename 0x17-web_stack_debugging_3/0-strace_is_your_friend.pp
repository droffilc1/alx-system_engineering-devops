# Fixes Apache 500 error
# https://stackoverflow.com/questions/174942/how-should-strace-be-used

exec { 'fix-config':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
