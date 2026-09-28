# Prompting Lab — Day 1, Segment 6
**Placement:** Day 1, after Advanced Prompting slide deck  
**Duration:** ~60 min  
**Tools:** ChatGPT or Microsoft Copilot (enterprise) — open a new chat for each exercise  
**Format:** Individual or pairs

---

> **How to use this guide**  
> Each exercise has a scenario, a starter prompt to improve, and a follow-up step. Work through them in order. If you finish early, jump to the Stretch exercise. Model answers are provided after each exercise — try before you peek.

---

## Warm-Up Exercise (10 min)

### The Prompt Makeover

**What you're practising:** Structuring a prompt with context, task, constraints, and format.

**Scenario:** You need a short summary of a topic to share with a colleague who missed a meeting.

**Starter prompt (use this as-is first):**
```
Summarise artificial intelligence for me.
```

**Step 1:** Run the starter prompt. Note what you get — length, tone, level of detail.

**Step 2:** Now rewrite it using the four-component framework (context → task → constraints → format). Aim for an output that is:
- 3–4 sentences
- Written for someone with no technical background
- Suitable to paste into a chat message

**Step 3:** Compare the two outputs. What changed?

> **Example improved prompt:**
> ```
> I need to brief a non-technical colleague who missed our AI overview session.
> Write a 3–4 sentence summary of what Generative AI is and why it matters for
> business professionals. Avoid jargon. Use plain, conversational language.
> ```

> **Example output:**
> *Generative AI refers to a category of artificial intelligence that can create new content — text, images, code, and more — based on patterns it has learned from large amounts of data. Unlike traditional software that follows fixed rules, generative AI models can respond flexibly to open-ended requests, making them useful for tasks like drafting documents, answering questions, or summarising information. For business professionals, this means a new class of tool that can accelerate repetitive writing and research tasks — though it works best when given clear, specific instructions and when its outputs are reviewed before use.*

**Reflection:** What part of the prompt had the biggest impact on the output quality?

---

## Core Exercises (35 min)

---

### Exercise 1 — System Prompts & Personas (10 min)

**What you're practising:** System prompt design, role assignment, tone control.

**Scenario:** You need to draft a sensitive message to a client whose project has been delayed. You want the AI to act as a senior communications advisor — measured, empathetic, professional — not give you a generic apology template.

**Starter prompt:**
```
Write an email to a client about a project delay.
```

**Step 1:** Run the starter prompt and note the tone and structure of the output.

**Step 2:** Rewrite using a system prompt that assigns a persona and sets behavioural constraints. If your tool supports a system/instructions field (ChatGPT Custom Instructions or Copilot "Set context"), use it. If not, open your user message with a role assignment.

Your system prompt should specify:
- Who the model is (role + seniority + domain)
- The tone it should use
- What it should and should not include

Then write your user message (the actual task) separately.

**Step 3:** Ask a follow-up: *"Make it 20% shorter without losing the empathetic tone."*

> **Example system prompt:**
> ```
> You are a senior client communications advisor at a professional services firm.
> You write in a measured, empathetic tone — direct but never cold. You acknowledge
> problems honestly without dwelling on them, pivot quickly to constructive next steps,
> and avoid corporate filler phrases like "we apologise for any inconvenience."
> ```

> **Example user message:**
> ```
> Draft an email to our client Meridian Retail informing them that the Phase 2
> delivery will be delayed by three weeks due to scope changes agreed in the
> last steering committee. Propose a revised timeline call for next week.
> Keep it under 200 words.
> ```

> **Example output (excerpt):**
> *Subject: Phase 2 Timeline Update — Revised Delivery Date*
>
> *Hi [Name],*
>
> *I wanted to give you a heads-up on Phase 2 timing. As a result of the scope adjustments we agreed in last week's steering committee, we're revising the delivery date by three weeks, to [new date]. This gives the team the runway to incorporate the changes properly rather than rushing the integration.*
>
> *I'd like to schedule a 30-minute call next week to walk through the updated plan and confirm milestones. Would Tuesday or Wednesday work on your end?*

**Reflection:** How did the persona change the *character* of the output, not just the content?

---

### Exercise 2 — Structured Output (10 min)

**What you're practising:** Requesting specific output formats; using AI output in a downstream workflow.

**Scenario:** You're preparing a team retrospective. You have rough notes from a 45-minute meeting and need to turn them into a structured action log that can be pasted into a project tracker.

**Starter prompt:**
```
Here are my meeting notes. Give me the action items.

Notes: We talked about the onboarding process taking too long. Sarah said she'd look
into the new hire checklist. There's a compliance training that needs scheduling —
James owns that. The manager dashboard hasn't been updated since Q2, someone needs
to pick that up. We agreed to meet again in two weeks to review progress.
```

**Step 1:** Run the starter prompt. Note the format of the output.

**Step 2:** Rewrite to request a structured table with specific columns: Action | Owner | Due Date | Priority. Also add an instruction for how to handle missing information (e.g., "If the owner or due date is not stated, mark as TBC").

**Step 3 (optional):** Ask the model to output the same table as a JSON array — useful if you wanted to import it into a system programmatically.

> **Example improved prompt:**
> ```
> Here are notes from a team retrospective. Extract all action items and return them
> as a markdown table with four columns: Action | Owner | Due Date | Priority.
> If owner or due date is not stated in the notes, write TBC.
> Infer priority (High / Medium / Low) from the context and urgency implied.
>
> Notes: [paste notes]
> ```

> **Example output:**
>
> | Action | Owner | Due Date | Priority |
> |--------|-------|----------|----------|
> | Review and update the new hire onboarding checklist | Sarah | TBC | Medium |
> | Schedule compliance training for the team | James | TBC | High |
> | Update the manager dashboard (last updated Q2) | TBC | TBC | Medium |
> | Retrospective follow-up meeting | Team | +2 weeks | Low |

