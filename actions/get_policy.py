from lib import action


class VaultGetPolicyAction(action.VaultBaseAction):
    def run(self, name):
        return self.vault.get_policy(name)
