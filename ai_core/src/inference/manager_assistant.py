import ollama
import yaml
from datetime import datetime

class ManagerAssistant:
    def __init__(self, persona_config="manager"):
        # Load persona configuration
        with open(f"../ollama_interface/persona_configs/{persona_config}.yaml") as f:
            self.config = yaml.safe_load(f)
        
        self.model = self.config["model"]
        self.history = []
        
    def generate_response(self, user_query):
        # Build system context
        context = f"CURRENT DATE: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
        context += f"USER QUERY: {user_query}\n\nRESPONSE FORMAT:\n"
        
        # Add format requirements
        context += "1. Request summary\n2. Key action areas\n3. Owner assignments\n"
        context += "4. Timelines\n5. Success metrics\n"
        
        # Generate response
        response = ollama.chat(
            model=self.model,
            messages=[{
                'role': 'user',
                'content': context
            }],
            options={
                'num_gpu': 20,  # Use GPU layers
                'temperature': 0.7
            }
        )
        return response['message']['content']
    
    def interactive_session(self):
        print(f"\n=== {self.config['name'].upper()} READY ===")
        print("Type 'exit' to end session\n")
        
        while True:
            query = input("\nManagement Request: ")
            if query.lower() == 'exit':
                break
                
            response = self.generate_response(query)
            print(f"\nMANAGER RESPONSE:\n{'-'*30}")
            print(response)
            print('-' * 30)

if __name__ == "__main__":
    assistant = ManagerAssistant()
    assistant.interactive_session()