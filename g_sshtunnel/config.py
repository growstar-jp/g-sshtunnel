import os

from dotenv import load_dotenv

load_dotenv()
    
# SSH TUNNEL
TUNNEL_FLAG = bool(os.getenv("TUNNEL_FLAG", False) == "True")
TUNNEL_SSH_HOST = os.getenv("TUNNEL_SSH_HOST", "")
TUNNEL_SSH_PORT = int(os.getenv("TUNNEL_SSH_PORT", 22))
TUNNEL_SSH_USER = os.getenv("TUNNEL_SSH_USER", "")
TUNNEL_SSH_KEY = os.getenv("TUNNEL_SSH_KEY")
TUNNEL_REMOTE_HOST = os.getenv("TUNNEL_REMOTE_HOST")
TUNNEL_REMOTE_PORT = int(os.getenv("TUNNEL_REMOTE_PORT", 22))
TUNNEL_LOCAL_HOST = os.getenv("TUNNEL_LOCAL_HOST", "localhost")
TUNNEL_LOCAL_PORT = int(os.getenv("TUNNEL_LOCAL_PORT", 59000))
