import logging
import os

from crypy.client import Client

logging.basicConfig(level=logging.INFO)

def get_client_tokens():
    dcos_env = 'ops'
    if 'DCOS_ENV' in os.environ:
        dcos_env = os.environ['DCOS_ENV']
    cc = Client('dcos', crypter_env=dcos_env)
    consul_acl_token = cc.read_credential('CONSUL_CLIENT_ACL_TOKEN')
    consul_encrypt_key = cc.read_credential('CONSUL_CLIENT_ENCRYPT_KEY')
    return "%s,%s" %(consul_acl_token, consul_encrypt_key)

if __name__ == '__main__':
    print get_client_tokens()
