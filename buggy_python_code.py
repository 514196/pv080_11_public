# contains bunch of buggy examples
# taken from https://hackernoon.com/10-common-security-gotchas-
#                   in-python-and-how-to-avoid-them-e19fbe265e03

import base64
import subprocess
import flask
import cPickle


# Input injection
def transcode_file(request, filename):
    """
    x
    :param request: x
    :param filename: x
    :return: x
    """
    command = 'ffmpeg -i "{source}" output_file.mpg'\
        .format(source=filename)
    subprocess.call(command, shell=True)  # a bad idea!


# Assert statements
def authorize(request, user):
    """
    x
    :param request: x
    :param user: x
    :return: x
    """
    assert user.is_admin, 'user does not have access'
    # secure code...


# Pickles
class RunBinSh:
    """
    RunBinSh Class
    """
    def __reduce__(self):
        """
        x
        :return: x
        """
        return subprocess.Popen, (('/bin/sh',),)


def import_urlib_version(version):
    """
    x
    :param version: x
    :return: x
    """
    exec("import urllib%s as urllib" % version)


def index():
    """
    x
    :return: x
    """
    module = flask.request.args.get("module")
    import_urlib_version(module)


print(base64.b64encode(pickle.dumps(RunBinSh())))
