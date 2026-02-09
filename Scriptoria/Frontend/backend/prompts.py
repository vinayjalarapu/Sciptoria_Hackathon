def idea_analysis_prompt(idea):
    return f"""
Analyze the following film idea and provide:
- Genre
- Mood
- Target audience
- One improvement suggestion

Film Idea:
{idea}
"""

def greenlight_prompt(script, region, budget):
    return f"""
You are a senior film producer.

Analyze the following project and give a GREENLIGHT decision.

SCRIPT / STORY:
{script}

TARGET MARKET: {region}
BUDGET RANGE: {budget}

Provide:
1. Market Potential (High/Medium/Low)
2. Target Audience
3. Revenue Channels (OTT/Theatre)
4. Risk Factors
5. Success Probability (0–100%)
6. Final Greenlight Recommendation (YES/NO)

Keep it concise and professional.
"""

# ===============================
# ScriptForge Prompts
# ===============================

def story_structure_prompt(idea, genre, tone):
    return f"""
You are a professional screenwriter.

Create a clear story structure for the following film idea.

IDEA:
{idea}

GENRE: {genre}
TONE: {tone}

Output:
- Logline
- Act 1 Setup
- Act 2 Conflict
- Act 3 Resolution

Keep it cinematic and structured.
"""


def scene_generation_prompt(story_structure):
    return f"""
You are a screenplay writer.

Expand the following story structure into scene-wise breakdown.

STORY STRUCTURE:
{story_structure}

Output format:
Scene 1:
Scene 2:
Scene 3:
(Each scene should include setting and purpose)

Keep it concise.
"""


def dialogue_generation_prompt(scene):
    return f"""
You are a dialogue writer.

Write a screenplay-style scene with dialogues.

SCENE:
{scene}

Use proper screenplay format:
INT./EXT. – LOCATION – DAY/NIGHT
Character names in CAPS
Natural, cinematic dialogues
"""

# ===============================
# Visual DNA Prompts
# ===============================

def visual_dna_prompt(script, genre, tone):
    return f"""
You are a visionary film director and cinematographer.

Analyze the following script and define its VISUAL DNA.

SCRIPT / STORY:
{script}

GENRE: {genre}
TONE: {tone}

Provide:
1. Overall Visual Mood
2. Color Palette (with emotions)
3. Camera Style (handheld, static, tracking, etc.)
4. Lighting Style
5. Production Design Notes
6. Visual References (film names only)

Keep it artistic, cinematic, and practical.
"""

# ===============================
# Visual Blueprint Prompt
# ===============================

def visual_blueprint_prompt(script, genre, tone):
    return f"""
You are a film director creating PRE-PRODUCTION VISUAL BLUEPRINTS.

SCRIPT:
{script}

GENRE: {genre}
TONE: {tone}

Generate:

1. SCENE COMPOSITION BLUEPRINTS
- Describe framing (wide/medium/close)
- Subject placement
- Foreground / background

2. CAMERA BLOCKING
- Camera movement (static, pan, dolly, handheld)
- Actor movement
- Emotional intent

3. MOOD BOARD IMAGE PROMPTS
- Write 5 detailed image prompts
- Cinematic, photorealistic
- No character names
- Ready for AI image generation tools

4. PRODUCTION DESIGN NOTES
- Locations
- Props
- Textures
- Architectural style

Output clearly with headings.
"""

