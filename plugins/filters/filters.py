from urlparse import urlsplit


def consul_server_ips(hostvars, groups, consul_group='consul'):
    consul_ips = set()
    for host in groups[consul_group]:
        interface = hostvars[host]['consul']['bind_interface']
        ip = hostvars[host]['ansible_' + interface]['ipv4']['address']
        consul_ips.add(ip)
    return sorted(list(consul_ips))


def urlparse(url, index):
    return urlsplit(url)[index]


def domain(url):
    return urlsplit(url)[0] + '://' + urlsplit(url)[1]


def hostname(url):
    return urlsplit(url).hostname


def list_contains_url(_list, url):
    intersection = [r for r in _list if r in url]
    return intersection


class FilterModule(object):
    ''' ursula infra filters '''

    def filters(self):
        return {
            'consul_server_ips': consul_server_ips,
            'urlparse': urlparse,
            'domain': domain,
            'hostname': hostname,
            'list_contains_url': list_contains_url
        }
