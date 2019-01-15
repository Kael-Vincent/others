import pexpect, re
import time, threading


def ssh_command(user, host, password, command):
        ssh_new_key = 'Are you sure you want to connect?'
        handle = pexpect.spawn("ssh -l % % %" % (user, host, command))
        i = handle.expect([pexpect.TIMEOUT, ssh_new_key, 'password:'])
        if i == 0:
            print('Error,ssh could not login.Here is ssh said:')
            print(handle.before, handle.after)
            return None
        if i == 1:
            handle.sendline('yes')
            handle.expect('password:')
            j = handle.expect([pexpect.TIMEOUT, 'password:'])
            if j == 0:
                print('Error,ssh could not login,here is ssh said:')
                print(handle.before, handle.after)
                return None
        handle.sendline(password)
        return handle


"""
memory listen
"""


def men_info():
        handle = ssh_command('root', '10.9.26.34', '123123', 'cat /proc/meninfo')
        handle.expect(pexpect.EOF)
        mem = handle.before
        mem_values = re.findall("(\d)\ kB", mem)
        MemTotal = mem_values[0]
        MemFree = mem_values[1]
        Buffers = mem_values[2]
        Cached = mem_values[3]
        SwapCached = mem_values[4]
        SwapTotal = mem_values[13]
        Swapfree = mem_values[14]
        print('**********************内存监控**************************')
        print('****************时间：', time.strftime("%Y-%m-%d %H:%m:%S", time.localtime()), '**********')
        print(u'总内存:', MemTotal)
        print(u'空闲内存:', MemFree)
        print(u'文件缓冲内存:', Buffers)
        print(u'缓存大小:', Cached)
        print(u'交换缓存大小:', SwapCached)
        if int(SwapTotal) == 0:
            print(u'交换缓存总共为：0')
        else:
            Rate_Swap = 100 - 100 * int(Swapfree) / float(SwapTotal)
            print(u'交换内存利用率为:', Rate_Swap)
        FreeMem = int(MemFree) + int(Buffers) + int(Cached)
        Used_Mem = int(MemTotal) - FreeMem
        Rate_Mem = 100 * Used_Mem / MemTotal
        print(u'内存利用率：', str("%.2f" % Rate_Mem), "%" )


def load_stat():
        handle = ssh_command('root', '10.9.26.34', '123123', 'cat /proc/loadavg')
        handle.expect(pexpect.EOF)
        loadavg = handle.before.strip().split()
        print('*********cpu监控*************')
        print('******************时间：', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), '************')
        print('系统5分钟前的负载：', loadavg[0])
        print('系统10分钟前的负载：', loadavg[1])
        print('系统15分钟前的负载：', loadavg[2])
        print('分子是正在进行的进程数，分母是总进程数:', loadavg[3])
        print('最近运行的进程Id：', loadavg[4])


if __name__ == '__main__':
    try:
        threads = []
        t1 = threading.Thread(target=men_info)
        threads.append(t1)
        t2 = threading.Thread(target=load_stat)
        threads.append(t2)
        for n in range(len(threads)):
            threads[n].start()
    except Exception as e:
        print(e)
