class ManifestDeployer():
    def __init__(self, shell, manifest_dir, cluster):
        self.shell = shell
        self.manifest_dir = manifest_dir
        self.cluster = cluster

    def deploy(self, dryrun=False):
        command = ["kubectl", "apply", "-f", self.manifest_dir, "-R", "--context", self.cluster]

        if dryrun:
            command.extend(["--dry-run=server"])

        output = self.shell.execute(command)
        print(output)

    def diff(self):
        command = ["kubectl", "diff", "-f", self.manifest_dir, "--recursive=true", "--context", self.cluster]
        output = self.shell.execute(command)
        print(output)
