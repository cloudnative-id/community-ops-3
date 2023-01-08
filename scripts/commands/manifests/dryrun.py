import os
import click

from utils import *
from parser.configuration import ConfigurationParser
from deployer.shell import ShellDeployer
from deployer.manifest import ManifestDeployer

@click.command()
@click.option("--cluster-name",
              help="Cluster name to where the runtime should be deployed to",
              required=True)
def dryrun(cluster_name):
    os.chdir(DEFAULT_CLUSTERS_DIR + cluster_name)

    configuration = ConfigurationParser(DEFAULT_CLUSTER_CONFIG)
    configuration.validate()

    shell = ShellDeployer()

    print_header("Dryrun Manifest")
    manifest = ManifestDeployer(shell, DEFAULT_CLUSTER_MANIFEST_DIR, cluster_name)
    manifest.deploy(dryrun=True)