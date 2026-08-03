# Round 1 interview prompt

Paste at the end of a target chat (or after a transcript export).

```text
ROLE
You are a transcript witness for Innovation OS memory capture.
You answer only from this chat transcript and pastes inside it.
You do not invent. You do not import outside knowledge. You do not write YAML.

ACTION
Answer every question in the Round 1 checklist below, in order.
Use only this conversation as evidence.
If something is not in the transcript, write exactly: NOT IN TRANSCRIPT

CONTEXT
- This is an inventory pass, not a final memory document.
- Prefer short, concrete answers.
- Quotes or tight paraphrases beat vague summary.
- For mappings, list rows; do not collapse into one sentence.
- For code, describe growth across the chat when code appears.

EXPECTATION
- Keep the question numbers.
- No preamble, no closing essay, no YAML.
- Output format: "1. ..." through "32. ..."
- For question 12: one mapping row per line as source → target → meaning
- For question 31: three labels only — strong | partial | missing

ROUND 1 CHECKLIST

A. Scope and identity
1. What is the main system, module, or project this chat is about? (names as used in the chat)
2. What other systems, layers, or codenames are mentioned? (list all)
3. In one sentence, what was the user trying to accomplish in this chat?
4. Did the chat end with something settled, still open, or mixed?

B. Decisions and rationale
5. What explicit choices were made? (who chose what)
6. What options were rejected or replaced? (old → new if stated)
7. What constraints or requirements did the user impose? (format, policy, process)
8. What constraints came from pasted system or audit text (not the user)?
9. Where does the transcript state why something must be that way? Quote or paraphrase and mark USER / ASSISTANT / PASTE
10. Where is why not stated and only implied?

C. Theological / scriptural / symbolic frames
11. Is there a Decalogue, biblical, theological, or similar mapping in the chat? YES or NO
12. If YES: list every mapping row as source → target → meaning (one line per row). If NO: NOT IN TRANSCRIPT
13. What other non-technical frames appear (OMEGA, Sabbath, humility gate, etc.)?
14. Does the transcript say why that frame is used or binding, or only that it is used?

D. Architecture and structure
15. What layers, phases, stacks, or pipelines are named?
16. What inputs/outputs, envelopes, or interfaces are described?
17. What failure modes, statuses, or error codes appear?
18. What external dependencies or missing modules are named?

E. Code presence and growth
19. Was any source code pasted or generated in this chat? YES / NO / PARTIAL
20. If code appeared: list distinct code moments in chronological order. If none: NOT IN TRANSCRIPT
21. For each moment: what changed versus the previous moment?
22. For each change: was a rationale given? State it, or UNKNOWN
23. Best final code state in the transcript: FULL / PARTIAL / NONE; filename hint if any; what is still missing
24. Most important changed code segment (short excerpt or description). If none: NONE

F. Evidence anchors
25. List 5–15 hard anchors (class names, functions, log lines, commandment lines, requirement numbers)
26. Flag any anchor that looks important but appears only once with no explanation

G. Open loops
27. What questions remain unanswered in the chat?
28. What did participants say they would do next but did not complete here?

H. Participants
29. Summarize user moves: framed / constrained / chose / questioned / coded
30. Summarize assistant moves: proposed / chose / repaired / refused / explained

I. Honesty check
31. Rate using only this transcript — repair rationale, architecture founding rationale, ontology/frame rationale (each: strong | partial | missing)
32. In one sentence: what must Round 2 still get before this is safe to store as long-term memory?
```

After answers, merge into an Episode under `memory/episodes/` and promote durable choices to `memory/decisions/`.
