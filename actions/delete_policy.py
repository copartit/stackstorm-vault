from lib import action


class VaultPolicyDeleteAction(action.VaultBaseAction):
    def run(self, name, profile=None):
        self.setup(profile)
        return self.vault.sys.delete_policy(name)
