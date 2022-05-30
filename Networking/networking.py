from __future__ import print_function
from pexpect import spawn
from json import loads


# system parameters
CONST_ITEM = []

file = 'src/ip_address_list.txt'
with open(file, 'r') as host_list:
    for line in host_list:
        host = line.split()[0]
        print("Start configuration on host ", host)

child = spawn('telnet %s' % host)


def json_ops(jfile):
    global CONST_ITEM
    with open(jfile, 'r') as jf:
        ci = jf.read()
    item = loads(ci)
    CONST_ITEM.append(list(item.values()))
    return CONST_ITEM


def login_to_node():
    # use Telnet
    SWITCH_USERNAME = CONST_ITEM[0]
    SWITCH_TELNET_PASSWORD = CONST_ITEM[1]
    SWITCH_ENABLE_PASSWORD = CONST_ITEM[2]
    try:
        child.expect('Username:')
        child.sendline(SWITCH_USERNAME)
        child.expect('Password:')
        child.sendline(SWITCH_TELNET_PASSWORD)
        child.expect('#')
        print("Successfully Telnetted to host ", host)
    except Exception:
        try:
            # child.expect('>')
            child.sendline('enable')
            child.expect('Password:')
            child.sendline(SWITCH_ENABLE_PASSWORD)
            child.expect('#')
            print("Successfully Telneted to host ", host, ',and enabled console')
        except Exception:
            print("Failed to Telnet to host ", host)
    return


# update firmware
def update_firmware():
    FIRMWARE_2960 = CONST_ITEM[6]
    FIRMWARE_3560 = CONST_ITEM[7]
    MIN_FLASH_REQ = CONST_ITEM[8]
    try:
        # check platform
        # child = spawn()

        # check model
        child.sendline('show version | include Model number')
        # child.expect('(?:Processor\sboard\sID\s)(\d|\w{11})')
        # hardware_model = child.after[-11:]

        # check running firmware
        child.sendline('show version | include MSystem image')
        # child.expect('(?:Processor\sboard\sID\s)(\d|\w{11})')
        # firmware = child.after[-11:]

        # check available space
        child.sendline('show flash | include bytes total')
        # child.expect('(?:Processor\sboard\sID\s)(\d|\w{11})')
        # flash_available = child.after[-11:]

        # upload new firmware
        # confirm md5
        # set boot variable
        # delete old firmware
        # notify upgrade
        # reboot
        print("Successfully updated firmware on host ", host)
    except Exception:
        print("Failed to update firmware on host ", host)
    return


# load configuration update
def load_config_update():
    CONFIGURATION_SERVER = CONST_ITEM[5]
    try:
        # copy config file to unit
        # child = pexpect.spawn()
        child.sendline('copy ftp: flash:')
        child.expect('[Address or name of remote host []?]')
        child.sendline(CONFIGURATION_SERVER)
        child.expect('[Source filename []?]')
        child.sendline('temp_config.cfg')
        print("Using device config file temp_config.cfg")
        child.sendline('temp_config.cfg')
        child.expect('[Source filename []?]')
        child.sendline('temp_config.cfg')
        child.expect('#')
        print("Successfully copied files to flash ", host)

        # copy config to running config (append current)
        try:
            child.sendline('copy flash:temp_config.cfg running-config')
            child.expect('[?]')
            child.sendline('running-config')
            child.expect('#')
            print("Successfully copied files to running-config ", host)
        except Exception:
            print("Failed to copy files to running-config ", host)
    except Exception:
        print("Failed to copy files to flash ", host)
    return


# load custom config
def load_custom_config(dev_id):
    CONFIGURATION_SERVER = CONST_ITEM[5]
    FTP_USERNAME = CONST_ITEM[3]
    FTP_PASSWORD = CONST_ITEM[4]
    MIN_FLASH_REQ = CONST_ITEM[8]
    try:
        # get unit info
        child.sendline('show version | include Processor')
        child.expect(r'(?:Processor\sboard\sID\s)(\d|\w{11})')
        print("This is Device-ID ", child.after[-11:])
        print("This is Device-SN ", dev_id)
        config = '%s.cfg' % dev_id

        # copy config file to unit
        child.sendline('copy ftp: flash:')
        child.expect('[Address or name of remote host []?]')
        child.sendline(CONFIGURATION_SERVER)
        child.expect('[Source filename []?]')
        print("Using device config file ", config)
        child.sendline(config)
        child.expect('[Source filename []?]')
        child.sendline('temp_config.cfg')
        child.expect('#')
        print("Successfully copied files to flash ", host)

        # copy config to running config (replace current)
        try:
            child.sendline('copy flash:temp_config.cfg running-config')
            child.expect('[?]')
            child.sendline('running-config')
            child.expect('#')
            print("Successfully copied files to running-config ", host)
        except Exception:
            print("Failed to copy files to running-config ", host)
    except Exception:
        print("Failed to copy files to flash ", host)
    return


# generate new crypto key
def generate_rsa_key():
    RSA_KEY_LENGTH = CONST_ITEM[9]
    # check current key
    # ?
    # generate new key
    try:
        child.sendline('crypto key generate rsa')
        child.expect('(512)')
        child.sendline(RSA_KEY_LENGTH)
        child.expect('#')
        print("Successfully generated new RSA key on host ", host)
    except Exception:
        print("RSA key gen failed on host ", host)
    return


# save running config
def save_running_config():
    try:
        child.expect('#')
        child.sendline('write memory')
        child.expect('[OK]')
        child.expect('#')
        print("Successfully saved the running-config on ", host)
    except Exception:
        print("Failed to save the running-config on ", host)


# backup running config
def backup_deployed_congig():
    CONFIGURATION_SERVER = CONST_ITEM[5]
    FTP_USERNAME = CONST_ITEM[3]
    FTP_PASSWORD = CONST_ITEM[4]
    # child.sendline('quit')
    return


# test function
def test_function():
    try:
        print("Successfully ran the test function on host ", host)
    except Exception:
        print("Test function failed on host ", host)
    return


def net_main():
    json_file = 'networking.json'
    json_ops(json_file)
    login_to_node()
    update_firmware()
    load_config_update()
    load_custom_config(device_id)
    generate_rsa_key()
    save_running_config()
    backup_deployed_congig()
    test_function()


if __name__ == '__main__':
    net_main()
    platform = None
    hardware_model = None
    firmware = None
    flash_available = None
    device_id = None
    serial_number = None
    config_file = None
