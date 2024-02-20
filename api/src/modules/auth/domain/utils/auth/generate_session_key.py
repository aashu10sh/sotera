from snowflake import SnowflakeGenerator  # type:ignore


gen = SnowflakeGenerator(42)


def generate_session_key():
    return next(gen)
