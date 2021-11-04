import os


class ConfigClass:
    api_modules = ["api"]
    env = os.environ.get('env', 'test')
    if env == "staging":
        # staging config
        VAULT_SERVICE = "https://vault.vault:8200/v1/vre/app/config"
        VAULT_CRT = "/run/secrets/kubernetes.io/serviceaccount/ca.crt"
        VAULT_TOKEN = "s.L35l8Ip6lgLikVJK4CaktfrE"
    elif env == "charite":
        # charite config
        VAULT_SERVICE = "https://vault.vault:8200/v1/vre/app/config"
        VAULT_CRT = "/run/secrets/kubernetes.io/serviceaccount/ca.crt"
        VAULT_TOKEN = "s.NPjdx6Rb2UfptYOjVQ7LPWIL"
    else:
        VAULT_SERVICE = "https://vault.vault:8200/v1/vre/app/config"
        VAULT_CRT = "/run/secrets/kubernetes.io/serviceaccount/ca.crt"
        VAULT_TOKEN = "s.p97lqlxBZ61C6sx5aHAFB4Ya"
