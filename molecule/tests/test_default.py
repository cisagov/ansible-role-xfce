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
def test_debian_and_ubuntu_packages(host, pkg):
    """Test that the appropriate packages were installed on Debian and Ubuntu."""
    if (
        host.system_info.distribution == "debian"
        or host.system_info.distribution == "ubuntu"
    ):
        assert host.package(pkg).is_installed


@pytest.mark.parametrize("pkg", ["kali-desktop-xfce", "xfce4-goodies"])
def test_kali_packages(host, pkg):
    """Test that the appropriate packages were installed on Kali."""
    if host.system_info.distribution == "kali":
        assert host.package(pkg).is_installed


@pytest.mark.parametrize("pkg", ["@xfce-desktop-environment"])
def test_fedora_packages(host, pkg):
    """Test that the appropriate packages were installed on Fedora."""
    if host.system_info.distribution == "fedora":
        assert host.package(pkg).is_installed