**Reflection:** What downstream task becomes easier when you control the output format upfront?

---

### Exercise 3 — Multi-Step Reasoning / Chain-of-Thought (15 min)

**What you're practising:** Asking the model to reason step-by-step before giving a conclusion; evaluating whether the reasoning is sound.

**Scenario:** You're evaluating whether to bring a specific process in-house or continue outsourcing it. You have some facts but no clear framework. You want the AI to help you think through it — not just give you a yes/no answer.

**Starter prompt:**
```
Should we outsource our data reporting or do it in-house?
```

**Step 1:** Run it. Note that the output is likely generic advice with no reasoning.

**Step 2:** Rewrite using a chain-of-thought instruction. Ask the model to:
1. First, identify the key factors that should drive this decision
2. Then, evaluate each factor given a specific context you provide
3. Finally, give a reasoned recommendation

Provide this context:
- The team has 3 analysts; all have moderate Excel/SQL skills but no data engineering background
- Current outsourced provider costs £80k/year; estimated in-house tooling + time cost is £55k/year
- Data reports are produced weekly; currently there's a 2-day lag from data to report
- Data is commercially sensitive and subject to GDPR

**Step 3:** After you get the output, ask: *"What's the strongest argument against your recommendation?"* Evaluate whether the model reasons honestly or just defends its first answer.

> **Example improved prompt:**
> ```
> I need to think through a build-vs-buy decision. Work through this step by step.
>
> Step 1: Identify the 4–5 key factors that should drive an in-house vs. outsourcing
> decision for a business process.
> Step 2: For each factor, evaluate our situation based on the context below.
> Step 3: Give a clear recommendation with a 2–3 sentence rationale.
>
> Context: [paste context above]
> ```

> **Example output (structure):**
> *Key factors: Cost, Capability, Data sensitivity, Speed/agility, Strategic value.*
>
> *Cost: In-house saves ~£25k/year on direct costs, but the estimate may not account for management overhead and tooling maintenance. Moderate advantage for in-house.*
>
> *Capability: Team has moderate skills; a step up to full in-house ownership would require upskilling or a new hire. Risk factor — in-house is viable but not low-effort.*
>
> *Data sensitivity: GDPR and commercial sensitivity are significant. Keeping data internal removes a third-party data-sharing risk. Clear advantage for in-house.*
>
> *Speed: Current 2-day lag is a known pain point. In-house ownership could reduce this, but only once the team is fully operational.*
>
> *Recommendation: Bring in-house, but phase the transition over 6 months. The data sensitivity argument alone justifies it; the cost saving makes it financially attractive. Success depends on investing in tooling and one round of upskilling.*

**Reflection:** Did the model's reasoning help you think more clearly — or did it just produce confident-sounding text? What would you verify before acting on it?

---

## Stretch Exercise (15 min)

### Bring Your Own Task

**What you're practising:** Applying the complete prompting framework to a real task from your own work.

**Instructions:**

Think of a task you do regularly that involves producing a document, analysis, summary, or communication. Use the framework below to design a prompt for it — then run it and evaluate the output.

**Your prompt design template:**

```
SYSTEM PROMPT (who the AI is, what constraints it operates under):
[Write here]

USER MESSAGE:

Context: [Who you are, what situation you're in, any relevant background]

Task: [What you specifically want produced]

Constraints:
- Length: [e.g., under 300 words / one page / 5 bullet points]
- Tone: [e.g., formal / conversational / technical]
- Audience: [e.g., C-suite / client / new hire]
- Format: [e.g., email / table / numbered list / prose]

Evaluation criteria — the output should:
1. [What "good" looks like for this task]
2. [Second criterion]
3. [Third criterion]
```

**After you run it:**
- Score the output against your own criteria (1–3 on each)
- Identify one thing to adjust and re-run
- Note whether the second attempt was better — and why

---

## Reflection (5 min)

Answer these for yourself before the group debrief:

1. Which technique from today had the biggest impact on output quality for you personally?
2. What's a task in your current role where you'd apply this in the next week?
3. What's one thing you still want to understand better about how prompting works?

---

## Facilitator Notes

### Timing
- Warm-up: 10 min — keep it moving, don't let groups over-discuss before trying
- Core Ex 1: 10 min — likely to spark good discussion about persona; leave 2 min for brief share-out
- Core Ex 2: 10 min — fast exercise; stretch goal (JSON output) keeps fast finishers busy
- Core Ex 3: 15 min — hardest exercise; some groups will need a nudge to add the explicit step-by-step instruction
- Stretch: 15 min — for anyone done early; can run during Ex 3 for fast finishers
- Reflection: 5 min solo, then 5 min group debrief

### Common mistakes to watch for
- Participants rewrite the prompt but forget to re-run it — remind them the test is the output, not the prompt text
- System prompts placed inside the user message (doesn't work the same way) — show them where the system/instructions field is in each tool
- Exercise 3: participants often just ask "give me a recommendation" rather than forcing step-by-step reasoning — coach them to be explicit: "reason through each factor before concluding"
- Stretch exercise: some participants choose tasks too vague ("write a report") — help them narrow to a specific document with a specific audience

### Debrief discussion questions
1. Which of your rewrites made the biggest difference? Why do you think that was?
2. Did anyone get a confidently wrong output? What does that tell us about how to use AI at work?
3. For Exercise 3 — when you asked for the counter-argument, did the model change its mind or defend itself? What does that imply about using AI for decisions?
4. From the stretch exercise: what made a task easy vs. hard to prompt for?

### Bridging to Day 2
Close by previewing: *"Tomorrow we move from crafting prompts to building systems — where AI isn't just answering your question but connected to data, workflows, and other tools."*
