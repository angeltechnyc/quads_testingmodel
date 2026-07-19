import os
def load_secrets(self, env_path: str) -> dict:
        """
        Pre-emptively checks for a .env file and parses its contents 
        into a dictionary. Returns an empty dict if the file is missing.
        """
        # Pre-emptive guard clause to prevent crashing if .env is missing
        if not os.path.exists(env_path):
            return {}
            
        secrets = {}
        
        # Open and read the file safely
        with open(env_path, 'r') as file:
            for line in file:
                line = line.strip()
                
                # Skip empty lines or comments
                if not line or line.startswith('#'):
                    continue
                
                # Ensure the line is a valid key-value pair before splitting
                if '=' in line:
                    # Split only on the first '=' to protect complex keys/tokens
                    key, value = line.split('=', 1)
                    
                    # Strip whitespace and any surrounding quotes
                    clean_key = key.strip()
                    clean_value = value.strip().strip('"').strip("'")
                    
                    secrets[clean_key] = clean_value
                    
        return secrets