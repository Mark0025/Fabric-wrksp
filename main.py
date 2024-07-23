#!/usr/bin/env python3

import os
import subprocess
import logging
import sys
import time

def get_youtube_url_from_user():
    """Prompt the user to provide a YouTube URL."""
    try:
        youtube_url = input("Please provide a YouTube URL: ")
        return youtube_url
    except Exception as e:
        logging.error("Error getting YouTube URL: %s", e)
        print("Error: Unable to get YouTube URL")
        return None

def load_environment_variables():
    """Load environment variables."""
    try:
        return {
            "output_dir": os.path.expanduser("~/output")
        }
    except Exception as e:
        logging.error("Error loading environment variables: %s", e)
        print("Error: Unable to load environment variables")
        return {}

def extract_youtube_data(youtube_url, output_dir):
    """Extract YouTube data and save the transcript."""
    try:
        logging.debug("Extracting YouTube data from URL: %s", youtube_url)
        transcript_command = f"yt --transcript {youtube_url}"
        logging.debug("Running command: %s", transcript_command)
        transcript = subprocess.check_output(transcript_command, shell=True).decode('utf-8')
        transcript_path = os.path.join(output_dir, "transcript.txt")
        with open(transcript_path, "w") as f:
            logging.debug("Writing transcript to %s", transcript_path)
            f.write(transcript)
    except subprocess.CalledProcessError as e:
        logging.error("Failed to extract YouTube data: %s", e.output.decode('utf-8'))
        print("Error: Unable to extract YouTube data")
    except Exception as e:
        logging.error("Error extracting YouTube data: %s", e)
        print("Error: Unable to extract YouTube data")

def run_fabric_pattern(pattern, input_data):
    """Run a Fabric pattern with the given input data."""
    try:
        logging.debug("Running Fabric pattern: %s with input data: %s...", pattern, input_data[:100])
        command = f'echo "{input_data}" | fabric --pattern {pattern}'
        logging.debug("Running command: %s", command)
        result = subprocess.check_output(command, shell=True).decode('utf-8')
        return result
    except subprocess.CalledProcessError as e:
        logging.error("Failed to run Fabric pattern: %s", e.output.decode('utf-8'))
        print("Error: Unable to run Fabric pattern")
        return ""
    except Exception as e:
        logging.error("Error running Fabric pattern: %s", e)
        print("Error: Unable to run Fabric pattern")
        return ""

def main():
    """Main function to orchestrate the script execution."""
    start_time = time.time()
    try:
        env_vars = load_environment_variables()
        youtube_url = "https://www.youtube.com/watch?v=ITOZkzjtjUA"
        
        # Ensure the output directory exists
        os.makedirs(env_vars["output_dir"], exist_ok=True)
        logging.debug("Ensured output directory exists: %s", env_vars["output_dir"])
        
        # Extract YouTube data
        extract_youtube_data(youtube_url, env_vars["output_dir"])
        
        # Read the extracted transcript
        transcript_path = os.path.join(env_vars["output_dir"], "transcript.txt")
        with open(transcript_path, "r") as f:
            transcript = f.read()
        
        # Split the transcript into smaller chunks
        chunk_size = 1000  # Adjust the chunk size as needed
        logging.debug("Splitting transcript into chunks of size %d", chunk_size)
        transcript_chunks = [transcript[i:i + chunk_size] for i in range(0, len(transcript), chunk_size)]
        
        wisdom = ""
        for chunk in transcript_chunks:
            logging.debug("Processing chunk: %s...", chunk[:100])
            chunk_wisdom = run_fabric_pattern("extract_wisdom", chunk)
            wisdom += chunk_wisdom + "\n"
        
        print("Extracted Wisdom:", wisdom)
        
        # Save wisdom to a file
        wisdom_path = os.path.join(env_vars["output_dir"], "wisdom.txt")
        with open(wisdom_path, "w") as f:
            f.write(wisdom)
        
        # Use Fabric to create a coding project
        project = run_fabric_pattern("create_coding_project", "Create a full-stack web application using Python")
        print("Created Project:", project)
        
        # Save project details to a file
        project_path = os.path.join(env_vars["output_dir"], "project.txt")
        with open(project_path, "w") as f:
            f.write(project)
    except Exception as e:
        logging.error("Error in main function: %s", e)
        print("Error: Unable to complete project")
    
    end_time = time.time()
    estimated_time = (end_time - start_time) / 60
    print(f"Estimated time to complete project: {estimated_time:.2f} minutes")

if __name__ == "__main__":
    main()