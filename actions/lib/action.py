import hvac
from st2common.runners.base_action import Action


class VaultBaseAction(Action):

    vault = None

    def __init__(self, config, action_service):
        super(VaultBaseAction, self).__init__(config, action_service)

    def setup(self, connection_profile_name=None):
        self.vault = self._get_client(connection_profile_name)

    def _get_client(self, profile_name=None):
        connection_profile = self._build_profile(profile_name)

        url = connection_profile["url"]
        verify = self._get_verify(connection_profile)

        auth_method = connection_profile.get("auth_method", "token")
        token = connection_profile.get("token")

        # token is passed during client init to allow client to also
        # get the token from VAULT_TOKEN env var or ~/.vault-token
        client = hvac.Client(url=url, token=token, verify=verify)

        # NB: for auth_methods, we used to be able to login with
        # client.auth_*, but most of those have been deprecated
        # in favor of: client.auth.<method>.login
        # So, use client.auth.<method> where implemented

        # token is handled during client init
        # other auth methods will override it as needed
        if auth_method == "token":
            if token is None:
                raise KeyError(
                    "token is required when auth_method is 'token'. Please adjust pack config. (profile: {})".format(
                        profile_name
                    )
                )
        elif auth_method == "approle":
            client.auth.approle.login(
                role_id=connection_profile["role_id"],
                secret_id=connection_profile["secret_id"],
            )
        else:
            raise NotImplementedError(
                "The {} auth method has a typo or has not been implemented (yet).".format(
                    auth_method
                )
            )

        return client

    def _build_profile(self, profile_name):
        config = self.config

        default_profile = {}

        # TODO: Drop this top-level stuff in favor of taking the first entry
        default_profile_name = config.pop("default-profile", "@@@top-level@@@")
        if default_profile_name == "@@@top-level@@@":
            for key in ["url", "cert", "verify", "auth_method", "token", "role_id", "secret_id"]:
                default_profile[key] = config.get(key)

        profiles = config.pop("profiles", {})
        profile = profiles.get(profile_name, profiles.get(default_profile_name, default_profile))
        if profile.get("url", None) is None:
            if len(profiles) == 1:
                profile = profiles.popitem()
            else:
                raise KeyError("Unable to find vault connection profile (default: {})".format(default_profile_name))
        return profile

    @staticmethod
    def _get_verify(connection_profile):
        verify = connection_profile["verify"]
        cert = connection_profile["cert"]
        if verify and cert:
            return cert
        return verify
