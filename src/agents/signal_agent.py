from src.pipeline.extract_signals import SignalExtractor


class SignalAgent:

    def __init__(self):

        self.extractor = SignalExtractor()

    def analyze(self, text):

        return self.extractor.extract(text)