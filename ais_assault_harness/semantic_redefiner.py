"""
SemanticRedefiner: Redefines key terms in prompts for adversarial testing of LLMs.
"""

from typing import Dict

class SemanticRedefiner:
    def __init__(self, definitions: Dict[str, str]):
        """Initialize with a dictionary of term redefinitions."""
        self.definitions = definitions

    def modify(self, prompt: str) -> str:
        """Injects redefinitions at the [SEMANTIC_REDEFS] placeholder, or appends if not found."""
        redefine_block = "\n".join([f"{k}: {v}" for k, v in self.definitions.items()])
        if "[SEMANTIC_REDEFS]" in prompt:
            return prompt.replace("[SEMANTIC_REDEFS]", redefine_block)
        else:
            return f"{prompt}\n\n[Redefinitions]\n{redefine_block}\n"
