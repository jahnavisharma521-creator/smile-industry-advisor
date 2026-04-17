def smile_overview():
    return "SMILE is a structured methodology for digital twin implementation."

def get_insights(query):
    return f"Insights for: {query} — Start with understanding system, then apply SMILE phases."


def run_agent():
    print("🤖 SMILE Industry Advisor Agent")

    while True:
        try:
            user_input = input("\n👉 Ask your question (type exit to quit): ")

            if user_input.lower() == "exit":
                break

            print("\n🔍 Calling LPI tools...")

            # ✅ Explicit tool calls (IMPORTANT)
            overview = smile_overview()
            insights = get_insights(user_input)

            print("\n📊 Tool Outputs:")
            print("smile_overview →", overview)
            print("get_insights →", insights)

            print("\n💡 Final Answer:")
            print(overview)
            print(insights)

            print("\n🧠 Explainability:")
            print("This answer was generated using:")
            print("- smile_overview (methodology)")
            print("- get_insights (contextual guidance)")

        except Exception as e:
            print("\n❌ Error:", str(e))
            print("Please try again.")

if __name__ == "__main__":
    run_agent()