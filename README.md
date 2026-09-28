# Generative AI Professional Training Program

3-day intensive virtual training on Generative AI · ~6.5 hrs/day · Single-track, layered for mixed audiences (by role, technical background, and prior AI knowledge).

**Open [`index.html`](index.html) in a browser for the full interactive agenda.**

---

## Program Overview

| | Day 1 | Day 2 | Day 3 |
|---|---|---|---|
| **Theme** | Understanding AI & Mastering Prompts | Building with AI | Real-World AI: Ethics, Strategy & Capstone |
| **Duration** | ~6.5 hrs | ~6.5 hrs | ~6.5 hrs |
| **Focus** | Foundations, model landscape, prompting | APIs, automation (n8n), RAG, agents | Safety/ethics, role use cases, strategy |

---

## Day 1 — Understanding AI & Mastering Prompts

| # | Session | Duration | Type | Link |
|---|---------|----------|------|------|
| 1 | Welcome & Icebreaker | 15 min | 🃏 Review Cards | [warm-up-flip-card.html](day1/warm-up-flip-card.html) |
| 2 | Cold-Start Exercise | 30 min | 📄 Handout | [day1-coldstart-exercise.md](day1/day1-coldstart-exercise.md) |
| 3 | AI Foundations | 60 min | 🎯 Slide Deck | [genai-basics.html](day1/genai-basics.html) |
| 4 | The AI Model Landscape | 30 min | 🎯 Slide Deck | [model-landscape.html](day1/model-landscape.html) |
| 5 | Prompting Basics | 60 min | 🎯 Slide Deck | [prompting_basics.html](day1/prompting_basics.html) |
| 6 | Advanced Prompting | 75 min | 🎯 Slide Deck | [advanced-prompting.html](day1/advanced-prompting.html) |
| 7 | Prompting Lab | 60 min | 📄 Handout | [day1-prompting-lab.md](day1/day1-prompting-lab.md) |
| 8 | Python & API Refresher | 75 min | 📓 Notebook | [day1-python-refresher.ipynb](day1/day1-python-refresher.ipynb) |
| — | Day 1 Review Cards | — | 🃏 Review Cards | [review-day1.html](day1/review-day1.html) |

**Cold-start supporting material:** [day1-coldstart-workshop-notes.md](day1/day1-coldstart-workshop-notes.md)

---

## Day 2 — Building with AI

| # | Session | Duration | Type | Link |
|---|---------|----------|------|------|
| 1 | Day 1 Recap & Warm-up | 20 min | 🃏 Review Cards | [review-flip-cards-1.html](day2/review-flip-cards-1.html) |
| 2 | AI APIs Hands-on | 60 min | 💻 Code Lab | [src/hello_openai_1.0.py](src/hello_openai_1.0.py) |
| 3 | n8n Automation Lab | 90 min | 💻 Code Lab | [n8n/n8n_lab_guide.html](n8n/n8n_lab_guide.html) |
| 4 | RAG: Concept & Build | 75 min | 💻 Code Lab | [src/RAG/](src/RAG/) |
| 5 | Agentic AI | 60 min | 💻 Code Lab | [src/crew-agents.py](src/crew-agents.py) |
| 6 | Multi-Agent Systems | 45 min | 💻 Code Lab | [src/crew-agents.py](src/crew-agents.py) |
| — | Day 2 Review Cards | — | 🃏 Review Cards | [review-day2.html](day2/review-day2.html) |

---

## Day 3 — Real-World AI: Ethics, Strategy & Capstone

| # | Session | Duration | Type | Link |
|---|---------|----------|------|------|
| 1 | Day 2 Recap & Warm-up | 20 min | 🃏 Review Cards | [review-day2.html](day2/review-day2.html) |
| 2 | AI Safety, Ethics & Governance | 90 min | 🎯 Slide Deck | [safety-ethics-governance.html](day3/safety-ethics-governance.html) |
| 3 | AI Use Cases by Role | 60 min | 🎯 Slide Deck | [role-specific-use-cases.html](day3/role-specific-use-cases.html) |
| 4 | AI Strategy & What's Next | 90 min | 🎯 Slide Deck | [strategy-and-whats-next.html](day3/strategy-and-whats-next.html) |
| 5 | Final Review & Capstone | 60 min | 🃏 Review Cards | [final_day_review_flipcards.html](day3/final_day_review_flipcards.html) |
| — | Day 3 Review Cards | — | 🃏 Review Cards | [review-day3.html](day3/review-day3.html) |

