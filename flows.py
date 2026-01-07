def donor_flow(user_input=None):
    if not user_input:
        return (
            "Thank you for choosing to become a donor ❤️\n\n"
            "Please answer a few questions.\n"
            "Do you have any chronic diseases? (Yes/No)"
        )

    if "yes" in user_input.lower():
        return (
            "Thank you for your honesty.\n"
            "Based on your response, further medical verification is required.\n"
            "Our system will evaluate eligibility safely."
        )

    if "no" in user_input.lower():
        return (
            "Great 👍\n"
            "You appear eligible for donation.\n"
            "Your details will be verified to prevent fake registrations."
        )

    return "Please answer Yes or No."


def recipient_flow(user_input=None):
    if not user_input:
        return (
            "I understand you are waiting for an organ.\n\n"
            "Please describe your medical condition."
        )

    if "critical" in user_input.lower() or "dialysis" in user_input.lower():
        return (
            "Your condition indicates **high medical urgency**.\n"
            "You are prioritized by the ML-based system.\n"
            "You will be notified immediately when a match is found."
        )

    return (
        "Thank you for the information.\n"
        "Your priority will be assessed based on medical urgency and compatibility."
    )
