from fabric.api import sudo, settings, run

def add_dns(hostname, ip, record_type='A'):
    with settings(user='vagrant', password='vagrant'):
        sudo('echo "{}.kvm.lan.      IN      {}      {}" >> /srv/salt/files/bind/kvm.lan.zone'.format(hostname, record_type, ip))
        sudo('salt "dns*" state.highstate')

def remove_dns(hostname):
    with settings(user='vagrant', password='vagrant'):
        sudo('sed "/{}*/d" /srv/salt/files/bind/kvm.lan.zone -i'.format(hostname))
        sudo('salt "dns*" state.highstate')

def show_dns():
    with settings(user='vagrant', password='vagrant'):
        sudo('cat /srv/salt/files/bind/kvm.lan.zone')

def salt_key_accept():
    with settings(user='vagrant', password='vagrant'):
        sudo('salt-key -y -A')

def salt_highstate(hostname):
    with settings(user='vagrant', password='vagrant', timeout=300):
        sudo('salt "{}*" state.highstate'.format(hostname))
