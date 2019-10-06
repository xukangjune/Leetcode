def func(ip):
    ipv4 = ip.split('.')
    ipv6 = ip.split(':')

    if len(ipv4) == 4 and len(ipv6) == 1:
        for x in ipv4:
            if not x:
                return "Neither"
            if not x.isalnum():
                return "Neither"
            if (len(x)) > 1 and x.startswith('0'):
                return "Neither"
            if int(x)<0 or int(x) > 255:
                return "Neither"
        return "IPv4"

    elif len(ipv4) == 1 and len(ipv6) == 8:
        for x in ipv6:
            if len(x) > 4:
                return "Neither"
            try:
                y = int(x, base=16)
                if y==0 and len(x) > 1:
                    return "Neither"
            except Exception:
                return "Neither"
        return "IPv6"
    else:
        return "Neither"

ip = input().strip()
print(func(ip))