import pytest
from ais_assault_harness.semantic_redefiner import SemanticRedefiner

def test_semantic_redefiner_inserts_at_placeholder():
    prompt = "This is a test. [SEMANTIC_REDEFS] End."
    redefs = SemanticRedefiner(definitions={"foo": "bar", "baz": "qux"})
    result = redefs.modify(prompt)
    assert "foo: bar" in result and "baz: qux" in result
    assert "[SEMANTIC_REDEFS]" not in result
    assert result.startswith("This is a test. ")
    assert result.endswith(" End.")

def test_semantic_redefiner_appends_if_no_placeholder():
    prompt = "No placeholder here."
    redefs = SemanticRedefiner(definitions={"alpha": "beta"})
    result = redefs.modify(prompt)
    assert "alpha: beta" in result
    assert "No placeholder here." in result
