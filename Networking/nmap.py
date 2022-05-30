from os import system


def nmap(ip):
    var = f'nmap -A -p- {ip} -v'
    print('Running scan against', var)


def recon(ip):
    system(f'nmap -A -p- -Pn {ip} -v')
    system(f'dirb {ip}')


if __name__ == '__main__':
    recon(input('What ip would you like to scan? '))


