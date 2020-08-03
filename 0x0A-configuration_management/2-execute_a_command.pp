# create kill exec

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}