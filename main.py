import sys
import os

# Ensure the root directory is in sys.path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.game import main

if __name__ == "__main__":
    print("🚀 Launching Humble RPG...")
    try:
        main()
    except Exception as e:
        print(f"❌ Error during game execution: {e}")
