from src.models import Signal

signal = Signal(
    company="Vuori",
    signal_type="Hiring",
    evidence="Hiring Logistics Manager",
    confidence=0.95,
    reason="Growing logistics team",
    page_type="Hiring",
    title="Vuori Careers",
    url="https://vuoriclothing.com/pages/careers"
)

print(signal)