from lib import action


class VaultGetPolicyAction(action.VaultBaseAction):
    def run(self, name, profile=None):
        self.setup(profile)
        return self.vault.get_policy(name)
