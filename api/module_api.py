from flask_restx import Api

module_api = Api(version='1.0', title='Service Utility API',
                 description='Service Utility API for VRE', doc='/v1/api-doc')