from pipeline_logger import log_pipeline_stage
from datetime import datetime

# Minimal required values
pipeline_id = "glue_test_logger_" + datetime.utcnow().strftime("%Y%m%d_%H%M%S")

log_pipeline_stage(
    pipeline_id=pipeline_id,
    stage="test_import",
    pipeline_name="test_glue_logger",
    pipeline_type="test",
    executor="glue",
    status="SUCCEEDED",
    timestamp=datetime.utcnow().isoformat(),
    details={"message": "✅ logger works inside Glue!"}
)

print("✅ pipeline_logger test completed")
