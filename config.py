
import os

class ConfigClass:
    api_modules = ["api"]
    env = os.environ.get('env', 'test')
    if env == "staging":
        # staging config
        VAULT_SERVICE = "https://vault.vault:8200/v1/vre/app/config"
        VAULT_CRT="/run/secrets/kubernetes.io/serviceaccount/ca.crt"
        VAULT_TOKEN="s.RISGjSyH1pylevR2Mq2gL2BC"
    elif env == "charite":
        # charite config
        VAULT_SERVICE = "https://vault.vault:8200/v1/vre/app/config"
        VAULT_CRT="/run/secrets/kubernetes.io/serviceaccount/ca.crt"
        VAULT_TOKEN="s.Juas29svaEwuOwThii3h5t5F"
    else:
        VAULT_SERVICE = "https://vault.vault:8200/v1/vre/app/config"
        VAULT_CRT="/run/secrets/kubernetes.io/serviceaccount/ca.crt"
        VAULT_TOKEN="s.VCX1vOVI94q1YKoYi4OZXpxz"