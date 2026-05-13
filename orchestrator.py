import anthropic
import json

client = anthropic.Anthropic()  # set ANTHROPIC_API_KEY in env

# ── 1. Your user story (later: fetch from Jira via MCP) ──────────────────
story = {
    "id": "STORY-1042",
    "title": "Password reset via email",
    "description": "As a user I want to reset my password via email",
    "acceptance_criteria": [
        "Email sent within 30 seconds",
        "Reset link expires after 1 hour",
        "Link is single-use only",
        "Invalid email shows inline error"
    ]
}

# ── 2. Your coding standards (later: fetched from RAG vector DB) ─────────
standards = """
Framework: Playwright + TypeScript
Style: page object model, kebab-case test IDs
Naming: TC-{id}: {description} 
Always test: happy path, boundary, negative
"""

# ── 3. Generate test cases ────────────────────────────────────────────────
def generate_test_cases(story, standards):
    prompt = f"""
You are a QA engineer. Given this user story and coding standards,
generate a complete test suite as JSON.

Story: {json.dumps(story, indent=2)}
Standards: {standards}

Return ONLY a JSON array of test cases, each with:
- id (string): TC-001 format
- title (string): what is being tested  
- type (string): happy_path | edge_case | negative
- steps (array): action steps
- expected (string): expected result
"""
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}]
    )
    raw = response.content[0].text
    clean = raw.replace("```json","").replace("```","").strip()
    return json.loads(clean)

# ── 4. Generate Playwright spec ───────────────────────────────────────────
def generate_playwright_spec(test_cases, story):
    tc_json = json.dumps(test_cases, indent=2)
    prompt = f"""
Write a complete Playwright TypeScript spec file for these test cases.
Story: {story['title']} ({story['id']})
Test cases: {tc_json}

Use: test(), expect(), getByRole(), getByLabel()
Export nothing — just the spec file content.
"""
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=3000,
        messages=[{"role": "user", "content": prompt}]
    )
    code = response.content[0].text
    return code.replace("```typescript","").replace("```","").strip()

# ── 5. Run the pipeline ───────────────────────────────────────────────────
print(f"Processing {story['id']}...")

test_cases = generate_test_cases(story, standards)
print(f"Generated {len(test_cases)} test cases")

spec = generate_playwright_spec(test_cases, story)

with open(f"{story['id'].lower()}.spec.ts", "w") as f:
    f.write(spec)

print(f"Saved: {story['id'].lower()}.spec.ts")
print("Next: add Jira MCP + GitHub MCP to automate filing")