import os

import testinfra.utils.ansible_runner

import pytest


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


""" ansible-role-platform (ctorgalson.platform) tests. """


@pytest.mark.parametrize('package,version', [
  ('platform', 'Platform.sh CLI 3'),
])
def test_platform_cli(host, package, version):
    c = '{} --version'.format(package)
    r = host.run(c)

    assert version in r.stdout
