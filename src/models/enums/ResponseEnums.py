from enum import Enum

class ResponseSignal(Enum):
    """
    Enum to represent the signal of a response.
    """
    FILE_VALIDATED_SUCCESS = "File Validated Successfully"
    FILE_TYPE_NOT_SUPPORTED = "File Type Not Supported"
    FILE_SIZE_EXCEEDED = "File Size Exceeded"
    FILE_UPLOAD_SUCCESS = "File Upload Success"
    FILE_UPLOAD_FAILED = "File Upload Failed"
    FILE_PROCESSING_FAILED = "File Processing Failed"
    FILE_PROCESSING_SUCCESS = "File Processing Success"
