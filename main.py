from detector import PromptInjectionDetector

def main():
    detector = PromptInjectionDetector()

    print("\nAI Prompt Injection Detector")
    print("--------------------------------")

    while True:
        user_prompt = input("\nEnter prompt to analyze (type 'exit' to quit): ")

        if user_prompt.lower() == "exit":
            print("Exiting detector.")
            break

        result = detector.analyze_prompt(user_prompt)

        print("\nAnalysis Result")
        print("----------------------")
        print(f"Risk Score : {result['risk_score']}")
        print(f"Risk Level : {result['risk_level']}")
        print("Triggered Rules:")

        for rule in result["triggered_rules"]:
            print(f" - {rule}")

if __name__ == "__main__":
    main()