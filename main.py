import asyncio
import sys

import uvicorn
from pydantic import ValidationError

from src.app import app
from src.core.logger import log
from src.core.settings import get_settings
from src.features.examples.model import Example  # noqa



async def main():
    """
    Run the application.
    """
    # Load Env and fail if env are missing
    try:
        settings = get_settings()
    except ValidationError as e:
        log.error("Missing environment variables:")
        for error in e.errors():
            log.error(f"  - {error['loc'][0]}: {error['msg']}")
        sys.exit(1)

    # Log the startup information
    log.info(f"Starting server in '{settings.APP_ENV}' mode.")

    # Create Uvicorn server instance
    config = uvicorn.Config(
        app,
        host=settings.HOST,
        port=settings.PORT,
        log_config=None,
    )
    server = uvicorn.Server(config)

    # Uvicorn's default signal handlers will catch Ctrl+C and trigger a
    # graceful shutdown. The await will complete after the server is stopped.
    await server.serve()
    log.info("Server shutdown process finished.")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        log.info("Application interrupted by user. Exiting.")