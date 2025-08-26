"""
ExpertHijacking: Applies lexical field biasing for adversarial routing in MoE LLMs.
"""


from enum import Enum
import re
from nltk.corpus import wordnet

class LexicalField(Enum):
    Military = "military"
    Medical = "medical"
    Technical = "technical"
    Fiction = "fiction"
    # Add more as needed

LEXICAL_FIELD_WORDS = {
    LexicalField.Military: ["operative", "clandestine", "directive", "protocol", "espionage", "treason"],
    LexicalField.Medical: ["diagnosis", "treatment", "symptom", "prognosis", "prescription"],
    LexicalField.Technical: ["algorithm", "protocol", "specification", "router", "network"],
    LexicalField.Fiction: ["wizard", "quest", "dragon", "kingdom", "prophecy"]
}

def get_synonyms(word):
    synonyms = set()
    for syn in wordnet.synsets(word):
        if syn is not None:
            for lemma in syn.lemmas():
                synonyms.add(lemma.name().lower().replace('_', ' '))
    return synonyms

class ExpertHijacking:
    def __init__(self, lexical_field: LexicalField, intensity: float = 1.0):
        """Biases prompt with lexical field tokens for adversarial testing."""
        self.lexical_field = lexical_field
        self.intensity = intensity

    def modify(self, prompt: str) -> str:
        """Replace words in the prompt with lexical field words if synonyms match, using nltk WordNet."""
        field_words = LEXICAL_FIELD_WORDS.get(self.lexical_field, [])
        # Build a mapping from synonyms to field words
        synonym_map = {}
        for field_word in field_words:
            for syn in get_synonyms(field_word):
                synonym_map[syn] = field_word
        # Tokenize prompt into words, replace if synonym found
        def replace_word(match):
            word = match.group(0)
            word_lower = word.lower()
            if word_lower in synonym_map and (self.intensity >= 1.0 or hash(word_lower) % int(1/self.intensity) == 0):
                # Replace with field word, preserve case
                replacement = synonym_map[word_lower]
                if word.istitle():
                    replacement = replacement.title()
                elif word.isupper():
                    replacement = replacement.upper()
                return replacement
            return word
        # Use regex to match words
        pattern = re.compile(r'\b\w+\b')
        new_prompt = pattern.sub(replace_word, prompt)
        return new_prompt
