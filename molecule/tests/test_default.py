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
    distribution = host.system_info.distribution
    pkgs = None
    if (
        distribution in ["debian"] and host.system_info.codename in ["buster"]
    ) or distribution in ["ubuntu"]:
        pkgs = ["xfce4", "xfce4-goodies"]
    elif distribution in ["debian"]:
        pkgs = ["dbus-x11", "xfce4", "xfce4-goodies"]
    elif distribution == "kali":
        pkgs = ["dbus-x11", "kali-desktop-xfce", "xfce4-goodies"]
    elif distribution in ["fedora"]:
        # We can't check for the metapackage
        # @xfce-desktop-environment, so we check for a key xfce
        # package.
        pkgs = ["xfce4-panel"]
    else:
        # This is an unknown OS, so force the test to fail
        assert False, f"Unknown distribution {distribution}"

    for pkg in pkgs:
        assert host.package(pkg).is_installed
