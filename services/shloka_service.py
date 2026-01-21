import random

SHLOKAS = [
    {
        "shloka": "कर्मण्येवाधिकारस्ते मा फलेषु कदाचन",
        "meaning": "Focus on your efforts, not the results.",
        "explanation": "Do your duty sincerely without worrying about outcomes."
    },
    {
        "shloka": "न हि कल्याणकृत् कश्चिद्दुर्गतिं तात गच्छति",
        "meaning": "Good actions never go to waste.",
        "explanation": "Every sincere effort helps you grow."
    },
    {
        "shloka": "योगस्थः कुरु कर्माणि सङ्गं त्यक्त्वा धनञ्जय",
        "meaning": "Perform your duties without attachment.",
        "explanation": "Do your work with detachment to achieve peace."
    },
    {
        "shloka": "सर्वधर्मान्परित्यज्य मामेकं शरणं व्रज",
        "meaning": "Surrender to me alone.",
        "explanation": "Let go of all duties and take refuge in the divine."
    },
    {
        "shloka": "मनः प्रसादः सौम्यत्वं मौनमात्मविनिग्रहः",
        "meaning": "Peace of mind, gentleness, silence, and self-control.",
        "explanation": "These are qualities of true knowledge."
    },
    {
        "shloka": "अहिंसा सत्यमस्तेयं शौचं सन्तोष आर्जवम्",
        "meaning": "Non-violence, truth, non-stealing, purity, contentment, and straightforwardness.",
        "explanation": "These are the virtues to cultivate."
    },
    {
        "shloka": "विद्या दानं तपः शौचं क्षान्तिः सत्यं दमः शमः",
        "meaning": "Knowledge, charity, austerity, purity, patience, truth, control, and peace.",
        "explanation": "These lead to spiritual growth."
    },
    {
        "shloka": "सुखदुःखे समे कृत्वा लाभालाभौ जयाजयौ",
        "meaning": "Treat pleasure and pain equally.",
        "explanation": "Remain balanced in gain and loss, victory and defeat."
    },
    {
        "shloka": "तस्मादसक्तः सततं कार्यं कर्म समाचर",
        "meaning": "Perform your duties without attachment.",
        "explanation": "Engage in work as an offering."
    },
    {
        "shloka": "यदा यदा हि धर्मस्य ग्लानिर्भवति भारत",
        "meaning": "Whenever righteousness declines.",
        "explanation": "The divine manifests to restore dharma."
    }
]

def get_daily_shloka():
    return random.choice(SHLOKAS)