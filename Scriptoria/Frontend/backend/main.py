import os
from groq import Groq

from backend.prompts import (
    idea_analysis_prompt,
    greenlight_prompt,
    visual_dna_prompt,
    story_structure_prompt,
    scene_generation_prompt,
    dialogue_generation_prompt,
    visual_blueprint_prompt

)

# ===============================
# Groq Client
# ===============================

client = Groq(
    api_key=os.getenv("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")
)

# ===============================
# Idea Vault
# ===============================

def analyze_idea(idea):
    prompt = idea_analysis_prompt(idea)

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a professional film analyst."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=250
    )

    return completion.choices[0].message.content


# ===============================
# Greenlight AI
# ===============================

def greenlight_analysis(script, region, budget):
    prompt = greenlight_prompt(script, region, budget)

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are an experienced film producer and market analyst."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.6,
        max_tokens=350
    )

    return completion.choices[0].message.content


# ===============================
# ScriptForge
# ===============================

def generate_story_structure(idea, genre, tone):
    prompt = story_structure_prompt(idea, genre, tone)

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a professional screenwriter."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=300
    )

    return completion.choices[0].message.content


def generate_scenes(story_structure):
    prompt = scene_generation_prompt(story_structure)

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a screenplay writer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=350
    )

    return completion.choices[0].message.content


def generate_dialogue(scene):
    prompt = dialogue_generation_prompt(scene)

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You are a dialogue writer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.75,
        max_tokens=400
    )

    return completion.choices[0].message.content


# ===============================
# Visual DNA
# ===============================

def generate_visual_dna(script, genre, tone):
    prompt = visual_dna_prompt(script, genre, tone)

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are an award-winning film director and cinematographer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.8,
        max_tokens=350
    )

    return completion.choices[0].message.content

    from backend.prompts import visual_blueprint_prompt

def generate_visual_blueprints(script, genre, tone):
    prompt = visual_blueprint_prompt(script, genre, tone)

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are a professional film director and storyboard artist."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.85,
        max_tokens=500
    )

    return completion.choices[0].message.content




