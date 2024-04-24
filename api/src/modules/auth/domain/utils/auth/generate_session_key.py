from snowflake import SnowflakeGenerator  # type:ignore


gen = SnowflakeGenerator(42)


def generate_session_key() -> int | None:
    return next(gen)
