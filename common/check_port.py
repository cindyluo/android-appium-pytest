import os
import socket


def check_port(host, port):
    '''
    確認 port 是否有被佔用
    '''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        s.shutdown(2)
    except OSError:
        print(f'port {port} is available!')
        return True
    else:
        print(f'port {port} already be in use!')
        return False


def release_port(port):
    '''
    釋放 port
    '''
    cmd_find = f'netstat -aon | grep {port}'
    print(cmd_find)

    result = os.popen(cmd_find).read()
    print(result)

    if str(port) and 'LISTENING' in result:
        i = result.index('LISTENING')
        start = i + len('LISTENING') + 7
        end = result.index('\n')
        pid = result[start:end]
        cmd_kill = f'taskkill -f -pid {pid}'
        print(cmd_kill)
        os.popen(cmd_kill)
    else:
        print(f'port {port} is available !')


if __name__ == '__main__':
    port = 4723
    if not check_port('127.0.0.1', port):
        release_port(port)
