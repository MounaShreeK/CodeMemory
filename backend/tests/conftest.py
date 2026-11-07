import sys
from pathlib import Path

BACKEND_ROOT = Path(__file__).resolve().parents[1]
if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))

# The Hindsight SDK is an external dependency; API health/schema tests do not call it.
# Stub its import so those isolated tests can run without network credentials or SDK install.
import sys
import types

if "hindsight_client" not in sys.modules:
    hindsight_stub = types.ModuleType("hindsight_client")

    class _HindsightNotConfigured:
        def __init__(self, *args, **kwargs):
            raise RuntimeError("Hindsight SDK is not available in this test environment")

    hindsight_stub.Hindsight = _HindsightNotConfigured
    sys.modules["hindsight_client"] = hindsight_stub
