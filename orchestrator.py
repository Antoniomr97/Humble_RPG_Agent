import os
import sys
import time
from agents.runner.loader import load_agent
from agents.runner.agent_loop import AgentRunner

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    # Use standard text for maximum compatibility
    print("="*50)
    print("   RPG AGENTIC 2D -- OLLAMA ORCHESTRATOR")
    print("="*50)

def select_model():
    temp_runner = AgentRunner()
    models = temp_runner.client.list_local_models()
    
    print("\nAvailable Models in Ollama:")
    if not models:
        print(" ! No models found or Ollama is not running.")
        model = input(" Enter model name manually (e.g., qwen2.5-coder:7b): ").strip()
        return model if model else "qwen2.5-coder:7b"
    
    for i, model in enumerate(models, 1):
        print(f" {i}. {model}")
    
    while True:
        try:
            choice = input(f"\nSelect model (1-{len(models)}) [default 1]: ").strip()
            if not choice: return models[0]
            idx = int(choice) - 1
            if 0 <= idx < len(models):
                return models[idx]
        except ValueError:
            pass
        print("X Invalid selection.")

def main():
    clear_screen()
    print_header()
    
    selected_model = select_model()
    print(f"\nUsing model: {selected_model}")
    
    runner = AgentRunner(model=selected_model)
    repo_path = "." # Current directory

    while True:
        print("\nSelect an option:")
        print(" 1. Architect (Design)")
        print(" 2. Gameplay  (Implement)")
        print(" 3. Designer  (Beautify)")
        print(" 4. Reviewer  (Fix/Improve)")
        print(" 5. Full Flow (Arch -> Game -> Design -> Rev)")
        print(" 0. Exit")
        
        choice = input("\nChoice: ").strip()
        
        if choice == '0':
            print("Goodbye! ")
            break
            
        if choice not in ['1', '2', '3', '4', '5']:
            print("X Invalid option.")
            continue
            
        task = input("Enter Task/Goal: ").strip()
        if not task:
            print("! Task cannot be empty.")
            continue

        agents_to_run = []
        if choice == '1': agents_to_run = [('architect', 'Architect')]
        elif choice == '2': agents_to_run = [('gameplay', 'Gameplay')]
        elif choice == '3': agents_to_run = [('designer', 'Designer')]
        elif choice == '4': agents_to_run = [('reviewer', 'Reviewer')]
        elif choice == '5': 
            agents_to_run = [
                ('architect', 'Architect'),
                ('gameplay', 'Gameplay'),
                ('designer', 'Designer'),
                ('reviewer', 'Reviewer')
            ]
        
        current_task = task
        for agent_id, agent_name in agents_to_run:
            print(f"\n-> Running {agent_name} Agent...")
            
            try:
                agent_data = load_agent(agent_id)
                system_prompt = agent_data['system']
                
                # Execute the agent loop
                response = runner.run(repo_path, current_task, system_prompt, agent_name)
                
                print(f"OK: {agent_name} completed.")
                
                if len(agents_to_run) > 1:
                    time.sleep(1)
                    
            except Exception as e:
                print(f"X Error in {agent_name} flow: {e}")
                break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting...")
        sys.exit(0)