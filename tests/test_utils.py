from app.utils import validate_image_file, list_to_string

def test_validate_image_file():
    class MockFile:
        filename = "test_image.png"

    assert validate_image_file(MockFile()) is True

def test_list_to_string():
    items = ["car", "tree", "house"]
    result = list_to_string(items)
    assert result == "car, tree, house"
