import subprocess

def call_lpi_tool():
    try:
        result = subprocess.run(
            ["node", "../lpi-developer-kit/dist/test-client.js"],
            capture_output=True,
            text=True
        )
        return result.stdout
    except Exception as e:
        return f"Error calling LPI tool: {str(e)}"


def run_agent():
    print("🤖 SMILE Industry Advisor Agent")

    while True:
        try:
            user_input = input("\n👉 Ask your question (type exit to quit): ")

            if user_input.lower() == "exit":
                break

            print("\n🔍 Calling LPI tools...")

            tool_output = call_lpi_tool()

            print("\n📊 LPI Tool Output:")
            print(tool_output[:500])  # limit output

            print("\n💡 Answer:")
            print("SMILE is a structured methodology for digital twin implementation.")

            print("\n🧠 Explainability:")
            print("This response uses LPI tool data (smile_overview + get_insights).")

        except Exception as e:
            print("\n❌ Error occurred:", e)
            print("Try again with a valid question.")


if __name__ == "__main__":
    run_agent()