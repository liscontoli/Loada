def negotiate_load(
    pickup_location: str,
    dropoff_location: str,
    load_type: str,
    weight: float,
    distance: float,
    broker_offer: float,
    previous_offers: list[float]
):
    market_rate_per_mile = 2.75
    market_total = round(distance * market_rate_per_mile, 2)
    under_market = market_total - broker_offer
    counter_offer = round(broker_offer + under_market * 0.8, 2)

    if previous_offers:
        last_offer = previous_offers[-1]
        ai_reply = (
            f"Thanks for the update. The new offer of ${broker_offer} "
            f"is an improvement over the last offer of ${last_offer}. "
            f"However, it's still below the market rate (${market_total}). "
            f"Would you consider going up to ${counter_offer} to secure a truck quickly?"
        )
    else:
        ai_reply = (
            f"Hi, given the route and load type, the market rate is around ${market_rate_per_mile}/mile. "
            f"Would you be able to go up to ${counter_offer}? I’d like to move forward but need a fairer rate."
        )

    analysis = (
        f"The broker's offer of ${broker_offer} is ${under_market:.2f} under "
        f"the estimated market rate (${market_total:.2f})."
    )

    return {
        "analysis": analysis,
        "suggested_counter_offer": counter_offer,
        "ai_reply": ai_reply
    }
