import subprocess
import sys
import os
import tempfile

SCRIPT = os.path.abspath("main.py")


def create_temp_csv(content: str) -> str:
    fd, path = tempfile.mkstemp(suffix=".csv", text=True)
    with os.fdopen(fd, 'w') as f:
        f.write(content)
    return path


def test_main_interface_filter_and_aggregate():
    csv_content = "brand,rating\nxiaomi,4.5\napple,4.9\nxiaomi,4.3"
    csv_file = create_temp_csv(csv_content)

    result = subprocess.run(
        [sys.executable, SCRIPT, "--file", csv_file, "--where", "brand==xiaomi", "--aggregate", "rating=min"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        encoding="utf-8"
    )

    assert result.returncode == 0
    assert "min(rating)" in result.stdout
    assert "4.3" in result.stdout
