from flows import donor_flow, recipient_flow

def identify_role(text):
    text = text.lower()
    if "donor" in text or "donate" in text:
        return "donor"
    elif "need" in text or "patient" in text or "recipient" in text:
        return "recipient"
    return "unknown"


def chatbot_response(user_input, state):
    role = identify_role(user_input)

    if role == "donor":
        state["role"] = "donor"
        return donor_flow()

    if role == "recipient":
        state["role"] = "recipient"
        return recipient_flow()

    if state.get("role") == "donor":
        return donor_flow(user_input)

    if state.get("role") == "recipient":
        return recipient_flow(user_input)

    return (
        "I am an Organ Donation AI Assistant 🫀\n\n"
        "I can help you with:\n"
        "- Donor registration\n"
        "- Patient priority assessment\n"
        "- Match status\n\n"
        "Please type **donor** or **recipient** to continue."
    )
