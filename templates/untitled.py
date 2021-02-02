#!/usr/bin/python

from subprocess import *

#defining constatnts

ssh_cmd = " ssh -A -o batchmode=yes -o stricthostkeychecking=no "
puppet_cmd = " /usr/bin/sudo -u root /usr/local/nagios/libexec/check_puppet_cron "
pgrep_cmd = " sudo pgrep puppet -fl | qwk '{ print $1 }' | xargs kill -9 "
puppet_run_cmd = " sudo puppet agent -tvd --evaltrace "
hostname = " mr26p42im-mail42511 "

def command_exec(cmd):
        cmd_out = Popen([ cmd ], shell=True ,stdout=PIPE ,stderr=STDOUT)
        cmd_result,return_code = cmd_out.communicate()[0],cmd_out.returncode
        cmd_result = cmd_result.strip().splitlines()
       # Check the retrun code
        if return_code == 0:
                return {"status": True , "data": cmd_result }
        else:
                return {"status": False , "data": cmd_result}


def puppet_cron():
	cmd = ssh_cmd + hostname + puppet_cmd
	print(cmd)
 	out = command_exec(cmd)
	print(out)

	cmd = ssh_cmd + hostname + pgrep_cmd
        print(cmd)
        out = command_exec(cmd)
        print(out)

	cmd = ssh_cmd + hostname + puppet_run_cmd
        print(cmd)
        out = command_exec(cmd)
        print(out)

	cmd = ssh_cmd + hostname + puppet_cmd
        print(cmd)
        out = command_exec(cmd)
        print(out)

puppet_cron()