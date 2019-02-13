import subprocess
from platform import system
from version import CheckWrapper

WIN = 'Windows'
MIN_NPM_VERSION = 5
MIN_NODE_VERSION = 9


def less_than_min(version, min_ver):
    min_checker = CheckWrapper(min_ver)
    version_checker = CheckWrapper(version)

    return min_checker > version_checker


def do_WIN():
    try:
        # TODO: Find out about shell parameter
        #  https://stackoverflow.com/questions/3172470/actual-meaning-of-shell-true-in-subprocess
        node_version = subprocess.check_output(['node', '-v'], shell=True)
    except FileNotFoundError:
        print('ERROR: You should install Node.js')
        raise EnvironmentError

    try:
        npm_version = subprocess.check_output(['npm', '-v'], shell=True)
    except FileNotFoundError:
        print('ERROR: You should install npm')
        raise EnvironmentError

    npm_bad = less_than_min(npm_version, MIN_NPM_VERSION)
    node_bad = less_than_min(node_version, MIN_NODE_VERSION)

    if npm_bad:
        print('ERROR: Update your npm')
        raise EnvironmentError

    if node_bad:
        print('ERROR: Update your Node.js')
        raise EnvironmentError

    # install npm dependencies
    try:
        subprocess.check_output(['npm', 'install'], shell=True)
    except Exception as error:
        print(error)

    # TODO: Install python dependencies


if system() == WIN:
   do_WIN()
else:
    print('WARN: Your platform is not supported.')
