"""Tests for is_valid_username, count_words, truncate  (function-style tests)."""
import pytest

from qe_utils import count_words, is_valid_username, truncate


# ---- WORKED EXAMPLE (already done for you; read it, then copy the pattern) ----
@pytest.mark.smoke
def test_username_valid_simple_name():
    # Arrange
    name = "qe_trainee"
    # Act
    result = is_valid_username(name)
    # Assert
    assert result is True


# ---- TODO tests: replace each `pytest.fail(...)` line with real test code ----
@pytest.mark.boundary
@pytest.mark.regression
def test_username_too_short_is_rejected():
    # TODO (Task 3): 2 characters must be rejected. Add markers: boundary, regression
    name = "qe"
    result = is_valid_username(name)
    assert result is False

@pytest.mark.boundary
@pytest.mark.regression
def test_username_exactly_3_chars_is_accepted():
    # TODO (Task 3): lower boundary. Markers: boundary, regression
    name = "abc"
    result = is_valid_username(name)
    assert result is True

@pytest.mark.boundary
@pytest.mark.regression
def test_username_16_chars_is_rejected():
    # TODO (Task 3): upper boundary + 1. Markers: boundary, regression
    name = "abcdefghijklmnop"
    result = is_valid_username(name)
    assert result is False

@pytest.mark.regression
def test_username_starting_with_digit_is_rejected():
    # TODO (Task 3): "1abc" -> False. Marker: regression
    name = "1abc"
    result = is_valid_username(name)
    assert result is False

@pytest.mark.regression
def test_username_with_space_or_symbol_is_rejected():
    # TODO (Task 3): "bad name" and "bad-name" -> False (two asserts are fine). Marker: regression
    name1 = "bad name"
    name2 = "bad-name"
    result1 = is_valid_username(name1)
    result2 = is_valid_username(name2)
    assert result1 is False
    assert result2 is False


def test_username_non_string_raises_type_error():
    # TODO (Task 4): use pytest.raises(TypeError, match=...) with the input 12345
    with pytest.raises(TypeError, match="username must be a string"):
        is_valid_username(12345)

@pytest.mark.smoke
def test_count_words_simple_sentence():
    # TODO (Task 3): "quality is everyone's job" -> 4. Marker: smoke
    text = "quality is everyone's job"
    result = count_words(text)
    assert result == 4

@pytest.mark.boundary
@pytest.mark.regression
def test_count_words_empty_string_is_zero():
    # TODO (Task 3): "" -> 0. Markers: boundary, regression
    text = ""
    result = count_words(text)
    assert result == 0


def test_count_words_non_string_raises_type_error():
    # TODO (Task 4): None must raise TypeError
    with pytest.raises(TypeError, match="text must be a string"):
        count_words(None)

@pytest.mark.smoke
def test_truncate_short_text_is_unchanged():
    # TODO (Task 3): truncate("hello", 10) == "hello". Marker: smoke
    text = "hello"
    max_len = 10
    result = truncate(text, max_len)
    assert result == "hello"

@pytest.mark.regression
def test_truncate_long_text_ends_with_ellipsis_and_has_max_len():
    # TODO (Task 3): truncate("abcdefghij", 8) == "abcde..."  (len 8). Marker: regression
    text = "abcdefghij"
    max_len = 8
    result = truncate(text, max_len)
    assert result == "abcde..."

@pytest.mark.boundary
@pytest.mark.regression
@pytest.mark.xfail(reason="Known bug: text is truncated even when its length equals max_len", strict=True)
def test_truncate_text_exactly_max_len_is_unchanged():
    # TODO (Task 6): by the docstring, text that fits exactly must NOT be cut.
    # Write the test according to the docstring. It will FAIL - why?
    # Then mark it as a known bug:  @pytest.mark.xfail(reason="...", strict=True)
    # Markers: boundary, regression
    text = "abcdefgh"
    max_len = 8
    result = truncate(text, max_len)
    assert result == "abcdefgh"

def test_truncate_max_len_below_3_raises_value_error():
    # TODO (Task 4): max_len=2 -> ValueError, check the message with match=
    with pytest.raises(ValueError, match="max_len must be at least 3"):
        truncate("hello", 2)
        
