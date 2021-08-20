import os


class ConfigClass:
    api_modules = ["api"]
    env = os.environ.get('env', 'test')
    if env == "staging":
        # staging config
        VAULT_SERVICE = "https://vault.vault:8200/v1/vre/app/config"
        VAULT_CRT = "/run/secrets/kubernetes.io/serviceaccount/ca.crt"
        VAULT_TOKEN = "s.zHgLC3aJKHLcFA12PG96hQ8x"
    elif env == "charite":
        # charite config
        VAULT_SERVICE = "https://vault.vault:8200/v1/vre/app/config"
        VAULT_CRT = "/run/secrets/kubernetes.io/serviceaccount/ca.crt"
        VAULT_TOKEN = "s.k58KFHp09AUnSSUlaNZI76IL"
    else:
        VAULT_SERVICE = "https://vault.vault:8200/v1/vre/app/config"
        VAULT_CRT = "/run/secrets/kubernetes.io/serviceaccount/ca.crt"
        VAULT_TOKEN = "s.uxoIjrydEZsgTF0zBWdsiVJ9"
