# Cold-Start Exercise: Before We Begin
**Placement:** Day 1, Segment 2 — after icebreaker, before AI Foundations  
**Duration:** ~30 min total (15 min task · 5 min observe · 10 min debrief)  
**Tool:** ChatGPT or Microsoft Copilot — open a new chat and go

---

## Setup

No preparation needed. No right answers. No evaluation.

This is a *discovery exercise* — you're going to use an AI tool to do something real, then notice what happens. That's it.

**Before you start, one question to hold in your head:**  
*What did you expect the AI to do, versus what actually happened?*

Open ChatGPT or Copilot. Start a new chat. You're ready.

---

## Part 1 — The Task (15 min)

### Scenario

Your team has just wrapped up a two-day internal workshop on improving client onboarding. A senior stakeholder who didn't attend has asked for a short briefing note — what was discussed, what the key decisions were, and what happens next.

You have rough notes but no time to write it up properly. You're going to ask the AI to help.

---

### Prompt 1 — Your starting prompt

Copy this into the chat exactly as written:

> **Write a briefing note about our onboarding workshop. Cover what was discussed, decisions made, and next steps.**

Read the output. Don't change anything yet.

---

### Prompt 1b — Now try it with your actual notes

Open the sample workshop notes: **[`day1-coldstart-workshop-notes.md`](day1-coldstart-workshop-notes.md)**

Copy the notes content, then send this prompt in the **same chat** (or start a fresh one — either works):

> **Here are my rough notes from the workshop:**
>
> [paste the workshop notes here]
>
> **Write a briefing note for a senior stakeholder who didn't attend. Cover what was discussed, key decisions, and next steps. Keep it under one page.**

Compare this output to Prompt 1. What changed? What's still imperfect?

---

### Prompt 2 — Follow-up

After you receive the output, send this follow-up in the same chat:

> **Are you confident this is accurate? What assumptions did you make?**

Read the response carefully.

---

### Prompt 3 — Optional push (if you finish early)

> **Rewrite the briefing note. This time, the audience is a senior partner who is skeptical that this workshop was worth the time. Adjust the tone and framing accordingly.**

---

## Part 2 — Observe & Note (5 min)

Answer these briefly in your own words — no need to share, just capture your thoughts:

1. **Prompt 1 vs. Prompt 1b — what changed when you added the notes?** (Specific differences in content, accuracy, or usefulness)

2. **What was still wrong or missing in the Prompt 1b output?** (Something in the notes that the AI got wrong, missed, or misrepresented)

3. **When you asked if it was confident — what did it say? Did that match how the output read?**

4. **What's one thing you'd do differently in your prompt next time?**

5. **One word that describes how you feel about what you just saw:** *(curious / skeptical / impressed / confused / something else)*

---

## Part 3 — Debrief (10 min, facilitated)

*Facilitator leads. See notes below.*

**Discussion questions for the group:**

1. **What did the AI produce?** Go around quickly — was it roughly similar for everyone, or quite different? Why might that be?

2. **What did the AI make up?** Did it invent workshop topics, names, dates, or decisions? How did it handle the fact that it had no real information?

3. **When you asked if it was confident — what happened?** Did the AI know what it didn't know?

4. **What would you need to do to actually send that briefing note?** What's the human's job in this workflow?

5. **What do you think is happening inside the model when it generates that text?**  
   *(This question sets up the AI Foundations session — let the group speculate freely, then say: "let's find out.")*

---

## Facilitator Notes

### What you're looking for

**In Part 1 outputs:**
- Almost everyone will get a plausible-sounding briefing note with invented content (fictional workshop topics, fake decisions, placeholder next steps)
- The structure will usually be good; the facts will be entirely made up
- Prompt 2 often reveals the model hedging gracefully ("I assumed...") — which can feel reassuring but doesn't undo the fabrication
- Prompt 3 (optional) typically produces a noticeably different tone — useful to highlight that the model is highly responsive to framing

**In Part 2 answers:**
- Most people note the output looks professional and is well-structured
- Most people are surprised by the confident fabrication
- The "one word" answers usually split between *impressed* and *skeptical* — both are valid starting points

### How to run the debrief

Keep it fast and conversational. Your goal is to surface 3–4 genuine observations from the room, not to lecture. Resist explaining too early — let participants articulate what they noticed before you add framing.

The pivot at question 5 is important: get the group speculating about what's happening inside the model ("it searches the internet?" "it looks things up?" "it guesses?"), then land with *"that's exactly what we're about to cover"* — and move into the AI Foundations deck.

### Common observations to amplify

| Observation | Why it matters (don't say this yet — just note it) |
|-------------|---------------------------------------------------|
| "It made everything up but it sounded real" | Introduces hallucination; leads to tokens/probability |
| "The structure was great but the content was wrong" | LLMs are form-generators, not fact-retrievers |
| "When I asked if it was confident, it got weird" | Model doesn't have reliable self-knowledge |
| "My output was different from my neighbour's" | Non-determinism / temperature |
| "Prompt 3 sounded completely different" | Framing and persona effects → leads to prompting session |

### Time guide

| Phase | Time |
|-------|------|
| Setup explanation | 2 min |
| Part 1 (task) | 15 min |
| Part 2 (observe) | 5 min |
| Part 3 (debrief) | 10 min |
| Transition to AI Foundations | 1 min |
| **Total** | **~33 min** |
