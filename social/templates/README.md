# Social audit templates

Use with the `social-audit` subagent (`.claude/agents/social-audit.md`) to repeat the Elena's Clean workflow for another business.

## Start a new business
1. Create `social/<business-slug>/` and copy the three templates below into it.
2. Invoke the agent with the intake form below.
3. Review the "Data still needed" list, gather screenshots/Insights from the owner, and re-run to fill the unverified rows.

## Intake form (paste into the agent prompt)
```
Business: <display name> (legal: <legal name>)
Niche / main services: <...>
Website: <url>
Service area: <cities>
Instagram: <@handle>   TikTok: <@handle>   Facebook: <url or "unknown">
Output folder: social/<business-slug>/
Branch: <branch name>     PR allowed: no
Posting plan target: <e.g. 3-4/week>   Owner time budget: <hours/week>
Known findings to verify, not re-derive: <...>
Owner-provided data: <screenshots, Insights, reviews>
```

## Files
- `brand-audit.template.md`
- `competitor-audit.template.md`
- `content-plan.template.md`

## What works and what does not (learned on Elena's Clean, 2026-10)
- TikTok profile and single-video pages are readable logged-out (`social/tools/tiktok_probe.py`).
- Instagram and Facebook are login-walled; use search-engine descriptions for counts (label as cached snippets) and owner screenshots for everything else.
- Many business websites may not be on the egress allowlist; ask for them to be added or paste the content.
- Handle guessing on TikTok often hits unrelated accounts; verify bio/location before attributing.
