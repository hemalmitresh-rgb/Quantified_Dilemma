<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Quantified Dilemma — Participant Rules</title>
  <style>
  :root{
    --bg: #0b0f14;
    --panel: #111827;
    --text: #e5e7eb;
    --muted: #a3a3a3;
    --border: rgba(255,255,255,0.10);
    --accent: #7c3aed;
    --accent2: #22c55e;
    --warn: #f59e0b;
    --codebg: rgba(255,255,255,0.06);
    --shadow: 0 10px 30px rgba(0,0,0,0.45);
  }

  * { box-sizing: border-box; }
  body{
    margin: 0;
    padding: 28px;
    background:
      radial-gradient(1200px 600px at 20% -10%, rgba(124,58,237,0.25), transparent 60%),
      radial-gradient(1000px 500px at 90% 0%, rgba(34,197,94,0.18), transparent 55%),
      var(--bg);
    color: var(--text);
    font-family: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Arial, "Apple Color Emoji","Segoe UI Emoji";
    line-height: 1.55;
  }

  .wrap{ max-width: 980px; margin: 0 auto; }

  h1{
    font-size: clamp(28px, 3vw, 38px);
    letter-spacing: -0.02em;
    margin: 0 0 6px;
  }

  h2{
    font-size: 18px;
    letter-spacing: -0.01em;
    margin: 0 0 10px;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  h2::before{
    content: "";
    width: 10px;
    height: 10px;
    border-radius: 999px;
    background: linear-gradient(135deg, var(--accent), var(--accent2));
    box-shadow: 0 0 0 4px rgba(124,58,237,0.18);
    flex: 0 0 auto;
  }

  p{ margin: 10px 0; }

  .subtitle{
    color: var(--muted);
    margin: 0 0 18px;
    max-width: 75ch;
  }

  .badgeRow{
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin: 14px 0 22px;
  }

  .badge{
    padding: 8px 12px;
    border: 1px solid var(--border);
    border-radius: 999px;
    background: rgba(255,255,255,0.04);
    box-shadow: 0 8px 20px rgba(0,0,0,0.25);
    font-size: 13px;
    color: var(--text);
  }

  .badge b{ color: #fff; }

  .card{
    border: 1px solid var(--border);
    border-radius: 16px;
    background: linear-gradient(180deg, rgba(255,255,255,0.05), rgba(255,255,255,0.02));
    padding: 18px 18px 16px;
    margin: 14px 0;
    box-shadow: var(--shadow);
    backdrop-filter: blur(6px);
  }

  .callout{
    border-left: 3px solid var(--warn);
    background: rgba(245,158,11,0.08);
    padding: 10px 12px;
    border-radius: 12px;
    margin-top: 10px;
    color: var(--text);
  }

  .muted{ color: var(--muted); }
  .small{ font-size: 0.95em; }

  ul, ol{ margin: 8px 0 0 1.2em; }
  li{ margin: 6px 0; }

  code, pre{
    background: var(--codebg);
    border: 1px solid var(--border);
    border-radius: 12px;
    color: #fff;
  }
  code{ padding: 2px 7px; }
  pre{
    padding: 14px;
    overflow: auto;
    box-shadow: inset 0 0 0 1px rgba(255,255,255,0.04);
  }

  table{
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    overflow: hidden;
    border-radius: 14px;
    border: 1px solid var(--border);
    margin-top: 12px;
  }
  th, td{
    padding: 12px;
    text-align: center;
    border-bottom: 1px solid var(--border);
    border-right: 1px solid var(--border);
  }
  tr:last-child td{ border-bottom: none; }
  th:last-child, td:last-child{ border-right: none; }

  th{
    background: rgba(255,255,255,0.06);
    color: #fff;
    font-weight: 600;
  }
  td{
    background: rgba(255,255,255,0.03);
    font-variant-numeric: tabular-nums;
  }
</style>

</head>
<body>
  <div class="wrap">
  <h1>Quantified Dilemma — Participant Rules</h1>
  <p class="muted">
    Theme: <b>Collateral &amp; Liquidity Under Stress</b> — repeated counterparty interactions where
    short-term advantage competes with long-term trust and resilience.
  </p>

  <div class="card">
    <h2>1) Objective</h2>
    <p>
      You will submit a bot (your strategy) that chooses one of three actions each round against an opponent bot.
      The tournament runs a <b>round-robin</b>: your bot plays every other bot.
      Your total score is the sum of points earned across all matchups and rounds.
    </p>
  </div>

  <div class="card">
    <h2>2) Actions (3x3)</h2>
    <p>Each round you must output exactly one action:</p>
    <ul>
      <li><b>PROVIDE (0)</b>: Extend support / meet calls smoothly / keep terms constructive.</li>
      <li><b>CONSERVE (1)</b>: Tighten moderately / protect your own book.</li>
      <li><b>WITHDRAW (2)</b>: Pull lines / hoard liquidity / demand hard terms.</li>
    </ul>
    <div class="callout"><b>Important:</b> Choosing <b>WITHDRAW</b> carries a fixed <b>friction cost</b> of <b>−1 point</b> each time you play it.</div>
    <p class="small muted">Actions are encoded as integers 0, 1, 2 (matching the enum).</p>
  </div>

  <div class="card">
    <h2>3) Payoffs (WITHDRAW friction applied)</h2>
    <p>Each cell shows <code>(your_points, opponent_points)</code>.</p>

    <table>
      <tr>
        <th rowspan="2">You \ Opponent</th>
        <th colspan="3">Opponent Action</th>
      </tr>
      <tr>
        <th>PROVIDE</th>
        <th>CONSERVE</th>
        <th>WITHDRAW</th>
      </tr>

      <tr>
        <th>PROVIDE</th>
        <td>(3, 3)</td>
        <td>(2, 4)</td>
        <td>(0, 4)</td>
      </tr>
      <tr>
        <th>CONSERVE</th>
        <td>(4, 2)</td>
        <td>(2, 2)</td>
        <td>(1, 2)</td>
      </tr>
      <tr>
        <th>WITHDRAW</th>
        <td>(4, 0)</td>
        <td>(2, 1)</td>
        <td>(0, 0)</td>
      </tr>
    </table>
  </div>

  <div class="card">
    <h2>4) Match Format</h2>
    <ul>
      <li><b>Penta round-robin:</b> The tournament runs <b>5</b> independent round-robins and your final score is the <b>average</b> across the 5 runs.</li>
      <li>Against each opponent, your bot plays a <b>fixed number of rounds</b>. This number is <b>not disclosed</b>.</li>
      <li>Both bots receive the full history of play <i>from their own perspective</i>.</li>
      <li>History format: <code>[ (my_prev, opp_prev), ... ]</code>.</li>
      <li>If your bot errors or returns an invalid action, the simulator will default it to <b>CONSERVE</b> for that move.</li>
    </ul>
  </div>

  <div class="card">
    <h2>5) How to Submit</h2>
    <ol>
      <li>Create a file named <code>strategies/&lt;team_name&gt;.py</code> for your submission.</li>
      <li>Start from <code>template.py</code> and modify only your strategy logic.</li>
      <li>Your file must define:
        <ul>
          <li><code>class Action(IntEnum)</code> with <code>PROVIDE=0</code>, <code>CONSERVE=1</code>, <code>WITHDRAW=2</code></li>
          <li><code>class Strategy</code> with <code>__init__(my_id)</code> and <code>select_action(round_number, opponent_id, history)</code></li>
        </ul>
      </li>
    </ol>
  </div>

  <div class="card">
    <h2>6) Fair Play Constraints</h2>
    <ul>
      <li>No network calls.</li>
      <li>Do not read/write external files outside your strategy file.</li>
      <li>Keep runtime lightweight (avoid heavy computation inside <code>select_action</code>).</li>
      <li>AI/ML libraries like <code>scikit-learn</code> or <code>tensorflow</code> are NOT allowed.</li>
    </ul>
  </div>

  <div class="card">
  <h2>7) Running Locally </h2>

  <h3 style="margin:12px 0 6px; font-size:15px;">Using master.py</h3>
  <p class="small muted">
    The master.py supports a <code>--debug</code> flag to print round-by-round actions, exceptions, and any forced moves.
    It imports settings from <code>config.py</code> (keep it in the same folder as <code>master.py</code>). Set the TOTAL_ROUNDS variable in <code>config.py</code> for local testing.
  </p>
  <pre><code>python3 master.py</code></pre>
  <pre><code>python3 master.py --debug</code></pre>
</div>

</div>
</body>
</html>
