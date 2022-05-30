from psutil import process_iter, NoSuchProcess, AccessDenied, ZombieProcess
from os import system


def find_process_id_by_name(process_name) -> list:
    """
    Get a list of all the PIDs of a all the running process whose name contains
    the given string processName
    """
    list_of_process_objects = []
    # Iterate over the all the running process
    for proc in process_iter():
        try:
            process_info = proc.as_dict(attrs=['pid', 'name'])
           
            # Check if process name contains the given name string.
            if process_name.lower() in str(process_info['name']).lower() :
                list_of_process_objects.append(process_info)
               
        except (NoSuchProcess, AccessDenied , ZombieProcess) :
            pass
    return list_of_process_objects


def process_check() -> None:
    start = ['Outlook.exe', 'notepad++.exe', 'chrome.exe', 'explorer.exe', 'lync.exe']

    for process in start:
        list_of_process_ids = find_process_id_by_name(process)
        if len(list_of_process_ids) > 0:
            print('Process Exists | PID and other details are')
            for element in list_of_process_ids:
                process_id = element['pid']
                process_name = element['name']
                print(process_id, process_name)
        else:
            print('No Running Process found with given text')


if __name__ == '__main__':
    process_check()
    system('pause')
