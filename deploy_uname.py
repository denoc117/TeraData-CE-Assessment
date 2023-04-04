from fabric.contrib.files import exists
from fabric.api import run


def deploy():
    _get_kernel_version()

def _get_kernel_version():
    if exists("/root"):
        run('uname -ar')
        run('rpm -qa')
        run('ps -fea')
