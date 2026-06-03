# strategies/AnticipatoryNash.py

def initial_distribution():
    # Start with the "Average Bot" Nash Equilibrium
    # Rock 44%, Paper 34%, Scissor 22%
    return [44, 34, 22]

def validate(probab, inc, dec):
    new = [probab[i] + inc[i] - dec[i] for i in range(3)]
    return all(0 <= x <= 100 for x in new) and sum(new) == 100

def re_distribute(probab, data_self, data_opp):
    # -----------------------------------------------------
    # STRATEGY: ANTICIPATORY COUNTER (Level 2 Thinking)
    # 1. Analyze MYSELF to see what the opponent sees.
    # 2. Predict their counter-move based on EV.
    # 3. Counter their predicted move.
    # -----------------------------------------------------

    last_opp = data_opp[-1]
    matches = sum(last_opp)
    
    # --- STEP 1: SAFETY CHECK (BOT DETECTION) ---
    # Level 2 thinking FAILS against dumb bots (they don't react).
    # If opponent is a Bot (>80% Paper), just crush them directly.
    # We check their actual play history for this.
    if matches > 0:
        opp_p_freq = last_opp[1] / matches
        if opp_p_freq > 0.8:
            # Bot detected! Switch to Hunter Mode (Scissors).
            # We ignore the complex logic below.
            if probab[0] >= 10: return [0, 0, 10], [10, 0, 0] # -Rock, +Scissor
            if probab[1] >= 10: return [0, 0, 10], [0, 10, 0] # -Paper, +Scissor

    # --- STEP 2: PREDICT OPPONENT'S MOVE ---
    # The opponent sees OUR current probabilities (approximated by 'probab').
    # They will try to maximize THEIR points against us.
    
    my_r = probab[0]
    my_p = probab[1]
    my_s = probab[2]
    
    # Opponent's Incentive to play ROCK:
    # They get 2 points if they catch our Scissor.
    opp_incentive_rock = 2.0 * my_s
    
    # Opponent's Incentive to play PAPER:
    # They get 1 point if they catch our Rock.
    opp_incentive_paper = 1.0 * my_r
    
    # Opponent's Incentive to play SCISSOR:
    # They get 1 point if they catch our Paper.
    opp_incentive_scissor = 1.0 * my_p
    
    incentives = [opp_incentive_rock, opp_incentive_paper, opp_incentive_scissor]
    
    # What is the opponent MOST likely to switch to?
    predicted_opp_move = incentives.index(max(incentives))
    # 0=Rock, 1=Paper, 2=Scissor
    
    # --- STEP 3: PREPARE THE TRAP ---
    # We don't want to beat what they played YESTERDAY.
    # We want to beat what they are shifting to TOMORROW (`predicted_opp_move`).
    
    # If they want Rock (0) -> We play Paper (1)
    # If they want Paper (1) -> We play Scissor (2)
    # If they want Scissor (2) -> We play Rock (0)
    
    my_counter_move = (predicted_opp_move + 1) % 3
    
    # --- STEP 4: EXECUTE ---
    increase = [0, 0, 0]
    decrease = [0, 0, 0]
    
    increase[my_counter_move] = 10
    
    # We need to decrease something. 
    # Ideally, we decrease the move that is "baiting" them the least,
    # OR we just decrease whatever we have most of (to stay agile).
    # Let's decrease the move that loses to their predicted move.
    # (If they are going to play Rock, we should decrease Scissor).
    avoid_move = (predicted_opp_move - 1 + 3) % 3 # The move that loses to prediction
    
    # Try to decrease the 'losing' move first
    if probab[avoid_move] >= 10:
        decrease[avoid_move] = 10
    else:
        # Fallback: Decrease any valid move that isn't our target
        found = False
        for i in range(3):
            if i != my_counter_move and probab[i] >= 10:
                decrease[i] = 10
                found = True
                break
        if not found:
            return [10, 0, 0], [10, 0, 0] # Null move

    return increase, decrease