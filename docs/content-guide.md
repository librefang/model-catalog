# Content Guide

Guidelines for contributing content to the LibreFang Registry.

## Naming Conventions

- Use **lowercase, hyphenated** names: `my-agent`, `web-scraper`, `code-reviewer`.
- Agent/hand/skill directory names must match their `name`/`id` field in the TOML.
- Provider and integration filenames must match their `id` field.

## Writing Descriptions

- Keep descriptions to **1-2 sentences**. Lead with a verb.
- Good: "Analyzes pull requests and suggests improvements."
- Bad: "This is an agent that can be used to analyze pull requests."

## System Prompts (Agents & Hands)

- Start with a clear role statement: "You are X, responsible for Y."
- Include specific instructions on behavior, not vague aspirations.
- Define what the agent should **not** do (scope boundaries).
- List tools it should use and when.
- Aim for **100-500 words** for agents, up to 1000 for complex hands.
- Avoid repeating information already in the TOML metadata.

## Agent vs Hand vs Skill

| Type | Use When |
|------|----------|
| **Agent** | Conversational, general-purpose, stateless Q&A or analysis. |
| **Hand** | Multi-step workflow requiring tools (shell, files, APIs). Has settings, dashboard, requirements. |
| **Skill** | Single focused task with defined inputs/outputs. Prompt-only or a short script. |

- If it needs `shell_exec` or external tools, it is probably a **hand**.
- If it is a reusable prompt template with parameters, it is a **skill**.
- If it is a conversational assistant for a domain, it is an **agent**.

## Provider Entries

- Include all models the provider offers that support chat completions.
- Use accurate `input_cost_per_m` / `output_cost_per_m` (USD per million tokens).
- Set `tier` honestly: `frontier` is reserved for the most capable models.
- Always include `context_window` and `max_output_tokens` from official docs.

## General Tips

- Run `make validate` before submitting.
- Run `make fmt` if you have taplo installed to keep TOML formatting consistent.
- Check `schema.toml` for the full field reference.
- Test scaffold output: `make new-agent NAME=test-agent`, verify, then delete.
