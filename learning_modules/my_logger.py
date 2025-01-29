import logging
# logging.basicConfig(level=logging.DEBUG) # specify Debug will see all levels
# or specify some formats
# result will be 2025-01-26 16:35:16,236 [DEBUG]  test on level debug
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s [%(levelname)s]  %(message)s"
)
logger = logging.getLogger(__name__)
"""
logger.debug("test on level debug") # DEBUG:__main__:test on level debug
logger.info("test on level info") # INFO:__main__:test on level info
logger.fatal("test on level fatal") # CRITICAL:__main__:test on level fatal
logger.warning("test on level warning") # WARNING:__main__:test on level warning
logger.error("test on level error") # ERROR:__main__:test on level error
"""