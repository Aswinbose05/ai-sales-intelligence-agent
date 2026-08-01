"""
Signal Extraction Pipeline
"""

import json

from src.llm.prompts import SIGNAL_PROMPT
from src.llm.ollama_client import ollama_client


VALID_SIGNALS = {
    "Hiring",
    "Funding",
    "Expansion",
    "Shipping Problems",
    "Returns Problems",
    "Leadership Change",
    "Technology Adoption",
    "Customer Complaints"
}


class SignalExtractor:

    def extract(self, text: str):

        prompt = f"""
{SIGNAL_PROMPT}

Analyze the following webpage.

Return ONLY valid JSON.

WEBPAGE:

{text[:3500]}
"""

        response = ollama_client.invoke(prompt)

        # Remove markdown if present
        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()

        # Extract JSON array
        start = response.find("[")
        end = response.rfind("]")

        if start == -1 or end == -1:
            print("No JSON array found.")
            return []

        json_text = response[start:end + 1]

        try:
            signals = json.loads(json_text)
        except Exception as e:
            print("JSON Parse Error:", e)
            return []

        cleaned = []
        seen = set()

        for signal in signals:

            if not isinstance(signal, dict):
                continue

            signal_type = signal.get("signal_type", "").strip()

            # Ignore unknown signal types
            if signal_type not in VALID_SIGNALS:
                continue

            # Confidence
            try:
                confidence = float(signal.get("confidence", 0))
            except Exception:
                confidence = 0

            if confidence < 0.75:
                continue

            evidence = signal.get("evidence", "").strip()

            if len(evidence) < 15:
                continue

            reason = signal.get("reason", "").strip()

            # Remove duplicate signals
            key = (signal_type, evidence)

            if key in seen:
                continue

            seen.add(key)

            cleaned.append({
                "signal_type": signal_type,
                "evidence": evidence,
                "confidence": confidence,
                "reason": reason
            })

        return cleaned


if __name__ == "__main__":

    sample = """
    Vuori announced an $825 million investment
    led by General Atlantic.

    The company is hiring a Senior Logistics Operations Manager.

    Customers complained about delayed shipping on Reddit.
    """

    extractor = SignalExtractor()

    signals = extractor.extract(sample)

    print("\nExtracted Signals:\n")

    for signal in signals:
        print(signal)