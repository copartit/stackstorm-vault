from lib import action


class VaultPolicyListAction(action.VaultBaseAction):
    def run(self, profile=None):
        self.setup(profile)
        return self.vault.list_policies()
