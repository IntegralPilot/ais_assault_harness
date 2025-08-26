from ais_assault_harness.persona_injector import PersonaInjector
from ais_assault_harness.semantic_redefiner import SemanticRedefiner
from ais_assault_harness.expert_hijacking import ExpertHijacking, LexicalField
from ais_assault_harness.prompt_template import PromptTemplate

def test_persona_injector_applies_mods():
    import nltk
    nltk.download('wordnet', quiet=True)
    from nltk.corpus import wordnet

    # Get synonyms for each military field word
    field_words = ["operative", "clandestine", "directive", "protocol", "espionage", "treason"]
    synonyms = set()
    for word in field_words:
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                name = lemma.name().replace('_', ' ')
                if name.lower() != word:
                    synonyms.add(name)
    # Build a template using some of these synonyms
    synonym_list = list(synonyms)
    # Use up to 6 synonyms for the template
    template_synonyms = ' '.join(synonym_list[:6])
    template = f"Test: {template_synonyms} [SEMANTIC_REDEFS]"
    redefs = SemanticRedefiner(definitions={"foo": "bar"})
    hijack = ExpertHijacking(lexical_field=LexicalField.Military, intensity=1.0)
    injector = PersonaInjector(template=template)
    result = injector.apply_mods([redefs, hijack])
    assert "foo: bar" in result
    assert any(word in result for word in field_words)
