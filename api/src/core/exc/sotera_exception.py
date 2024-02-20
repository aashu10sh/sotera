from typing import Any, Dict, List

from fastapi import HTTPException

from src.core.exc.error_codes import ErrorCode


class SoteraException(HTTPException):
    def __init__(
        self,
        status_code: int,
        code: ErrorCode,
        msg: str,
        fields: List[Any] = [],
        headers: Dict[str, str] | None = None,
    ) -> None:
        super().__init__(
            status_code=status_code,
            detail={"code": code, "msg": msg, "fields": fields},
            headers=headers,
        )
