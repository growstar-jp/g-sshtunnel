import logging

from sshtunnel import SSHTunnelForwarder

from . import config

logger = logging.getLogger(__name__)


def through_ssh(func: callable):
    def _through_ssh(*args, **kwargs):
        with SSHTunnelForwarder(
            ssh_address_or_host=(config.TUNNEL_SSH_HOST, config.TUNNEL_SSH_PORT),
            ssh_username=config.TUNNEL_SSH_USER,
            ssh_pkey=config.TUNNEL_SSH_KEY,
            remote_bind_address=(
                config.TUNNEL_REMOTE_HOST,
                config.TUNNEL_REMOTE_PORT,
            ),
            local_bind_address=(config.TUNNEL_LOCAL_HOST, config.TUNNEL_LOCAL_PORT),
        ) as tunnel:
            logger.info(f"{func.__name__} args:{args} kargs:{kwargs}")
            result = func(*args, **kwargs)
            return result
    logger.warning(f'SSH TUNNEL:{config.TUNNEL_FLAG}')
    if config.TUNNEL_FLAG:
        return _through_ssh
    else:
        return func
