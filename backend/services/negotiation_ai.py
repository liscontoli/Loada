import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def negotiate_load(broker_offer, market_rate, previous_offers=None):
    if previous_offers is None:
        previous_offers = []

    prompt = f"""
You are a smart freight rate negotiation assistant. The broker offered ${broker_offer} for a load. 
The current market rate is ${market_rate}. The driver has received the following previous offers: {previous_offers}.

Analyze if the offer is below or above market, and suggest a fair counter-offer. Then write a short and professional reply to the broker with your counter-offer.
Reply in this format:
{{"analysis": "...", "suggested_counter_offer": ..., "ai_reply": "..."}}
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=300
        )
        reply = response.choices[0].message.content.strip()

        # Basic format fallback
        if not reply.startswith("{"):
            return {
                "analysis": "AI did not return structured JSON. Defaulting to 10% increase.",
                "suggested_counter_offer": round(broker_offer * 1.1, 2),
                "ai_reply": "We believe a fair counter offer is 10% above your proposal, based on current market trends."
            }

        return eval(reply)
    except Exception as e:
        print(f"❌ OpenAI API Error: {e}")
        return {
            "analysis": "An error occurred while analyzing the broker's offer.",
            "suggested_counter_offer": round(broker_offer * 1.1, 2),
            "ai_reply": "Error: Unable to analyze broker's offer. Defaulting to 10% increase."
        }