import time
import os
import sys
import subprocess
import shlex

PID_FILE='/home/vagrant/demo.pid'
PATH=os.path.dirname(os.path.abspath(__file__))
PID=os.getpid()


def get_ptree():
    """
    """
    res = subprocess.check_output(shlex.split("pstree -p {}".format(PID)))
    return len(res.decode().strip().split("\n"))

def create_pid():
    if os.environ.get("DOCKER"):
        return
    with  open(PID_FILE, "w") as f:
        f.write(str(PID))



def clean_pid():
    try:
        os.remove(PID_FILE)
    except Exception as e:
        print(str(e))

def main():
    create_pid()
    while True:
        # execute
        c = get_ptree()
        # print("C: ", c)
        if c < 4:
            run_cmd("{}/demo_runner.py cmd1 -s 30 -a 'some demo text' >1&2 >/dev/null ".format(PATH))
        time.sleep(10)


def run_cmd(cmd):
    """
    """
    subprocess.Popen(shlex.split("nohup {} {} ".format(
        sys.executable,
        cmd)), preexec_fn=os.setpgrp)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(str(e))
    finally:
        clean_pid()

