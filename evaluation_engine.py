

import random
import re



def evaluate_candidate(
    answers,
    job_role,
    fraud_flags=None,
    behavior_signals=None
):

    if fraud_flags is None:
        fraud_flags = []

    if behavior_signals is None:
        behavior_signals = []




    all_answers = " ".join(
        answers
    ).lower()

    words = all_answers.split()

    word_count = len(words)

    sentence_count = max(
        1,
        len(re.findall(r'[.!?]', all_answers))
    )

    avg_sentence_length = (
        word_count / sentence_count
    )

    unique_word_count = len(set(words))

    vocabulary_richness = (
        unique_word_count / max(1, word_count)
    )



  

    negative_words = [
        "fight",
        "lazy",
        "late",
        "angry",
        "absent",
        "ignore",
        "careless"
    ]




    experience_words = [
        "years",
        "experience",
        "worked",
        "industry",
        "previous"
    ]



    confidence_words = [
        "managed",
        "handled",
        "solved",
        "operated",
        "led",
        "responsible",
        "experience",
        "trained",
        "organized",
        "completed",
        "maintained",
        "achieved",
        "improved",
        "learned"
    ]




    teamwork_words = [
        "team",
        "together",
        "cooperate",
        "support",
        "group",
        "workers",
        "staff",
        "helped",
        "coordination",
        "shared"
    ]



    safety_words = [
        "safety",
        "helmet",
        "rules",
        "precaution",
        "careful",
        "protection",
        "secure",
        "hazard",
        "guidelines",
        "risk"
    ]




    problem_solving_words = [
        "fixed",
        "solved",
        "issue",
        "problem",
        "repair",
        "managed",
        "handled",
        "resolved",
        "improved"
    ]



    communication_words = [
        "explained",
        "communicated",
        "understood",
        "discussed",
        "reported",
        "clarified",
        "informed"
    ]



  

    reliability_words = [
        "punctual",
        "daily",
        "consistent",
        "responsible",
        "discipline",
        "regular",
        "attendance"
    ]




    adaptability_words = [
        "learn",
        "adapt",
        "training",
        "new",
        "change",
        "improve",
        "flexible"
    ]



    leadership_words = [
        "lead",
        "supervise",
        "guide",
        "manage",
        "coordinate",
        "monitor"
    ]



    

    role_keywords = {

        "Construction Worker": [
            "construction",
            "cement",
            "site",
            "building",
            "labor",
            "safety",
            "equipment",
            "helmet"
        ],

        "Factory Worker": [
            "factory",
            "machine",
            "production",
            "assembly",
            "equipment",
            "quality",
            "shift"
        ],

        "Driver": [
            "driving",
            "vehicle",
            "license",
            "delivery",
            "transport",
            "traffic",
            "route"
        ],

        "Warehouse Worker": [
            "warehouse",
            "inventory",
            "loading",
            "packing",
            "storage",
            "shipment",
            "logistics"
        ]
    }



    selected_role_keywords = role_keywords.get(
        job_role,
        []
    )




    def count_hits(keyword_group):

        return sum(
            word in all_answers
            for word in keyword_group
        )



    confidence_hits = count_hits(
        confidence_words
    )

    teamwork_hits = count_hits(
        teamwork_words
    )

    safety_hits = count_hits(
        safety_words
    )

    problem_hits = count_hits(
        problem_solving_words
    )

    communication_hits = count_hits(
        communication_words
    )

    reliability_hits = count_hits(
        reliability_words
    )

    adaptability_hits = count_hits(
        adaptability_words
    )

    leadership_hits = count_hits(
        leadership_words
    )

    role_hits = count_hits(
        selected_role_keywords
    )

    experience_hits = count_hits(
        experience_words
    )

    negative_hits = count_hits(
        negative_words
    )



  

    if word_count > 140:

        clarity = 10

    elif word_count > 100:

        clarity = 9

    elif word_count > 70:

        clarity = 8

    elif word_count > 45:

        clarity = 7

    elif word_count > 25:

        clarity = 6

    else:

        clarity = 4



    

    if vocabulary_richness > 0.7:

        language_quality = 9

    elif vocabulary_richness > 0.55:

        language_quality = 8

    elif vocabulary_richness > 0.4:

        language_quality = 7

    else:

        language_quality = 5



  

    relevance = min(
        10,
        4 + (role_hits * 1.5)
    )

    confidence = min(
        10,
        5 + confidence_hits
    )

    teamwork = min(
        10,
        5 + teamwork_hits
    )

    safety = min(
        10,
        5 + safety_hits
    )

    problem_solving = min(
        10,
        5 + problem_hits
    )

    communication = min(
        10,
        5 + communication_hits
    )

    reliability = min(
        10,
        5 + reliability_hits
    )

    adaptability = min(
        10,
        5 + adaptability_hits
    )

    leadership = min(
        10,
        5 + leadership_hits
    )




    engagement = 7

    if avg_sentence_length > 12:

        engagement = 9

    elif avg_sentence_length > 8:

        engagement = 8

    elif avg_sentence_length > 5:

        engagement = 7

    else:

        engagement = 5



    video_behavior_bonus = 0

    if any(
        "attention maintained" in x.lower()
        for x in behavior_signals
    ):

        video_behavior_bonus += 0.4

    if any(
        "stable" in x.lower()
        for x in behavior_signals
    ):

        video_behavior_bonus += 0.3




    integrity = random.randint(85, 97)

    if any(
        "multiple faces" in x.lower()
        for x in fraud_flags
    ):

        integrity -= 25

    if any(
        "no face" in x.lower()
        for x in fraud_flags
    ):

        integrity -= 15

    integrity = max(40, integrity)




    avg = (
        clarity +
        confidence +
        relevance +
        teamwork +
        safety +
        problem_solving +
        communication +
        reliability +
        adaptability +
        leadership +
        language_quality +
        engagement
    ) / 12

    avg -= negative_hits * 0.3

    avg += experience_hits * 0.15

    avg += video_behavior_bonus



   

    if word_count < 20:

        avg -= 1



    avg = max(
        0,
        min(avg, 10)
    )




    if any(
        "multiple faces" in x.lower()
        for x in fraud_flags
    ):

        classification = "SUSPECTED FRAUD"

    elif word_count < 12:

        classification = "LOW CONFIDENCE"

    elif avg >= 8.7:

        classification = "JOB READY"

    elif avg >= 7:

        classification = "NEEDS TRAINING"

    else:

        classification = "MANUAL REVIEW"



    

    strengths = []

    if confidence >= 8:

        strengths.append(
            "High confidence and ownership indicators"
        )

    if teamwork >= 8:

        strengths.append(
            "Strong collaboration and teamwork signals"
        )

    if safety >= 8:

        strengths.append(
            "Excellent safety-awareness behavior"
        )

    if relevance >= 8:

        strengths.append(
            "Strong job-role alignment detected"
        )

    if communication >= 8:

        strengths.append(
            "Clear communication structure observed"
        )

    if adaptability >= 8:

        strengths.append(
            "Positive learning and adaptability indicators"
        )

    if leadership >= 8:

        strengths.append(
            "Leadership potential identified"
        )

    if any(
        "attention maintained" in x.lower()
        for x in behavior_signals
    ):

        strengths.append(
            "Consistent behavioral attention observed during video assessment"
        )



    concerns = []

    if clarity <= 5:

        concerns.append(
            "Limited communication depth"
        )

    if relevance <= 5:

        concerns.append(
            "Low role-specific alignment"
        )

    if safety <= 5:

        concerns.append(
            "Limited safety-awareness indicators"
        )

    if teamwork <= 5:

        concerns.append(
            "Weak teamwork indicators"
        )

    if any(
        "multiple faces" in x.lower()
        for x in fraud_flags
    ):

        concerns.append(
            "Potential identity inconsistency detected"
        )

    if any(
        "far from camera" in x.lower()
        for x in behavior_signals
    ):

        concerns.append(
            "Reduced engagement visibility during interview"
        )

    if len(concerns) == 0:

        concerns.append(
            "No major workforce concerns detected"
        )



    if classification == "JOB READY":

        recommendation = (
            "Candidate recommended for immediate onboarding "
            "with high workforce readiness confidence."
        )

    elif classification == "NEEDS TRAINING":

        recommendation = (
            "Candidate suitable after supervised training "
            "and monitored onboarding."
        )

    elif classification == "LOW CONFIDENCE":

        recommendation = (
            "Additional interview responses required "
            "for reliable workforce evaluation."
        )

    elif classification == "SUSPECTED FRAUD":

        recommendation = (
            "Manual verification recommended due to "
            "integrity signal anomalies detected during "
            "video assessment."
        )

    else:

        recommendation = (
            "Additional manual evaluation and skill assessment "
            "recommended before onboarding."
        )



   

    return {

        "clarity": clarity,

        "confidence": confidence,

        "relevance": relevance,

        "teamwork": teamwork,

        "safety": safety,

        "problem_solving": problem_solving,

        "communication": communication,

        "reliability": reliability,

        "adaptability": adaptability,

        "leadership": leadership,

        "language_quality": language_quality,

        "engagement": engagement,

        "integrity": integrity,

        "classification": classification,

        "strengths": strengths,

        "concerns": concerns,

        "recommendation": recommendation,

        "avg": round(avg, 2)
    }