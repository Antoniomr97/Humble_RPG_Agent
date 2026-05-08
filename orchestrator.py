import os
import sys
import time
from agents.runner.loader import load_agent
from agents.runner.agent_loop import AgentRunner

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header():
    print("\033[95m" + "="*50 + "\033[0m")
    print("\033[96m" + "   🤖 RPG AGENTIC 2D — OLLAMA ORCHESTRATOR" + "\033[0m")
    print("\033[95m" + "="*50 + "\033[0m")

def main():
    clear_screen()
    print_header()
    
    runner = AgentRunner()
    repo_path = "." # Current directory

    while True:
        print("\n\033[1mSelect an option:\033[0m")
        print(" 1. 🏗️  Architect (Design)")
        print(" 2. 🎮 Gameplay  (Implement)")
        print(" 3. 🔍 Reviewer  (Fix/Improve)")
        print(" 4. 🔁 Full Flow (Architect -> Gameplay -> Reviewer)")
        print(" 0. 🚪 Exit")
        
        choice = input("\nChoice: ").strip()
        
        if choice == '0':
            print("Goodbye! 👋")
            break
            
        if choice not in ['1', '2', '3', '4']:
            print("❌ Invalid option.")
            continue
            
        task = input("\033[1mEnter Task/Goal:\033[0m ").strip()
        if not task:
            print("⚠️ Task cannot be empty.")
            continue

        agents_to_run = []
        if choice == '1': agents_to_run = [('architect', 'Architect')]
        elif choice == '2': agents_to_run = [('gameplay', 'Gameplay')]
        elif choice == '3': agents_to_run = [('reviewer', 'Reviewer')]
        elif choice == '4': 
            agents_to_run = [
                ('architect', 'Architect'),
                ('gameplay', 'Gameplay'),
                ('reviewer', 'Reviewer')
            ]
        
        current_task = task
        for agent_id, agent_name in agents_to_run:
            print(f"\n\033[94m▶️  Running {agent_name} Agent...\033[0m")
            
            try:
                agent_data = load_agent(agent_id)
                system_prompt = agent_data['system']
                
                # Execute the agent loop
                response = runner.run(repo_path, current_task, system_prompt, agent_name)
                
                # In a full flow, the output of one could potentially influence the next
                # For now, we keep the task but notify about completion
                print(f"✅ {agent_name} completed.")
                
                # If we have more agents, maybe we wait a bit for visibility
                if len(agents_to_run) > 1:
                    time.sleep(1)
                    
            except Exception as e:
                print(f"❌ Error in {agent_name} flow: {e}")
                break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting... 👋")
        sys.exit(0)