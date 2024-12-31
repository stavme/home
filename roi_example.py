
def comparison_promt(promt, threshold, bigger_prompt, smaller_prompt):
    variable = int(input(promt))
    if variable > threshold:
        print(bigger_prompt)
    else:
        print(smaller_prompt)

comparison_promt("בן כמה אתה?", 5, "ילד גדול", "אתה מניאק, תחזור פעם הבאה")
