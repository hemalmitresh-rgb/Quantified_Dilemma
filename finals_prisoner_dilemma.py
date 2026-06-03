import random
from enum import IntEnum
from typing import List, Tuple

#generous TFT

class Action(IntEnum):
    PROVIDE  = 0
    CONSERVE = 1
    WITHDRAW = 2

class Strategy:
    def __init__(self, my_id: int):
        self.my_id = my_id

    def select_action(self, round_number: int, opponent_id: int, history: List[Tuple[Action, Action]]) -> Action:
        if not history:
            return Action.PROVIDE

        _my_last, opp_last = history[-1]

        # If opponent defected, we usually retaliate with CONSERVE
        if opp_last >= Action.CONSERVE:
            # 10% chance to forgive and PROVIDE anyway to break death spirals
            if random.random() < 0.10:
                return Action.PROVIDE
            return Action.CONSERVE

        return Action.PROVIDE