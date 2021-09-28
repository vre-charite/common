class ConfigCenterPolicy:

    @staticmethod
    def get_granted(srv_namespace):
        return {
            'service_download': ConfigCenterPolicy.service_download()
        }.get(
            srv_namespace,
            []
        )

    @staticmethod
    def service_download():
        return [
            "DOWNLOAD",
            "KEYCLOAK",
            "MINIO",
            "REDIS",
            "NEO4J_SERVICE",
            "PROVENANCE_SERVICE",
            "QUEUE_SERVICE",
            "UTILITY_SERVICE",
            "DATA_OPS_GR",
            "DATA_OPS_UTIL",
            "DATASET_SERVICE",
        ]