---

## Reference Materials

| Resource | Description | Link |
|----------|-------------|------|
| Glossary Flash Cards | Key GenAI terms and definitions | [glossary-flash-cards.html](reference/glossary-flash-cards.html) |
| n8n Companion Guide | Reference guide for the automation lab | [n8n/n8n-companion-guide.html](n8n/n8n-companion-guide.html) |
| Daily AI News Brief | Sample n8n workflow (JSON) | [n8n/Daily AI News Brief.json](n8n/Daily%20AI%20News%20Brief.json) |
| RAG Build Scripts | Index builder and query scripts | [src/RAG/](src/RAG/) |
| Python Warm-up | Pre-work / optional coding primer | [src/py-warm-up/](src/py-warm-up/) |

---

## Content Legend

| Icon | Type | Description |
|------|------|-------------|
| 🎯 | Slide Deck | Fullscreen HTML presentation — open in browser, navigate with arrow keys or click |
| 🃏 | Review Cards | Flip-card knowledge check — click to flip, filter by topic/type/difficulty |
| 📓 | Notebook | Jupyter notebook — open with `jupyter notebook` or Google Colab |
| 💻 | Code Lab | Python script or folder — run locally or in the provided virtual environment |
| 📄 | Handout | Markdown document — participant worksheet or facilitator guide |

---

## File Structure

```
genaiprof/
├── index.html                        # Interactive agenda (open in browser)
├── README.md                         # This file
│
├── day1/
│   ├── warm-up-flip-card.html        # Icebreaker
│   ├── genai-basics.html             # AI Foundations slide deck
│   ├── model-landscape.html          # Model Landscape slide deck
│   ├── prompting_basics.html         # Prompting Basics slide deck
│   ├── advanced-prompting.html       # Advanced Prompting slide deck
│   ├── review-day1.html              # Day 1 review cards (30 cards)
│   ├── day1-python-refresher.ipynb   # Python & API refresher notebook
│   ├── day1-coldstart-exercise.md    # Cold-start participant handout
│   ├── day1-coldstart-workshop-notes.md  # Sample workshop notes (linked from cold-start)
│   └── day1-prompting-lab.md         # Prompting lab participant handout
│
├── day2/
│   ├── review-flip-cards-1.html      # Day 2 opener recap cards
│   └── review-day2.html              # Day 2 review cards (30 cards)
│
├── day3/
│   ├── safety-ethics-governance.html # Safety, Ethics & Governance slide deck
│   ├── role-specific-use-cases.html  # AI Use Cases by Role slide deck
│   ├── strategy-and-whats-next.html  # AI Strategy slide deck
│   ├── final_day_review_flipcards.html  # Capstone review cards
│   └── review-day3.html              # Day 3 review cards (30 cards)
│
├── reference/
│   └── glossary-flash-cards.html     # GenAI glossary
│
├── n8n/                              # n8n automation lab materials
├── src/                              # Python source files (RAG, agents, API)
└── drafts/                           # Original .md content sources
```

---

## Setup

**To run slide decks and flip-cards:** Open any `.html` file directly in a browser. No server required — all assets load from CDN.

**To run the Python notebook:**
```bash
cd genaiprof
source venv/bin/activate   # or: python -m venv venv && pip install -r requirements.txt
jupyter notebook day1/day1-python-refresher.ipynb
```

**To run RAG / agent demos:**
```bash
source venv/bin/activate
python src/RAG/01_build_index.py
python src/RAG/02_query_rag.py
```

**API key required** for OpenAI-dependent exercises. Set `OPENAI_API_KEY` in your environment or a `.env` file before running code labs.

---

*Content generated for internal training use.*
