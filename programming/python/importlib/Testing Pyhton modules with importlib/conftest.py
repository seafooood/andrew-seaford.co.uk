# conftest.py (shared across all tests in this folder)
import pathlib
import pytest

@pytest.fixture(scope="module")
def mymodule():
    """Load myfile.py into a namespace, stripping invalid top-level returns."""
    module_path = pathlib.Path(__file__).parent / "myfile.py"
    source = module_path.read_text()

    # Strip out any invalid top-level `return ...` lines
    cleaned_source = "\n".join(
        line for line in source.splitlines() if not line.startswith("return ")
    )

    ns = {}
    exec(cleaned_source, ns)
    return ns
