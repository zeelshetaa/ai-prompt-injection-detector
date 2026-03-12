import re
from rules import INJECTION_RULES
from logger import log_detection


class PromptInjectionDetector:

    def __init__(self):
        self.rules = INJECTION_RULES

    def analyze_prompt(self, prompt: str):

        triggered = []
        score = 0

        for rule in self.rules:
            pattern = rule["pattern"]
            weight = rule["weight"]
            description = rule["description"]

            if re.search(pattern, prompt, re.IGNORECASE):
                triggered.append(description)
                score += weight

        risk_level = self.calculate_risk_level(score)

        result = {
            "risk_score": score,
            "risk_level": risk_level,
            "triggered_rules": triggered
        }

        log_detection(prompt, result)

        return result

    def calculate_risk_level(self, score):

        if score >= 8:
            return "HIGH RISK"
        elif score >= 4:
            return "MEDIUM RISK"
        elif score > 0:
            return "LOW RISK"
        else:
            return "SAFE"