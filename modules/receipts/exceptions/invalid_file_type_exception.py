from ...shared.exceptions.bad_request_exception import BadRequestException


class InvalidFileTypeException(BadRequestException):
    def __init__(self, expected_file_type: str, actual_file_type: str):
        super().__init__(
            code="INVALID_FILE_TYPE",
            message=f"Invalid file type. Expected: {expected_file_type}. Actual: {actual_file_type}.",
            expected_file_type=expected_file_type,
            actual_file_type=actual_file_type,
        )
