import base64
import json
import logging
import boto3
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_secret(secret_name):
    """
    Return a cleartext secret JSON string
    :param secret_name:
    :return: Dict of cleartext secret values
    : rasise AWS SDK exception
    """

    secret_name = secret_name
    client= boto3.client('secretsmanager')

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId= secret_name
        )
    except ClientError as err:
        logging.error('Error Message:{}'.format(err.response['Error']['Message']))
        logging.error('Request ID:{}'.format(err.response['ResponseMetadata']['RequestId']))
        logging.error('Http code:{}'.format(err.response['ResponseMetadata']['HTTPStatusCode']))
        # don't swallow, throw it now 
        raise err
    else:
        # Decrypts secret using the associtated KMS CMK.
        # Depending on whether the secrect is a string or binary, one of these fields will be populated.
        if 'SecretString' in get_secret_value_response:
            secret = get_secret_value_response['SecretString']
        else:
            secret = base64.b64decode(get_secret_value_response['SecretBinary'])
        return json.loads(secret)
