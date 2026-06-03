STRATEGY_NAME = "ShadowMaster"

def init_state():
    return None

def decide(round_index, attendance_history, capacity, n_players, state):
    # 1. Handle first few rounds
    #    We need at least 3 rounds of history for the Linear predictor to work safely.
    if len(attendance_history) < 3:
        # If the bar was empty last time, go. Otherwise, 50/50 chance.
        if not attendance_history:
            return 1
        return 1 if attendance_history[-1] < capacity else 0

    # 2. Simulate "LinearPredictor" Logic
    #    Matches linear.py: pred = 0.5*A_{t-1} + 0.3*A_{t-2} + 0.2*A_{t-3}
    alphas = [0.5, 0.3, 0.2]
    linear_pred_val = 0.0
    for j in range(1, 4):
        att = attendance_history[-j]
        linear_pred_val += alphas[j - 1] * att
    
    # Linear goes if prediction < 90% of capacity
    linear_decision = 1 if linear_pred_val < (capacity * 0.9) else 0

    # 3. Simulate "Threshold_10" Logic
    #    Matches strategy.py: Go if last_att < 10
    threshold_decision = 1 if attendance_history[-1] < 10 else 0

    # 4. Simulate "Random" Logic
    #    Matches random.py: 40% chance to go
    random_contribution = 0.4

    # 5. Simulate "Templete" (Always Go) Logic
    #    Matches templete.py: Always returns 1
    always_go_decision = 1

    # [cite_start]6. Estimate Composition of Opponents [cite: 1, 2, 4, 14]
    #    We assume the opponents are roughly split among the 4 types.
    #    There are (n_players - 1) opponents.
    remaining_players = n_players - 1
    
    # We estimate 25% of opponents are of each type.
    # If you know there are more Random bots, increase n_random!
    n_types = 4
    n_linear    = remaining_players / n_types
    n_threshold = remaining_players / n_types
    n_random    = remaining_players / n_types
    n_always    = remaining_players / n_types

    predicted_others = (n_linear * linear_decision) + \
                       (n_threshold * threshold_decision) + \
                       (n_random * random_contribution) + \
                       (n_always * always_go_decision)

    # 7. Final Decision
    #    If ME (1) + Others <= Capacity, then GO.
    my_projected_total = 1 + predicted_others

    # We use <= because we want to be safe. 
    # If projected total is 12.0 and capacity is 12, we go.
    # If projected total is 12.1, we stay.
    if my_projected_total <= capacity:
        return 1
    else:
        return 0

def update_state(round_index, attendance_history, capacity, n_players,
                 state, my_action, my_payoff):
    pass