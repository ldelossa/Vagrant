from fabric.api import sudo, settings, run

def update_dns(hostname, ip):
    with settings(user='vagrant', password='vagrant'):
        sudo('echo "{}.kvm.lan.      IN      A      {}" >> /srv/salt/files/bind/kvm.lan.zone'.format(hostname, ip))
        sudo('salt "dns*" state.highstate')

def salt_key_accept():
    with settings(user='vagrant', password='vagrant'):
        sudo('salt-key -y -A')

def salt_highstate(hostname):
    with settings(user='vagrant', password='vagrant', timeout=300):
        sudo('salt "{}*" state.highstate'.format(hostname))
