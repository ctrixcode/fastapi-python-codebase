# src/core/logger.py

import logging
import sys
import structlog

# ==============================================================================
# Standard Library Logging Configuration
# ==============================================================================

# These processors are used to format log records from the standard library
# (like uvicorn) before they are rendered.
stdlib_processors = [
    structlog.stdlib.add_logger_name,
    structlog.stdlib.add_log_level,
    structlog.stdlib.PositionalArgumentsFormatter(),
    structlog.processors.TimeStamper(
        fmt="%Y-%m-%d %H:%M:%S", utc=False
    ),  # Original format
    structlog.processors.StackInfoRenderer(),
    structlog.processors.format_exc_info,
]

# The ProcessorFormatter is the bridge between standard logging and structlog.
formatter = structlog.stdlib.ProcessorFormatter(
    # These processors are run first for foreign (non-structlog) log records.
    foreign_pre_chain=stdlib_processors,
    # This is the final processor that renders the log record.
    # We use ConsoleRenderer for the same pretty output as before.
    processor=structlog.dev.ConsoleRenderer(),
)

# Create a handler that will write to stdout.
handler = logging.StreamHandler(sys.stdout)
# Attach our custom formatter to the handler.
handler.setFormatter(formatter)

# Get the root logger, remove any existing handlers, and add our new one.
root_logger = logging.getLogger()
root_logger.handlers.clear()
root_logger.addHandler(handler)
# Set the minimum log level for the root logger.
# All logs at this level or higher will be processed.
root_logger.setLevel(logging.INFO)


# ==============================================================================
# Structlog Configuration
# ==============================================================================

# These processors are for logs made directly with structlog.
structlog.configure(
    processors=[
        structlog.contextvars.merge_contextvars,
        structlog.stdlib.filter_by_level,
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.TimeStamper(
            fmt="%Y-%m-%d %H:%M:%S", utc=False
        ),  # Original format
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        # This processor passes the processed log record to the standard logging machinery.
        structlog.stdlib.render_to_log_kwargs,
    ],
    # Use a logger factory that creates standard library loggers.
    logger_factory=structlog.stdlib.LoggerFactory(),
    # Use a wrapper class that is compatible with standard logging.
    wrapper_class=structlog.stdlib.BoundLogger,
    cache_logger_on_first_use=True,
)

# ==============================================================================
# Logger Instance
# ==============================================================================

log = structlog.get_logger()


if __name__ == "__main__":
    log.info("This is an informational message from structlog.")

    # This log will be captured and formatted by our setup.
    uvicorn_logger = logging.getLogger("uvicorn.error")
    uvicorn_logger.info("This is a test message from a uvicorn logger.")

    try:
        1 / 0
    except ZeroDivisionError:
        log.exception("An exception occurred.")
