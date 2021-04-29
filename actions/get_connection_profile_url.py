from lib import action


class VaultIsInitializedAction(action.VaultBaseAction):
    def run(self, profile=None):
        connection_profile = self._build_profile(profile)
        url = connection_profile["url"]
        return url
