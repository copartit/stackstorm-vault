from lib import action


class VaultCreateTokenAction(action.VaultBaseAction):
    def run(self,
            token_id=None,
            policies=None,
            meta=None,
            no_parent=False,
            display_name=None,
            num_uses=None,
            no_default_policy=False,
            ttl=None,
            wrap_ttl=None,
            profile=None):
        self.setup(profile)
        return self.vault.auth.token.create(id=token_id,
                                       policies=policies,
                                       meta=meta,
                                       no_parent=no_parent,
                                       display_name=display_name,
                                       num_uses=num_uses,
                                       no_default_policy=no_default_policy,
                                       ttl=ttl,
                                       wrap_ttl=wrap_ttl)
