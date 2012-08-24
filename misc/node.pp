yumrepo { 'sewell':
  descr    => 'sewell',
  baseurl  => 'http://dl.sewell.org/rpm/sewell/el/6/x86_64/',
  gpgcheck => 0,
  enabled  => 1,
}

package { ['brpm', 'git', 'python-argparse', 'PyYAML', 'vim-enhanced']:
  ensure  => present,
  require => Yumrepo['sewell'],
}

exec { 'group_mock_vagrant':
  command => '/usr/sbin/usermod -a -G mock vagrant',
  unless  => '/usr/bin/id -G --name vagrant | grep mock &>/dev/null',
  require => Package['brpm'],
}

file { '/home/vagrant/.bashrc':
  ensure  => present,
  owner   => 'vagrant',
  group   => 'vagrant',
  mode    => '0644',
  content => '
    test -f /etc/bashrc && . /etc/bashrc
    test -f /home/vagrant/.bash_local && . /home/vagrant/.bash_local

    export PATH="/vagrant/python-rock/scripts:$PATH"
    export PATH="/vagrant/tools/src:$PATH"
    export PYTHONPATH="/vagrant/python-rock:$PYTHONPATH"
  ',
}

class { 'rock': release => 0 }

rock::runtime { ['node04', 'node06', 'node08', 'perl516', 'php54', 'python27', 'ruby18', 'ruby19']:
  autoupgrade => true,
}
