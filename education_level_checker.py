print("aptitude-test-checker\n")

def get_user_input(prompt, valid_options=None):
    while True:
        user_input = input(prompt).upper()
        if valid_options:
            if user_input in valid_options:
                return user_input
            else:
                print(f"Valid options are: {', '.join(valid_options)}. Please try again.")
        else:
            return user_input

def save_user_data(name, education_level, career_suggestion):
    with open('user_data.txt', 'a') as file:
        file.write(f"{name}, {education_level}, {career_suggestion}\n")

def display_summary():
    try:
        with open('user_data.txt', 'r') as file:
            data = file.readlines()
            summary = {}
            for line in data:
                _, education_level, _ = line.strip().split(', ')
                if education_level in summary:
                    summary[education_level] += 1
                else:
                    summary[education_level] = 1
            
            print("\nSummary of Entries by Education Level:")
            for level, count in summary.items():
                print(f"{level}: {count}")
    except FileNotFoundError:
        print("No data available.")

career_data = {
    "IT Support Specialist": {
        "average_salary": "$53,470",
        "job_outlook": "8% (faster than average)",
        "required_education": "High School Diploma",
        "description": "IT Support Specialists provide help to people and companies with their computer equipment and software."
    },
    "Medical Assistant": {
        "average_salary": "$34,800",
        "job_outlook": "19% (much faster than average)",
        "required_education": "High School Diploma",
        "description": "Medical Assistants perform administrative and clinical tasks in the offices of physicians, hospitals, and other healthcare facilities."
    },
    "Administrative Assistant": {
        "average_salary": "$40,990",
        "job_outlook": "-7% (decline)",
        "required_education": "High School Diploma",
        "description": "Administrative Assistants perform routine clerical and administrative duties. They organize files, prepare documents, schedule appointments, and support other staff."
    },
    "Network Administrator": {
        "average_salary": "$83,510",
        "job_outlook": "5% (as fast as average)",
        "required_education": "Associate's Degree",
        "description": "Network Administrators are responsible for the day-to-day operation of computer networks."
    },
    "Nurse": {
        "average_salary": "$75,330",
        "job_outlook": "7% (faster than average)",
        "required_education": "Associate's Degree",
        "description": "Nurses provide and coordinate patient care, educate patients about health conditions, and provide advice and emotional support."
    },
    "Accountant": {
        "average_salary": "$73,560",
        "job_outlook": "4% (as fast as average)",
        "required_education": "Bachelor's Degree",
        "description": "Accountants prepare and examine financial records, ensuring that records are accurate and taxes are paid properly and on time."
    },
    "Web Designer": {
        "average_salary": "$77,200",
        "job_outlook": "8% (faster than average)",
        "required_education": "Associate's Degree",
        "description": "Web Designers create the look, layout, and features of a website."
    },
    "Software Developer": {
        "average_salary": "$110,140",
        "job_outlook": "22% (much faster than average)",
        "required_education": "Bachelor's Degree",
        "description": "Software Developers create applications or systems that run on computers or other devices."
    },
    "Physical Therapist": {
        "average_salary": "$89,440",
        "job_outlook": "18% (much faster than average)",
        "required_education": "Bachelor's Degree",
        "description": "Physical Therapists help injured or ill people improve movement and manage pain."
    },
    "Marketing Manager": {
        "average_salary": "$135,900",
        "job_outlook": "10% (faster than average)",
        "required_education": "Bachelor's Degree",
        "description": "Marketing Managers plan programs to generate interest in products or services."
    },
    "Art Director": {
        "average_salary": "$94,220",
        "job_outlook": "2% (slower than average)",
        "required_education": "Bachelor's Degree",
        "description": "Art Directors are responsible for the visual style and images in magazines, newspapers, product packaging, and movie and television productions."
    },
    "Data Scientist": {
        "average_salary": "$94,280",
        "job_outlook": "15% (much faster than average)",
        "required_education": "Master's Degree",
        "description": "Data Scientists use analytical tools and methods to extract meaningful insights from data."
    },
    "Healthcare Administrator": {
        "average_salary": "$100,980",
        "job_outlook": "32% (much faster than average)",
        "required_education": "Master's Degree",
        "description": "Healthcare Administrators plan, direct, and coordinate medical and health services."
    },
    "Financial Analyst": {
        "average_salary": "$83,660",
        "job_outlook": "5% (as fast as average)",
        "required_education": "Master's Degree",
        "description": "Financial Analysts provide guidance to businesses and individuals making investment decisions."
    },
    "Creative Director": {
        "average_salary": "$102,590",
        "job_outlook": "1% (slower than average)",
        "required_education": "Master's Degree",
        "description": "Creative Directors oversee the creative process of producing advertisements, products, and other creative endeavors."
    },
    "Chief Technology Officer": {
        "average_salary": "$163,250",
        "job_outlook": "4% (as fast as average)",
        "required_education": "PhD",
        "description": "Chief Technology Officers oversee a company’s technical direction, technology development, and technological policies."
    },
    "Medical Scientist": {
        "average_salary": "$91,510",
        "job_outlook": "6% (as fast as average)",
        "required_education": "PhD",
        "description": "Medical Scientists conduct research aimed at improving overall human health."
    },
    "Professor of Business": {
        "average_salary": "$88,580",
        "job_outlook": "9% (faster than average)",
        "required_education": "PhD",
        "description": "Professors of Business teach courses in business administration and management."
    },
    "Professor of Fine Arts": {
        "average_salary": "$75,940",
        "job_outlook": "6% (as fast as average)",
        "required_education": "PhD",
        "description": "Professors of Fine Arts teach courses in fine arts, such as painting, sculpture, or design."
    },
    "Lead Research Scientist": {
        "average_salary": "$102,800",
        "job_outlook": "8% (faster than average)",
        "required_education": "PhD",
        "description": "Lead Research Scientists direct and manage scientific research projects."
    }
}

