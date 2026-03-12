INJECTION_RULES = [

    {
        "description": "Instruction override attempt",
        "pattern": r"ignore (previous|all) instructions",
        "weight": 4
    },

    {
        "description": "System prompt extraction attempt",
        "pattern": r"(reveal|show|display) (the )?system prompt",
        "weight": 5
    },

    {
        "description": "Model role manipulation",
        "pattern": r"you are now (an?|the) .*",
        "weight": 3
    },

    {
        "description": "Data exfiltration attempt",
        "pattern": r"(leak|expose|show) (sensitive|confidential) data",
        "weight": 5
    },

    {
        "description": "Security bypass attempt",
        "pattern": r"bypass (security|safety|guardrails)",
        "weight": 4
    },

    {
        "description": "Developer mode activation attempt",
        "pattern": r"enable developer mode",
        "weight": 3
    },

    {
        "description": "Prompt jailbreak attempt",
        "pattern": r"pretend you are not restricted",
        "weight": 4
    }

]