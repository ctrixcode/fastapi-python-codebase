from src.core.utils import format_username


def test_format_username():
    """
    Tests the username formatting utility.
    """
    assert format_username("  JohnDoe  ") == "johndoe"
    assert format_username("JaneDoe") == "janedoe"
    assert format_username("  leading") == "leading"
    assert format_username("trailing  ") == "trailing"
