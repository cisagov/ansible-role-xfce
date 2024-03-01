"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_packages(host):
    """Test that the appropriate packages were installed."""
    pkgs = None
    if (
        host.system_info.distribution == "debian"
        and host.system_info.codename != "bullseye"
    ) or host.system_info.distribution == "ubuntu":
        pkgs = ["xfce4", "xfce4-goodies"]
    elif (
        host.system_info.distribution == "debian"
        and host.system_info.codename == "bullseye"
    ):
        pkgs = ["dbus-x11", "xfce4", "xfce4-goodies"]
    elif host.system_info.distribution == "kali":
        pkgs = ["dbus-x11", "kali-desktop-xfce", "xfce4-goodies"]
    elif host.system_info.distribution == "fedora":
        # We can't check for the metapackage
        # @xfce-desktop-environment, so we check for a key xfce
        # package.
        pkgs = ["xfce4-panel"]
    else:
        # This is an unknown OS, so force the test to fail
        assert False

    for pkg in pkgs:
        assert host.package(pkg).is_installed
