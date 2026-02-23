import random

SHLOKAS = [
    {
        "shloka": "कर्मण्येवाधिकारस्ते मा फलेषु कदाचन",
        "meaning": "You have the right to work, not to the results.",
        "explanation": "Focus on sincere effort instead of worrying about outcomes.",
        "example": "A student studies consistently for exams without obsessing over marks, which naturally improves performance."
    },
    {
        "shloka": "न हि कल्याणकृत् कश्चिद्दुर्गतिं तात गच्छति",
        "meaning": "Good actions never go to waste.",
        "explanation": "Every positive effort contributes to growth.",
        "example": "Helping classmates regularly builds confidence and goodwill even if rewards are not immediate."
    },
    {
        "shloka": "योगस्थः कुरु कर्माणि सङ्गं त्यक्त्वा धनञ्जय",
        "meaning": "Perform your duties with balance and detachment.",
        "explanation": "A calm mind helps you work better under pressure.",
        "example": "A student focuses on preparation instead of stressing about competition."
    },
    {
        "shloka": "सुखदुःखे समे कृत्वा लाभालाभौ जयाजयौ",
        "meaning": "Remain balanced in success and failure.",
        "explanation": "Emotional balance helps in long-term success.",
        "example": "A student treats both good and bad exam results as learning experiences."
    },
    {
        "shloka": "उद्धरेदात्मनाऽत्मानं नात्मानमवसादयेत्",
        "meaning": "Lift yourself by your own effort.",
        "explanation": "Self-belief is essential for progress.",
        "example": "After failing once, a student regains confidence and prepares again."
    },
    {
        "shloka": "मनः प्रसादः सौम्यत्वं मौनमात्मविनिग्रहः",
        "meaning": "Calmness, gentleness, and self-control.",
        "explanation": "Inner discipline brings clarity.",
        "example": "A calm student handles pressure better during exams."
    },
    {
        "shloka": "श्रद्धावान् लभते ज्ञानं",
        "meaning": "Those with faith gain knowledge.",
        "explanation": "Belief in learning enhances growth.",
        "example": "A student who trusts the learning process improves steadily."
    },
    {
        "shloka": "तस्मादसक्तः सततं कार्यं कर्म समाचर",
        "meaning": "Work without attachment.",
        "explanation": "Let go of fear and focus on action.",
        "example": "A student gives their best effort without fear of failure."
    },
    {
        "shloka": "विद्या दानं तपः शौचं क्षान्तिः सत्यं दमः शमः",
        "meaning": "Knowledge, patience, and self-control.",
        "explanation": "These values build strong character.",
        "example": "A disciplined student balances studies and personal life."
    },
    {
        "shloka": "आत्मैव ह्यात्मनो बन्धुरात्मैव रिपुरात्मनः",
        "meaning": "The mind can be your friend or enemy.",
        "explanation": "Your thoughts shape your reality.",
        "example": "Positive thinking helps a student overcome self-doubt."
    },
    {
        "shloka": "यदा संहरते चायं कूर्मोऽङ्गानीव सर्वशः",
        "meaning": "Withdraw the mind from distractions.",
        "explanation": "Focus improves efficiency.",
        "example": "Avoiding social media during study hours increases concentration."
    },
    {
        "shloka": "नियतं कुरु कर्म त्वं कर्म ज्यायो ह्यकर्मणः",
        "meaning": "Action is better than inaction.",
        "explanation": "Taking steps matters more than waiting.",
        "example": "Starting revision early reduces exam stress."
    },
    {
        "shloka": "असंशयं महाबाहो मनो दुर्निग्रहं चलम्",
        "meaning": "The mind is restless.",
        "explanation": "Awareness helps manage distractions.",
        "example": "Mindfulness helps students focus better."
    },
    {
        "shloka": "संयम्येन्द्रियग्रामं सर्वत्र समबुद्धयः",
        "meaning": "Control senses with balance.",
        "explanation": "Discipline leads to success.",
        "example": "Limiting screen time improves academic performance."
    },
    {
        "shloka": "क्लैब्यं मा स्म गमः पार्थ",
        "meaning": "Do not give in to weakness.",
        "explanation": "Courage helps overcome challenges.",
        "example": "Facing interviews confidently improves chances of success."
    },
    {
        "shloka": "श्रेयान्स्वधर्मो विगुणः",
        "meaning": "Follow your own path.",
        "explanation": "Personal growth matters more than comparison.",
        "example": "Choosing a career aligned with skills brings satisfaction."
    },
    {
        "shloka": "योगः कर्मसु कौशलम्",
        "meaning": "Excellence in action is yoga.",
        "explanation": "Skillful work brings fulfillment.",
        "example": "Focused study sessions lead to better understanding."
    },
    {
        "shloka": "नैव किंचित्करोमीति",
        "meaning": "Remain humble in action.",
        "explanation": "Humility keeps learning continuous.",
        "example": "A topper remains open to improvement."
    },
    {
        "shloka": "सन्तोषः परमं सुखम्",
        "meaning": "Contentment is the greatest happiness.",
        "explanation": "Peace comes from acceptance.",
        "example": "Being satisfied with steady progress reduces anxiety."
    },
    {
        "shloka": "यदा यदा हि धर्मस्य ग्लानिर्भवति भारत",
        "meaning": "When values decline, guidance arises.",
        "explanation": "Support appears when needed.",
        "example": "Seeking mentorship during confusion restores direction."
    }
]


def get_daily_shloka():
    return random.choice(SHLOKAS)