import os
from fabric.api import run, env, cd

env.use_ssh_config = True
env.hosts = ['yj']


def host_type():
    run('uname -s')


APP_ROOT = "/data/apps/dash"


def root(x): return os.path.join(APP_ROOT, x)


VENV_ROOT = root(".venv")
PYTHON = root(".venv/bin/python")
PIP = root(".venv/bin/pip")
MANAGE = root("manage.py")


def migrate():
    run('{0} {1} migrate'.format(PYTHON, MANAGE))


def install_depends():
    run('{0} install -r ./requirements.txt'.format(PIP))


def publish():
    with cd(APP_ROOT):
        install_depends()
        migrate()


def reload():
    """reload services"""
