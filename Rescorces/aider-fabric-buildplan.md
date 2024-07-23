# Aider Fabric Build Plan

## Introduction

This document outlines the detailed plan for integrating Fabric into our project. Fabric is an open-source framework for augmenting humans using AI. It provides a modular framework for solving specific problems using a crowdsourced set of AI prompts that can be used anywhere.

## Goals

1. Extract transcripts and metadata from YouTube videos.
2. Save the extracted data in organized folders.
3. Use the extracted data to create specific Crew AI agents.
4. Integrate Fabric to enhance the efficiency and effectiveness of these tasks.
5. Build a full-stack web application using Python based on the extracted data.

## Steps

### 1. Understanding Fabric

Before we proceed, it's crucial to understand the Fabric framework. Fabric is designed to help integrate AI into everyday tasks by breaking problems into individual components and applying AI to them one at a time. It uses a modular approach with components like Patterns, Stitches, Mills, and Looms.

### 2. Setting Up Fabric

#### Prerequisites

- Ensure you have at least Python 3.10 installed.
- Install pipx:
  ```bash
  brew install pipx  # macOS
  sudo apt install pipx  # Linux
  ```

#### Installation

- The Fabric server is already installed globally.

### 3. Using Fabric Patterns

Fabric Patterns are pre-defined AI prompts that can be used to perform specific tasks. We will use the following Patterns:

- `extract_wisdom`: Extracts key insights from YouTube transcripts.
- `summarize`: Summarizes long content.
- `analyze_claims`: Analyzes claims made in the content.
- `create_coding_project`: Helps in creating coding projects.
- `explain_code`: Explains code snippets.

#### Example Commands

1. Extract wisdom from a YouTube video:
   ```bash
   yt --transcript https://youtube.com/watch?v=ITOZkzjtjUA > transcript.txt
   cat transcript.txt | fabric --pattern extract_wisdom
   ```

2. Summarize content:
   ```bash
   echo "Long content here" | fabric --pattern summarize
   ```

3. Analyze claims:
   ```bash
   echo "Claim to analyze" | fabric --pattern analyze_claims
   ```

4. Create a coding project:
   ```bash
   echo "Create a full-stack web application using Python" | fabric --pattern create_coding_project
   ```

5. Explain code:
   ```bash
   echo "Code snippet here" | fabric --pattern explain_code
   ```

### 4. Creating Custom Patterns

We can create custom Patterns to suit our specific needs. These Patterns can be stored locally and used with Fabric.

#### Example Custom Pattern

Create a custom Pattern to extract metadata from YouTube videos and save it to a file.

1. Create a new file `extract_metadata.md` in the `~/.config/custom-fabric-patterns` directory:
   ```markdown
   # System
   Extract metadata from the following YouTube video URL: {{url}}

   # User
   Please provide the metadata in JSON format.
   ```

2. Copy the custom Pattern to the Fabric patterns directory:
   ```bash
   cp ~/.config/custom-fabric-patterns/extract_metadata.md ~/.config/fabric/patterns/
   ```

3. Use the custom Pattern:
   ```bash
   echo "https://youtube.com/watch?v=ITOZkzjtjUA" | fabric --pattern extract_metadata
   ```

### 5. Integrating Fabric with Our Project

#### Updating `main.py`

1. Import the necessary Fabric functions.
2. Use Fabric Patterns to extract and process data.
3. Save the processed data in the desired format.

#### Example Integration

```python
import os
from youtube_extractor import extract_youtube_data
from fabric import run_pattern

def main():
    env_vars = load_environment_variables()
    youtube_url = "https://www.youtube.com/watch?v=ITOZkzjtjUA"
    
    # Extract YouTube data
    extract_youtube_data(youtube_url, env_vars["output_dir"])
    
    # Use Fabric to extract wisdom
    wisdom = run_pattern("extract_wisdom", youtube_url)
    print("Extracted Wisdom:", wisdom)
    
    # Save wisdom to a file
    with open(os.path.join(env_vars["output_dir"], "wisdom.txt"), "w") as f:
        f.write(wisdom)
    
    # Use Fabric to create a coding project
    project = run_pattern("create_coding_project", "Create a full-stack web application using Python")
    print("Created Project:", project)
    
    # Save project details to a file
    with open(os.path.join(env_vars["output_dir"], "project.txt"), "w") as f:
        f.write(project)

if __name__ == "__main__":
    main()
```

### 6. Creating Crew AI Agents

Using the extracted data, we can create specific Crew AI agents to perform various tasks. These agents can be defined using the Fabric framework and integrated into our project.

#### Example Crew AI Agent

```python
from crewai import Agent, Task, Crew, Process

class WisdomExtractorAgent(Agent):
    def _run(self, youtube_url):
        wisdom = run_pattern("extract_wisdom", youtube_url)
        return wisdom

class ProjectCreatorAgent(Agent):
    def _run(self, description):
        project = run_pattern("create_coding_project", description)
        return project

def main():
    youtube_url = "https://www.youtube.com/watch?v=ITOZkzjtjUA"
    wisdom_extractor = WisdomExtractorAgent(role="Wisdom Extractor", goal="Extract wisdom from YouTube videos.")
    project_creator = ProjectCreatorAgent(role="Project Creator", goal="Create a full-stack web application using Python.")
    
    tasks = [
        Task(description="Extract Wisdom", agent=wisdom_extractor, args=[youtube_url]),
        Task(description="Create Project", agent=project_creator, args=["Create a full-stack web application using Python"])
    ]
    
    crew = Crew(agents=[wisdom_extractor, project_creator], tasks=tasks, process=Process.sequential)
    crew.kickoff()

if __name__ == "__main__":
    main()
```

## Conclusion

This build plan provides a detailed roadmap for integrating Fabric into our project. By following these steps, we can enhance our workflow and achieve our goals more efficiently. If you have any questions or need further assistance, feel free to ask.
