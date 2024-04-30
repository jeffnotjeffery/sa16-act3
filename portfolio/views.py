from django.shortcuts import render

def home(request):
    context = {
        'welcome': 'Welcome to My Portfolio',
        'summary': "This is a small breakdown of what goes on with me."
    }
    return render(request, 'portfolio/home.html', context)
def about(request):
    bio = 'I am an aspiring Computer Science Major, who plans to graduate this upcoming May.'
    whereIlearned = "I graduated from Collierville High School. I then attended Southwest Community College for two years, until I transferred to the University of Memphis to pursue a Bachelor's Degree in Computer Science."
    skills = ["Ruby on Rails", "HTML", "CSS", "SQL", "Canva", "Python"]
    achieved = ["I achieved "]
    context = {
        'bio': bio,
        'whereIlearned': whereIlearned,
        'skills': skills,
        'achieved': achieved
    }
    return render(request, 'portfolio/about.html', context)


def work(request):
    work_history = [
        {"title": "Pyros Fire Fresh Pizza", "description": "3 years 2017-2020"},
        {"title": "Target Co.", "description": "Under 1 year, 2019-2020"},
        {"title": "Amerigo Italian Restaurant", "description": "3 and a half years - current. 2020- present"}
    ]
    context = {
        'workhistory': work_history
    }
    return render(request, 'portfolio/work.html', context)


def contact(request):
    contact_details = {
        "quote": "I won't compromise the privacy of my references at the moment, however here is my info if you have any further questions.",
        "email": "jhhbbart@memphis.edu",
        "phone": "901-444-4444",
        "social_media": {
            "github": "https://github.com/jeffnotjeffery/sa16-act2",
            "linkedin": "https://www.linkedin.com/in/your-linkedin-profile/"
        }
    }
    context = {
        'contact_details': contact_details
    }
    return render(request, 'portfolio/contact.html', context)


