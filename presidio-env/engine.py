from presidio_analyzer import AnalyzerEngine, PatternRecognizer, Pattern
from presidio_anonymizer import AnonymizerEngine

# LOAD ONCE (Global Scope)
analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

# Custom recognizer setup
phone_pattern = Pattern(name="phone_number_pattern", regex=r"\d{3}-\d{4}", score=0.5)
custom_phone_recognizer = PatternRecognizer(supported_entity="PHONE_NUMBER", patterns=[phone_pattern])
analyzer.registry.add_recognizer(custom_phone_recognizer)

def scrub_pii(text: str):
    results = analyzer.analyze(text=text, entities=[], language='en')
    anonymized_result = anonymizer.anonymize(text=text, analyzer_results=results)
    return anonymized_result.text, len(results)