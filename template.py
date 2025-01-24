import os

# Define the base directory
base_dir = "."

# Define the directory structure
structure = {
    "bin": ["start_jarvis.sh", "stop_jarvis.sh"],
    "config": ["config.yaml", "home_assistant.yaml", "face_recognition.yaml"],
    "data": {
        "face_data": [],
        "models": [],
        "logs": []
    },
    "src": {
        "voice": ["speech_to_text.py", "text_to_speech.py"],
        "nlp": ["intent_recognition.py", "response_generator.py"],
        "workflows": ["home_automation.py", "web_search.py", "face_recognition.py"],
        "main.py": ""
    },
    "tools": {
        "whisper": [],
        "gpt-neo": [],
        "opencv": []
    },
    "tests": ["test_voice.py", "test_nlp.py", "test_workflows.py"],
    "README.md": "",
    "requirements.txt": ""
}

# Function to create directories and files
def create_structure(base_path, structure):
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            # Create a directory and recurse
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)
        elif isinstance(content, list):
            # Create a directory and files inside it
            os.makedirs(path, exist_ok=True)
            for file_name in content:
                with open(os.path.join(path, file_name), "w") as f:
                    if file_name.endswith(".py"):
                        f.write("# Placeholder script\n")
                    elif file_name.endswith(".sh"):
                        f.write("#!/bin/bash\n\n# Placeholder script\n")
                    elif file_name.endswith(".yaml"):
                        f.write("# Placeholder configuration\n")
        else:
            # Create a file
            with open(path, "w") as f:
                if name.endswith(".md"):
                    f.write("# JarvisBot\n\nA personalized home automation assistant.\n")
                elif name.endswith(".txt"):
                    f.write("# Placeholder for requirements\n")
                elif name.endswith(".py"):
                    f.write("# Placeholder script\n")

# Create the structure
create_structure(base_dir, structure)

print(f"Project structure created successfully at {base_dir}!")