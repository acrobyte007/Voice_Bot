import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from dotenv import load_dotenv
load_dotenv(override=True)
import os
GRPQ_API_KEY = os.getenv("API_KEY")