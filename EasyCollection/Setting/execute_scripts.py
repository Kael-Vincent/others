import paramiko
from time import sleep


def execute_scripts():
    ssh= paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    try:
        ssh.connect(hostname='10.40.11.140', port=22, username='root', password='PkKgX8bA')
    except Exception as e:
        print(e)
    cm1 = 'cd /opt/server/OneCollection/onecollection-job/scripts/ &&'
    cm2 = 'sh debtor-gps-info/start-update-debtor-gps-info.sh test &&'
    cm3 = 'sh auto-entrust-task/start-auto-entrust-task.sh test &&'
    cm4 = ' sh auto-init-electric-task-by-rule/start-auto-init-electric-task-by-rule.sh test &&'
    cm5 = ' sh auto-entrust-electric/start-auto-entrust-electric.sh test &&'
    cm6 = 'sh auto-assign-task-by-rule/start-assign-task-by-rule.sh test'
    # cm4='sh 24hour_auto_finish_task/start-24hour-auto-finish-task.sh test'
    # cm4= 'sh withdraw-task/start-withdraw-task.sh test'
    # for i in range(210):
    stdin,stdout,stderr = ssh.exec_command(cm1+cm2+cm3+cm4+cm5+cm6)
    print(stdout.read().decode())
    ssh.close()
execute_scripts()