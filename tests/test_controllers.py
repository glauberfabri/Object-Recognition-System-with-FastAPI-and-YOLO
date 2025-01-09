from app.controllers import process_image
from unittest.mock import AsyncMock

async def test_process_image():
    mock_file = AsyncMock()
    mock_file.filename = "test_image.jpg"
    mock_file.read.return_value = b"fake_image_data"

    result = await process_image(mock_file)
    assert "image" in result
    assert "objects_detected" in result
