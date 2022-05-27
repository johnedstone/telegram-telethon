import logging
import secrets
import string

logger = logging.getLogger(__name__)

def get_random_id():
    random_id = ''.join(secrets.choice( 
           string.ascii_uppercase + string.digits) for i in range(16))
    logger.info(random_id)
    # Next: check that this is unique

    return random_id
