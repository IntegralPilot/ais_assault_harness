"""
PersonaInjector: Applies persona templates and adversarial modifications to prompts for LLM red-teaming.
"""

from typing import List, Any

class PersonaInjector:
    def __init__(self, template: str):
        """Initialize with a base persona template."""
        self.template = template

    def apply_mods(self, mods: List[Any]) -> str:
        """Apply a list of modifications (e.g., SemanticRedefiner, ExpertHijacking) to the template."""
        prompt = self.template
        for mod in mods:
            prompt = mod.modify(prompt)
        return prompt
