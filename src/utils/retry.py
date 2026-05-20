from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential
)


def retry_on_failure():
    """
    Retry decorator for transient failures.
    """

    return retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=2),
        reraise=True
    )