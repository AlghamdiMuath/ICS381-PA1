# ICS381-PA1 — Simple Reflex Agents

Programming assignment 1 for **ICS 381 – Introduction to Artificial Intelligence** at KFUPM (Term 222). Implements two simple reflex agents and the discrete-time environments they operate in.

> Auto-grader score: **100%**.

## What's inside

- `ac_simulation.py` / `ac_simulation.ipynb` — a thermostat-style AC controller. `SimpleACReflexAgent` decides `TurnOn` / `TurnOff` based on current temperature and AC state; `SimpleACEnvironment` simulates ambient temperature drift over time.
- `server_simulation.py` / `server_simulation.ipynb` — a load-shedding agent for a server cluster. Decides whether to power servers up/down based on incoming request load.
- `ai_env.yml` — conda environment used in the course.

## Run

```bash
conda env create -f ai_env.yml
conda activate ai_env
python ac_simulation.py
python server_simulation.py
```

Or open the matching `.ipynb` files in Jupyter.

---

*Archived: course artifact, kept for reference.*
