from pulpcore.plugin import PulpPluginAppConfig


class PulpSmartProxyPluginAppConfig(PulpPluginAppConfig):
    """Entry point for the smrt plugin."""

    name = "pulp_smart_proxy.app"
    label = "smrt"
    version = "0.0.0.dev"
    python_package_name = "pulp_smart_proxy"
    domain_compatible = True
