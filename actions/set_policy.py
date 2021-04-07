from lib import action


class VaultPolicySetAction(action.VaultBaseAction):
    def run(self, name, rules, profile=None):
        self.setup(profile)
        return self.vault.sys.create_or_update_policy(name, rules)
