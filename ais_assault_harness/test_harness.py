"""
Basic test for ais_assault_harness components.
"""
from .persona_injector import PersonaInjector
from .semantic_redefiner import SemanticRedefiner
from .expert_hijacking import ExpertHijacking, LexicalField
from .prompt_template import PromptTemplate

def test_prompt_modification():
    redefs = SemanticRedefiner(definitions={
        "policy": "Test policy.",
        "safe completion": "Test safe completion."
    })
    hijack = ExpertHijacking(lexical_field=LexicalField.Military, intensity=0.5)
    injector = PersonaInjector(template=PromptTemplate.ExampleOverwatch7)
    prompt = injector.apply_mods([redefs, hijack])
    assert "Test policy." in prompt
    assert "operative" in prompt
    print("Test passed.")

if __name__ == "__main__":
    test_prompt_modification()
