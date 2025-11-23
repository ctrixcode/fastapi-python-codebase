import uvicorn
from src.app import app
from src.core.logger import log
from src.core.settings import get_settings

if __name__ == "__main__":
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

    # Start the Uvicorn server
    uvicorn.run(app, host=settings.HOST, port=settings.PORT)