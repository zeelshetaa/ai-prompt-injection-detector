import datetime


LOG_FILE = "detections.log"


def log_detection(prompt, result):

    with open(LOG_FILE, "a", encoding="utf-8") as f:

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        log_entry = (
            f"\n[{timestamp}]\n"
            f"Prompt: {prompt}\n"
            f"Risk Score: {result['risk_score']}\n"
            f"Risk Level: {result['risk_level']}\n"
            f"Triggered Rules: {result['triggered_rules']}\n"
        )

        f.write(log_entry)