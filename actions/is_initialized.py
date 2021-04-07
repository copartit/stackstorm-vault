from lib import action


class VaultIsInitializedAction(action.VaultBaseAction):
    def run(self, profile=None):
        self.setup(profile)
        return self.vault.sys.is_initialized()
