import os
import yaml

from dotenv import load_dotenv

load_dotenv()


def get_prompt(prompt_name: str, version: str | None = None) -> dict[str, str] | str:
    """
    Retrieves the content of a prompt file based on the provided prompt name.
    
    Args:
        prompt_name (str): The name of the prompt file (without extension).
        version (str | None): Optional version of the prompt to retrieve.

    Returns:
        dict[str, str] | str: The content of the prompt file.
        
    Raises:
        FileNotFoundError: If the prompt file does not exist.
    """
    file_path = os.path.join(os.getenv("PROMPT_DIR", "./prompts"), f"{prompt_name}.txt")
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Prompt file '{file_path}' does not exist.")

    with open(file_path, 'r', encoding='utf-8') as file:
        prompt_raw = file.read()
    prompt_content = yaml.safe_load(prompt_raw)

    if version:
        if version not in prompt_content:
            raise ValueError(f"Version '{version}' not found in prompt '{prompt_name}'.")
        
        return prompt_content["version"]

    return prompt_content


__all__ = ["get_prompt"]