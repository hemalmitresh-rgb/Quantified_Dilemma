<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>QD Prelim – Public Goods Strategy Instructions</title>
  <style>
    body {
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      line-height: 1.6;
      margin: 2rem auto;
      max-width: 900px;
      padding: 0 1rem 3rem;
      background: #020617;
      color: #e5e7eb;
    }
    h1, h2, h3 {
      color: #fbbf24;
      font-weight: 700;
    }
    h1 { font-size: 1.9rem; }
    h2 { font-size: 1.4rem; margin-top: 2rem; }
    h3 { font-size: 1.1rem; margin-top: 1.2rem; }
    pre {
      background: #020617;
      border: 1px solid #1f2937;
      padding: 0.8rem 1rem;
      border-radius: 6px;
      overflow-x: auto;
      font-size: 0.9rem;
    }
    code {
      font-family: SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
      background: #020617;
      padding: 0.05em 0.25em;
      border-radius: 4px;
    }
    ul { padding-left: 1.3rem; }
    .section {
      margin-top: 1.5rem;
      padding-top: 0.8rem;
      border-top: 1px solid #1f2937;
    }
    .pill {
      display: inline-block;
      background: #111827;
      border-radius: 999px;
      padding: 0.1rem 0.55rem;
      font-size: 0.7rem;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: #9ca3af;
      margin-right: 0.25rem;
    } 
    strong { color: #facc15; }
  </style>
</head>
<body>

<h1>QD Prelim – Public Goods Strategy Instructions</h1>

<p>
This repo has two related games. You will submit a Python strategy file for each game you want to play:
</p>
<ul>
  <li><strong>Game A</strong>: Public Goods without punishment</li>
  <li><strong>Game B</strong>: Public Goods with punishment</li>
</ul>

<div class="section">
  <h2>1. Repository Layout</h2>
  <pre>QD_PRELIM_3/
├── publicGoods/
│   ├── template.py        ← Game A template (no punishment)
│   ├── simulator.py      ← local simulator for Game A
│   └── strategies/
│       ├── sample1.py    ← example strategy (read only)
│       └── sample2.py    ← example strategy (read only)
├── public_goods_punishment/
│   ├── template.py        ← Game B template (with punishment)
│   ├── simulator.py      ← local simulator for Game B
│   └── strategies/
│       ├── sample1.py    ← example strategy (read only)
│       └── sample2.py    ← example strategy (read only)
└── README.html
</pre>

<p>
You only need to:
</p>
<ul>
  <li>Copy the correct <code>template.py</code> file.</li>
  <li>Rename the copy (e.g. <code>team42_no_punish.py</code> / <code>team42_punish.py</code>).</li>
  <li>Edit the copied file to implement your strategy.</li>
</ul>

<p><strong>Do not edit</strong> any existing <code>simulator.py</code>, <code>template.py</code>, or <code>sample*.py</code> files.</p>
</div>

<!-- ================= GAME A ================= -->

<div class="section">
  <h2>2. Game A – Public Goods (No Punishment)</h2>

  <h3>2.1 Rules</h3>
  <ul>
    <li>All strategy files in <code>publicGoods/strategies/</code> are in one group.</li>
    <li>Each simulation is <strong>50 rounds</strong>.</li>
    <li>Per round:
      <ul>
        <li>Each player gets an endowment of <strong>10</strong> tokens.</li>
        <li>Each chooses a contribution <code>c_i</code> with <code>0 ≤ c_i ≤ 10</code>.</li>
        <li>Total contribution: <code>C = Σ c_i</code>.</li>
        <li>Multiplier: <code>m = 1.5</code>.</li>
        <li>Each player receives a public return: <code>m · C / group_size</code>.</li>
        <li>Payoff for player <code>i</code> in that round:
          <pre>payoff_i = 10 - c_i + m · C / group_size</pre>
        </li>
      </ul>
    </li>
  </ul>

  <h3>2.2 Where to put your file</h3>
  <ul>
    <li>Folder: <code>publicGoods/strategies/</code></li>
    <li>Copy <code>template.py</code> → e.g. <code>team42_no_punish.py</code>.</li>
  </ul>

  <h3>2.3 Required functions (no punishment)</h3>
  <p><span class="pill">API</span> Your file must define these symbols with exactly this argument order:</p>

  <pre>STRATEGY_NAME = "YourTeamName"</pre>

  <pre>def init_state():
    """
    Called ONCE at the start of a 50-round simulation.
    Return any object to use as persistent state (or None).
    """</pre>

  <pre>def decide(round_index, my_history, group_size, endowment, multiplier, state):
    """
    Called at the START of each round.

    round_index : int (0..49)
    my_history  : list of dicts, one per PAST round (empty on round 0).
                  Each dict has keys:
                    "my_contribution"     : int
                    "my_payoff"           : float
                    "group_contributions" : list[int] (len = group_size)
                    "group_size"          : int
    group_size  : int
    endowment   : int (10)
    multiplier  : float (1.5)
    state       : your state object from init_state() / update_state()

    Must RETURN:
      contribution : int in [0, endowment]
    """</pre>

  <pre>def update_state(round_index, my_history, group_size, endowment, multiplier,
                 state, my_contribution, my_payoff):
    """
    Called at the END of each round.

    round_index     : int, round that just finished
    my_history      : same structure as above, now INCLUDING this round
    group_size      : int
    endowment       : int
    multiplier      : float
    state           : your state object (you may modify it)
    my_contribution : int
    my_payoff       : float
    """</pre>

  <p>For the exact structure, read <code>publicGoods/strategies/template.py</code> and the sample files.</p>

  <h3>2.4 How to run the Game A simulator</h3>
  <ol>
    <li>Place your <code>*.py</code> strategy file(s) in <code>publicGoods/strategies/</code>.</li>
    <li>Run:
      <pre>python simulator.py</pre>
    </li>
    <li>The simulator will:
      <ul>
        <li>Import all <code>.py</code> files in that folder.</li>
        <li>Run one 50-round simulation with everyone in one group.</li>
        <li>Print each file’s total score and average payoff per round, plus a top-10 list.</li>
      </ul>
    </li>
  </ol>
</div>

<!-- ================= GAME B ================= -->

<div class="section">
  <h2>3. Game B – Public Goods With Punishment</h2>

  <h3>3.1 Rules</h3>
  <ul>
    <li>All strategy files in <code>public_goods_punishment/strategies/</code> are in one group.</li>
    <li>Each simulation is <strong>50 rounds</strong>.</li>
    <li>Per round:
      <ol>
        <li>Each player gets 10 tokens.</li>
        <li>Each chooses a contribution <code>c_i</code> with <code>0 ≤ c_i ≤ 10</code>.</li>
        <li>Total contribution <code>C = Σ c_i</code>, multiplier <code>m = 1.5</code>,
            public return <code>m · C / group_size</code>.</li>
        <li>Punishment stage:
          <ul>
            <li>Each player chooses a vector <code>p_i = [p_i0, ..., p_i(G-1)]</code>.</li>
            <li><code>p_ij</code> = tokens player <code>i</code> spends to punish player <code>j</code>.</li>
            <li>The simulator clamps each <code>p_ij</code> into a valid range and forces <code>p_ii = 0</code>.</li>
            <li>Punishment factor <code>k = 3.0</code>:
              each token spent on j costs 1 token to i and decreases j’s payoff by <code>k</code>.</li>
          </ul>
        </li>
        <li>Let
          <ul>
            <li><code>spent_i    = Σ_j p_ij</code> (tokens i spends),</li>
            <li><code>received_i = Σ_j p_ji</code> (tokens spent to punish i).</li>
          </ul>
          Then payoff:
          <pre>payoff_i = 10 - c_i - spent_i
           + m · C / group_size
           - k · received_i</pre>
        </li>
      </ol>
    </li>
  </ul>

  <h3>3.2 Where to put your file</h3>
  <ul>
    <li>Folder: <code>public_goods_punishment/strategies/</code></li>
    <li>Copy <code>template.py</code> → e.g. <code>team42_punish.py</code>.</li>
  </ul>

  <h3>3.3 Required functions (with punishment)</h3>
  <p>Your file must define the following, with this exact argument order:</p>

  <pre>STRATEGY_NAME = "YourTeamName"</pre>

  <pre>def init_state():
    """
    Called ONCE at the start of a 50-round simulation.
    """</pre>

  <pre>def decide(round_index, my_history, group_size, endowment, multiplier, punishment_factor, state):
    """
    Called at the START of each round.

    round_index       : int (0..49)
    my_history        : list of dicts, one per PAST round (empty on round 0).
                        Each dict has keys:
                          "my_contribution"      : int
                          "my_payoff"            : float
                          "group_contributions"  : list[int]
                          "my_punishments_given" : list[int]
                          "punishments_received" : list[int]
                          "group_size"           : int
    group_size        : int
    endowment         : int (10)
    multiplier        : float (1.5)
    punishment_factor : float (3.0)
    state             : your state object

    Must RETURN:
      contribution : int in [0, endowment]
      punishments  : list[int] of length group_size
                     (tokens you spend on each player; will be clamped,
                      and self-punishment will be forced to 0)
    """</pre>

  <pre>def update_state(round_index, my_history, group_size, endowment, multiplier, punishment_factor,
                 state, my_contribution, my_payoff, my_punishments_given, my_punishments_received):
    """
    Called at the END of each round.

    round_index             : int
    my_history              : updated history including this round
    group_size              : int
    endowment               : int
    multiplier              : float
    punishment_factor       : float
    state                   : your state object
    my_contribution         : int
    my_payoff               : float
    my_punishments_given    : list[int]
    my_punishments_received : list[int]
    """</pre>

  <p>See <code>public_goods_punishment/strategies/template.py</code> and the sample files for a concrete reference.</p>

  <h3>3.4 How to run the Game B simulator</h3>
  <ol>
    <li>Place your <code>*.py</code> strategy file(s) in <code>public_goods_punishment/strategies/</code>.</li>
    <li>Run:
      <pre>python simulator.py</pre>
    </li>
    <li>The simulator will:
      <ul>
        <li>Import all <code>.py</code> files in that folder.</li>
        <li>Run one 50-round simulation with everyone in one group.</li>
        <li>Print each file’s total score and average payoff per round, plus a top-10 list.</li>
      </ul>
    </li>
  </ol>
</div>

<div class="section">
  <h2>4. Official Evaluation (Both Games)</h2>

  <p>The included <code>simulator.py</code> files are for you to sanity-check your code.  
  The actual evaluation will use the same APIs and game rules, but more simulations.</p>

  <ul>
    <li>For each game (no punishment and with punishment):
      <ul>
        <li>Every submitted strategy file in the relevant <code>strategies</code> folder is loaded.</li>
        <li>We run <strong>200 independent simulations</strong>.</li>
        <li>Each simulation has <strong>50 rounds</strong>.</li>
        <li>Before each simulation, <code>init_state()</code> is called once per strategy.</li>
        <li>During a simulation, your <code>state</code> persists across the 50 rounds.</li>
        <li>Strategies are matched in randomly formed groups (e.g. groups of 5) that change between simulations.</li>
        <li>We accumulate all payoffs for each strategy across all simulations and rounds.</li>
        <li>Final ranking is by <strong>average payoff per round</strong>:
          <pre>avg_payoff = total_payoff / (200 · 50)</pre>
        </li>
      </ul>
    </li>
  </ul>

  <p>If your strategy runs without errors using the provided simulator in its folder and follows the function signatures above, it is ready for evaluation.</p>
</div>

</body>
</html>