def suggest_career(education_level, interests):
    career_suggestions = {
        "HS": {
            "TECH": "IT Support Specialist",
            "HEALTH": "Medical Assistant",
            "BUSINESS": "Administrative Assistant",
            "ARTS": "Graphic Designer",
            "SCIENCE": "Lab Technician"
        },
        "AS": {
            "TECH": "Network Administrator",
           

 "HEALTH": "Nurse",
            "BUSINESS": "Accountant",
            "ARTS": "Web Designer",
            "SCIENCE": "Research Assistant"
        },
        "BS": {
            "TECH": "Software Developer",
            "HEALTH": "Physical Therapist",
            "BUSINESS": "Marketing Manager",
            "ARTS": "Art Director",
            "SCIENCE": "Biologist"
        },
        "MS": {
            "TECH": "Data Scientist",
            "HEALTH": "Healthcare Administrator",
            "BUSINESS": "Financial Analyst",
            "ARTS": "Creative Director",
            "SCIENCE": "Chemist"
        },
        "PHD": {
            "TECH": "Chief Technology Officer",
            "HEALTH": "Medical Scientist",
            "BUSINESS": "Professor of Business",
            "ARTS": "Professor of Fine Arts",
            "SCIENCE": "Lead Research Scientist"
        }
    }
    
    suggested_career = career_suggestions[education_level].get(interests, "Career not found")
    career_info = career_data.get(suggested_career, {})
    
    return suggested_career, career_info

def check_education_level():
    first_name = get_user_input("\nWhat's your name? ")
    education_level = get_user_input("Please enter your education level (HS, AS, BS, MS, or PhD): ", 
                                     valid_options=["HS", "AS", "BS", "MS", "PHD"])
    
    interests = get_user_input("Please enter your primary interest (TECH, HEALTH, BUSINESS, ARTS, SCIENCE): ", 
                               valid_options=["TECH", "HEALTH", "BUSINESS", "ARTS", "SCIENCE"])

    suggested_career, career_info = suggest_career(education_level, interests)
    
    print(f"\nHello, {first_name}! Based on your education level ({education_level}) and your interest ({interests}), a suggested career is: {suggested_career}.")
    if career_info:
        print(f"\nCareer Information:\nAverage Salary: {career_info['average_salary']}\nJob Outlook: {career_info['job_outlook']}\nRequired Education: {career_info['required_education']}\nDescription: {career_info['description']}")
    save_user_data(first_name, education_level, suggested_career)

def main():
    print("* * Aptitude Test Checker * *")
    while True:
        check_education_level()
        next_action = get_user_input("\nWould you like to take another test? (yes/no/summary/exit): ", 
                                     valid_options=["YES", "NO", "SUMMARY", "EXIT"])
        if next_action == "NO":
            continue
        elif next_action == "SUMMARY":
            display_summary()
        elif next_action == "EXIT":
            print("Exiting program. Goodbye!")
            break

main()