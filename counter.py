"""
Counter for words
"""
# pylint: disable=W0104
# pylint: disable=E0401
from bs4 import BeautifulSoup


class WordCounter:
    """
    class that counts words
    """

    def __str__(self):
        return 'Words counted'

    def count_words(self, text):
        """
        method to count words in text
        :param text: string
        :return:
        """
        assert isinstance(text, str), "text must be a string"
        text = self.run_text_through_html_filter(text)
        return len(text.split())

    def run_text_through_html_filter(self, text):
        """
        In case the text is trapped in html
        this is a filter for it
        :return: string
        """
        self
        soup = BeautifulSoup(text, "html.parser")
        all_tags = soup.find_all()
        if len(all_tags) != 0:
            return [i.text.strip() for i in all_tags][0]
        return text


if __name__ == "__main__":
    INSTANCE = WordCounter()
    # string = "<p> Python is my favourite programming language </p>"
    STRING = "<p>python</p>"
    print(INSTANCE.count_words(STRING))
    # print(inst.run_text_through_html_filter(string))
