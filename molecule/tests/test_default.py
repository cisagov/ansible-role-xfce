"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize("pkg", ["xfce4", "xfce4-goodies"])
def test_debian_packages(host, pkg):
    """Test that the appropriate packages were installed on Debian."""
    if host.system_info.distribution == "debian":
        assert host.package(pkg).is_installed


@pytest.mark.parametrize("pkg", ["kali-desktop-xfce", "xfce4-goodies"])
def test_kali_packages(host, pkg):
    """Test that the appropriate packages were installed on Kali."""
    if host.system_info.distribution == "kali":
        assert host.package(pkg).is_installed


@pytest.mark.parametrize("pkg", ["@xfce-desktop-environment"])
def test_redhat_packages(host, pkg):
    """Test that the appropriate packages were installed on RedHat."""
    if host.system_info.distribution == "redhat":
        assert host.package(pkg).is_installed
