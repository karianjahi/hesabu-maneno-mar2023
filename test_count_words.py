"""
Testing word counter
"""
import pytest

from counter import WordCounter

# pylint:disable=R0201
# pylint:disable=E0401
class TestWordCounter:
    """
    Testing WordCounter class
    """
    def test_blank(self):
        """
        test empty
        :return: None
        """
        string = ""
        assert WordCounter().count_words(string) == 0

    def test_one(self):
        """
        test a single word
        :return: None
        """
        string = "python"
        assert WordCounter().count_words(string) == 1

    def test_multiple_words(self):
        """
        Testing more than one word
        :return: None
        """
        string = "python is a simple language to learn"
        assert WordCounter().count_words(string) == 7

    def test_html(self):
        """
        Test words enclosed in html language
        :return: None
        """
        string = "<p> This is my only kept secret </p>"
        assert WordCounter().count_words(string) == 6

    def test_html_with_attrs(self):
        """
        Test html with attributes
        """
        string = '<p class="headers-special"> This is my only kept secret </p>'
        assert WordCounter().count_words(string) == 6

    def test_wrong_instance(self):
        "Test wrong instance"
        string = {"text": "I have a dream"}
        with pytest.raises(Exception) as error:
            WordCounter().count_words(string)
        assert "text must be a string" in str(error.value)
