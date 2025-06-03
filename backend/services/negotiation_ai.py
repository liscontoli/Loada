import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def negotiate_load(broker_offer, market_rate, previous_offers=None, countered_amount=None):
    if previous_offers is None:
        previous_offers = []

    # Initial negotiation prompt
    if countered_amount is None:
        prompt = f"""
You are an experienced freight negotiation assistant. The driver received a broker's offer of ${broker_offer} for a freight load. 
The current market rate is ${market_rate}.

Your task is to:
1. Analyze whether the broker's initial offer is fair based on the market rate.
2. If it's fair or above market, recommend that the driver accepts the offer and explain why.
3. If it's below market, suggest a fair counter-offer and explain your reasoning.
4. Write a short and professional reply the driver can send back to the broker.

Reply ONLY in the following structured JSON format:
{{
  "analysis": "...",
  "suggested_counter_offer": null OR number,
  "ai_reply": "..."
}}
"""
    else:
        # Counter-offer analysis prompt
        prompt = f"""
You are an experienced freight negotiation assistant. The driver initially countered the broker's offer. 
The broker has now replied with a counter-offer of ${countered_amount}. 
The current market rate is ${market_rate}.

Your task is to:
1. Analyze the broker’s new offer compared to the market rate and the driver’s expectations.
2. Recommend whether the driver should accept the new offer, counter again, or walk away.
3. Write a short and professional response the driver can send to the broker.

Reply ONLY in the following structured JSON format:
{{
  "analysis": "...",
  "suggested_counter_offer": null OR number,
  "ai_reply": "..."
}}
"""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            max_tokens=500
        )
        reply = response.choices[0].message.content.strip()

        # Fallback in case GPT doesn't return JSON
        if not reply.startswith("{"):
            return {
                "analysis": "AI did not return structured JSON. Defaulting to 10% counter offer increase.",
                "suggested_counter_offer": round(broker_offer * 1.1, 2),
                "ai_reply": "Based on market rates, a fair counter-offer would be 10% higher. Please consider adjusting the rate."
            }

        return eval(reply)

    except Exception as e:
        print(f"❌ OpenAI API Error: {e}")
        return {
            "analysis": "An error occurred while analyzing the broker's offer.",
            "suggested_counter_offer": round(broker_offer * 1.1, 2),
            "ai_reply": "Default suggestion: Offer seems low. Consider countering 10% higher."
        }