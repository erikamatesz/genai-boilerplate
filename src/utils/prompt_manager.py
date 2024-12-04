import os

class PromptManager:
    """
    Manage prompts based on templates stored in text files.
    """

    def __init__(self, templates_dir="prompts"):
        """
        Initializes the PromptManager and loads the templates.

        Args:
            templates_dir (str): Directory where template files are stored. 
                                  Defaults to 'prompts' if not specified.
        """
        self.templates_dir = templates_dir  # Set the templates directory
        self.templates = self._load_templates()

    def _load_templates(self):
        """
        Loads all templates from .txt files in the specified directory.

        Returns:
            dict: A dictionary with template names as keys and their contents as values.
        """
        templates = {}
        if not os.path.isdir(self.templates_dir):
            raise FileNotFoundError(f"The directory '{self.templates_dir}' was not found.")
        
        # Iterate over the files in the specified directory
        for filename in os.listdir(self.templates_dir):
            if filename.endswith(".txt"):
                # Get the template name without the file extension
                template_name = os.path.splitext(filename)[0]
                # Read the content of the template file
                with open(os.path.join(self.templates_dir, filename), "r", encoding="utf-8") as file:
                    templates[template_name] = file.read()
        return templates

    def generate_prompt(self, template_name, **kwargs):
        """
        Generates a prompt based on a template and replaces variables.

        Args:
            template_name (str): The name of the template to use.
            **kwargs: Variables to replace in the template.

        Returns:
            str: The generated prompt.
        """
        template = self.templates.get(template_name, None)
        if not template:
            raise ValueError(f"Template '{template_name}' not found.")
        try:
            # Format the template by replacing variables with provided values
            return template.format(**kwargs)
        except KeyError as e:
            raise ValueError(f"Missing variable in the template: {e}")
