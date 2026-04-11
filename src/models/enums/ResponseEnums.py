from enum import Enum
class ResponseSignals(Enum):
    FILE_VALIDATED_SUCCESS = "File validated successfully"
    FILE_TYPE_NOT_SUPPORTED = "Unsupported file type"
    FILE_SIZE_EXCEEDS_LIMIT = "File size exceeds the allowed limit"
    FILE_UPLOADED_SUCCESS = "File uploaded successfully"
    FILE_UPLOAD_FAILED = "File upload failed"
