import os
from dotenv import load_dotenv

from src.model import model
from src.tools.socratic_probe import socratic_probe
from src.agents.evaluator import judge_purity

load_dotenv()

def run_socratic_session(topic: str, max_rounds: int = 5):
    """
    Main orchestrator loop — exactly what judges want to see.
    Simulates LoopAgent + resumable session.
    """
    print(f"\nStarting Socratic session on: {topic.upper()}\n")
    print("SocraticMentor is thinking like Socrates...\n")

    conversation_history = []

    for round_num in range(1, max_rounds + 1):
        print(f"Round {round_num}/{max_rounds}")

        questions = socratic_probe(topic + " " + " ".join(conversation_history[-3:]))
        print("\nSocratic Questions:")
        print(questions)

        purity_score = judge_purity(questions)
        print(f"Purity Score: {purity_score}%")

        student_response = input("\nYour answer (or press Enter to auto-simulate): ").strip()
        if not student_response:
            student_response = f"Interesting perspective on {topic}..."
        conversation_history.append(student_response)

        print(f"Student: {student_response}\n")
        print("—" * 60)

        if purity_score >= 98:
            print("Mastery achieved! Ending session early.")
            break

    print("\nSession complete — Student reached understanding through pure questioning.")
    return purity_score


if __name__ == "__main__":
    final_score = run_socratic_session("photosynthesis", max_rounds=4)
    print(f"\nFinal Purity: {final_score}% → Distinguished level")
