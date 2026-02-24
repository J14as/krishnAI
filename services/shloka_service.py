import random

SHLOKAS = [
    {
        "shloka": "कर्मण्येवाधिकारस्ते मा फलेषु कदाचन",
        "meaning": "You have a right to perform your duties, but never to the fruits of your actions.",
        "explanation": "Do your work sincerely and with full effort, but do not make the outcome the reason for living. Whether you succeed or fail tomorrow, your job today is simply to act well.",
        "example": "A student who studies hard every day, regardless of exam results, embodies this teaching. They give their best, but do not let the fear of marks stop them from sitting down and opening the book."
    },
    {
        "shloka": "न हि कल्याणकृत् कश्चिद्दुर्गतिं तात गच्छति",
        "meaning": "One who does good never comes to harm.",
        "explanation": "Every sincere act of goodness plants a seed that eventually blossoms. Even if results seem delayed, no genuine effort is ever wasted.",
        "example": "A doctor who treats patients honestly and with compassion, even without expecting recognition, will always find meaning and peace in their work — and their reputation grows naturally over time."
    },
    {
        "shloka": "योगस्थः कुरु कर्माणि सङ्गं त्यक्त्वा धनञ्जय",
        "meaning": "Rooted in yoga (equanimity), perform your actions while abandoning attachment.",
        "explanation": "Work from a place of inner stillness. When you are not emotionally tied to whether things go your way, you act more clearly and freely.",
        "example": "An entrepreneur launching a startup should put in their best work each day without becoming obsessed with valuation numbers. This inner steadiness leads to better decisions and less burnout."
    },
    {
        "shloka": "सर्वधर्मान्परित्यज्य मामेकं शरणं व्रज",
        "meaning": "Abandon all varieties of duties and simply surrender to Me alone.",
        "explanation": "When all strategies, plans and rules feel overwhelming, there is a deeper refuge — trust in something greater than yourself. Let go of excessive control and allow life to unfold.",
        "example": "A parent who has done everything possible for a sick child, and finally rests in trust rather than panic, experiences this surrender. Letting go of what you cannot control is not weakness — it is wisdom."
    },
    {
        "shloka": "मनः प्रसादः सौम्यत्वं मौनमात्मविनिग्रहः",
        "meaning": "Serenity of mind, gentleness, silence, and self-restraint.",
        "explanation": "True wisdom shows up not in loud proclamations but in calm, gentle, controlled behaviour. A quiet mind makes better choices than a noisy one.",
        "example": "In a heated argument at work, the person who stays calm, listens before speaking, and responds gently — rather than reacting with anger — is the one who earns lasting respect."
    },
    {
        "shloka": "अहिंसा सत्यमस्तेयं शौचं सन्तोष आर्जवम्",
        "meaning": "Non-violence, truthfulness, non-stealing, purity, contentment, and straightforwardness.",
        "explanation": "These six virtues are the foundation of a meaningful life. Each one builds trust with others and inner peace within yourself.",
        "example": "A shopkeeper who gives the correct weight, charges a fair price, and does not deceive customers practises all of these virtues at once — and earns loyalty that no advertisement can buy."
    },
    {
        "shloka": "विद्या दानं तपः शौचं क्षान्तिः सत्यं दमः शमः",
        "meaning": "Knowledge, charity, austerity, purity, patience, truth, self-control, and tranquility.",
        "explanation": "These eight qualities, practised consistently, elevate a person's character and open the path to spiritual growth.",
        "example": "A teacher who patiently explains a concept ten times to a slow learner, without frustration, and does so without expecting extra reward, demonstrates austerity, patience, and truth all at once."
    },
    {
        "shloka": "सुखदुःखे समे कृत्वा लाभालाभौ जयाजयौ",
        "meaning": "Treating pleasure and pain, gain and loss, victory and defeat equally.",
        "explanation": "Life swings between highs and lows. The person who is not shattered by failure or intoxicated by success remains stable and keeps moving forward.",
        "example": "An athlete who celebrates a win with the same quiet gratitude as they accept a defeat, and keeps training just as hard either way, embodies this equanimity. Their consistency is what makes them great."
    },
    {
        "shloka": "तस्मादसक्तः सततं कार्यं कर्म समाचर",
        "meaning": "Therefore, always perform your duty without attachment.",
        "explanation": "Work done as a pure offering — without craving recognition or fearing failure — becomes a form of meditation in itself.",
        "example": "A volunteer who cleans up a community park every weekend without waiting for a thank-you or a photo opportunity is doing exactly this — work as pure, joyful action."
    },
    {
        "shloka": "यदा यदा हि धर्मस्य ग्लानिर्भवति भारत",
        "meaning": "Whenever righteousness declines and unrighteousness rises, O Arjuna…",
        "explanation": "The divine principle of justice restores balance whenever the world tilts too far toward chaos. This reminds us that evil is never truly permanent.",
        "example": "Think of how, throughout history, periods of oppression and injustice have always eventually given way to reform movements, visionary leaders, and social change — as if the universe corrects itself."
    }
]

def get_daily_shloka():
    return random.choice(SHLOKAS)