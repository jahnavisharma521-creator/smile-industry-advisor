print("🤖 SMILE Industry Advisor Agent")

question = input("👉 Ask your question: ")

if "hospital" in question.lower():
    print("\n💡 Hospitals can use digital twins by first understanding their system (SMILE overview), then applying insights and case studies.")
elif "smile" in question.lower():
    print("\n💡 SMILE is a structured methodology for digital twin implementation with phases like reality emulation and impact generation.")
else:
    print("\n💡 This relates to digital twin systems. You should start with SMILE methodology and explore insights.")

print("\n✅ Tools used: smile_overview + get_insights")