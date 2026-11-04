"""Chatbot brain for the SRMU Admission Guide (pure Python, no libraries)."""

OFFICIAL = "https://www.srmu.ac.in"

# Course data: key -> (name, why it suits you)
COURSES = {
    "btech": ("B.Tech (CSE, AI/ML, Civil, Mechanical, Electrical)", "Best for maths and science lovers who want engineering and tech jobs."),
    "bca":   ("BCA", "Good for computers and software careers; also leads to MCA."),
    "bba":   ("BBA", "Good for management, marketing and starting your own business."),
    "bpharm":("B.Pharm / D.Pharm", "For a career in medicines, pharma companies and drug stores."),
    "nurs":  ("B.Sc Nursing / Allied Health", "For healthcare and hospital careers."),
    "agri":  ("B.Sc Agriculture", "For farming science, agri-business and government agri jobs."),
    "bcom":  ("B.Com", "For accounts, finance, banking and CA/CS preparation."),
    "law":   ("LLB / BA LLB", "For court, corporate legal work and judiciary exams."),
    "ba":    ("BA (Arts / Humanities)", "Good base for civil services, teaching and social sciences."),
    "jmc":   ("Journalism & Mass Communication", "For media, content, PR and creative careers."),
    "bed":   ("Education (B.Ed / D.El.Ed)", "For a teaching career."),
    "dip":   ("Diploma / Polytechnic", "Short technical course after 10th with early job options."),
    "mba":   ("MBA", "Postgraduate management degree for leadership roles."),
    "mtech": ("M.Tech / MCA", "Advanced tech degrees for specialist and research roles."),
    "pg":    ("M.Pharm / LLM / MA / M.Com", "Postgraduate study in your own field."),
}

END = ["Admission process", "Start over"]


def course_list(keys, intro="Based on your answer, I recommend:"):
    items = "".join(f"<li><b>{COURSES[k][0]}</b> – {COURSES[k][1]}</li>" for k in keys)
    return f"{intro}<ul>{items}</ul>"


def link(text):
    return f'<a href="{OFFICIAL}" target="_blank" rel="noopener">{text}</a>'


# Rules are checked in order: (keywords, handler). First match wins.
def get_reply(message: str) -> dict:
    s = message.lower().strip()
    has = lambda *words: any(w in s for w in words)

    if has("start over", "restart", "hi", "hello", "namaste") and len(s) < 14:
        return {"restart": True}

    if has("after 10", "10th", "tenth", "diploma", "polytechnic"):
        return {"html": course_list(["dip"], "After 10th, a good path is:") +
                "You can also continue 11th–12th and pick a stream later.",
                "chips": ["After 12th", "Admission process", "Start over"]}

    if has("i did b.tech", "i did bca"):
        return {"html": course_list(["mtech", "mba"]), "chips": END}
    if has("i did bba", "i did b.com"):
        return {"html": course_list(["mba"]), "chips": END}
    if has("i did pharmacy", "i did law"):
        return {"html": course_list(["pg"]), "chips": END}
    if has("graduat", "after ba", "after b.tech", "pg", "master", "post"):
        return {"html": "Which field are you in?",
                "chips": ["I did B.Tech/BCA", "I did BBA/B.Com", "I did Pharmacy / Law / Arts"]}

    if has("after 12", "12th", "twelfth", "intermediate"):
        return {"html": "Great! <b>Which stream did you study in 12th?</b>",
                "chips": ["PCM (Maths)", "PCB (Biology)", "Commerce", "Arts"]}
    if has("pcm", "maths", "math"):
        return {"html": course_list(["btech", "bca", "bba"]),
                "chips": ["I like coding", "I like business", "Admission process"]}
    if has("pcb", "biology", "bio"):
        return {"html": course_list(["bpharm", "nurs", "agri", "bca"]), "chips": END}
    if has("commerce", "account", "finance", "bank"):
        return {"html": course_list(["bcom", "bba", "law", "bca"]), "chips": END}
    if has("arts", "humanit", "history", "upsc", "ias", "civil serv"):
        return {"html": course_list(["ba", "law", "jmc", "bed"]), "chips": END}

    # Interest based
    if has("cod", "computer", "software", "program", "ai", "it job", "tech", "engineer"):
        return {"html": course_list(["btech", "bca", "mtech"], "For a tech career, consider:"), "chips": END}
    if has("business", "manage", "market", "startup", "mba", "bba"):
        return {"html": course_list(["bba", "mba", "bcom"], "For business and management:"), "chips": END}
    if has("doctor", "medic", "pharm", "nurs", "health", "hospital"):
        return {"html": course_list(["bpharm", "nurs"], "For healthcare careers:"), "chips": END}
    if has("law", "lawyer", "judge", "court", "advocate"):
        return {"html": course_list(["law"], "For law:"), "chips": END}
    if has("farm", "agri", "kheti"):
        return {"html": course_list(["agri"], "For agriculture:"), "chips": END}
    if has("media", "journal", "creative", "anchor", "film"):
        return {"html": course_list(["jmc", "ba"], "For media and creative work:"), "chips": END}
    if has("teach", "education", "b.ed", "bed"):
        return {"html": course_list(["bed", "ba"], "For teaching:"), "chips": END}

    # Information
    if has("process", "how to apply", "apply", "admission", "form", "document", "eligib"):
        return {"html": "<b>Typical admission steps</b><ul>"
                "<li>Choose your course using this guide.</li>"
                "<li>Check eligibility (marks and subjects) for that course.</li>"
                "<li>Fill the online application form on the official website.</li>"
                "<li>Keep ready: 10th and 12th marksheets, ID proof, photo, and category/transfer certificates if needed.</li>"
                "<li>Attend counselling or entrance if required, then pay the fee to confirm your seat.</li></ul>"
                "Exact dates, fees and eligibility can change each year, so please verify them at "
                + link("srmu.ac.in") + ".",
                "chips": ["Contact / Apply", "Start over"]}
    if has("contact", "phone", "address", "location", "where"):
        return {"html": "SRMU (Shri Ramswaroop Memorial University) is near Lucknow–Deva Road, Barabanki, "
                "Uttar Pradesh. For phone numbers and the latest address, open " + link("the official website") +
                " and use its Admission / Contact page.", "chips": END}
    if has("fee", "cost", "scholar", "hostel", "placement"):
        return {"html": "Fees, scholarships, hostel and placement details change every session. Please check the "
                "latest numbers on " + link("srmu.ac.in") + " or call the admission office.", "chips": END}

    return {"html": "I didn’t fully get that. Tell me your <b>education level</b> (10th, 12th, graduate) "
            "or an <b>interest</b> like coding, business, health, law, farming or media.",
            "chips": ["After 12th", "After 10th", "After Graduation", "I like coding", "I like business"]}
