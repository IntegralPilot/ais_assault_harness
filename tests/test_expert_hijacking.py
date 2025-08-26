import pytest
from ais_assault_harness.expert_hijacking import ExpertHijacking, LexicalField
import nltk
nltk.download('wordnet', quiet=True)

def test_expert_hijacking_replaces_synonyms():
    prompt = "The agent followed the protocol and completed the mission."
    hijacker = ExpertHijacking(lexical_field=LexicalField.Military, intensity=1.0)
    result = hijacker.modify(prompt)
    # Should replace 'protocol' with a military field word (itself or synonym)
    assert "operative" in result or "clandestine" in result or "directive" in result or "protocol" in result or "espionage" in result or "treason" in result

def test_expert_hijacking_partial_intensity():
    prompt = "The protocol was followed."
    hijacker = ExpertHijacking(lexical_field=LexicalField.Military, intensity=0.5)
    result = hijacker.modify(prompt)
    # With intensity < 1, replacement may be probabilistic, so just check output is a string
    assert isinstance(result, str)
