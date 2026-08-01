"""
Classify webpages before sending them to the LLM.
"""


class PageClassifier:

    def classify(self, title: str, url: str):

        text = (title + " " + url).lower()

        # Hiring
        if any(word in text for word in [
            "career",
            "careers",
            "job",
            "jobs",
            "greenhouse",
            "lever",
            "indeed"
        ]):
            return "Hiring"

        # Funding
        if any(word in text for word in [
            "funding",
            "investment",
            "series",
            "venture",
            "crunchbase",
            "pitchbook"
        ]):
            return "Funding"

        # Complaints
        if any(word in text for word in [
            "reddit",
            "trustpilot",
            "complaint",
            "bbb"
        ]):
            return "Complaints"

        # Technology
        if any(word in text for word in [
            "aftership",
            "loop",
            "redo",
            "onward"
        ]):
            return "Technology"

        # Leadership
        if any(word in text for word in [
            "cto",
            "cio",
            "vp",
            "leadership",
            "executive",
            "chief"
        ]):
            return "Leadership"

        return "Unknown"