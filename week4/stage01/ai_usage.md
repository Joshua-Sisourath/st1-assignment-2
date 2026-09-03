AI usage 
I used AI (CoPilot) as a tutor to help me understand and compare the SmartCare appointment booking code.

"Act as a Python tutor. Explain this code and identify potential problems. Suggest improvements without rewriting the whole application."

I also asked AI to "create a simple beginner-friendly alternative that stores a patient name, practitioner name and appointment time without using a database or GUI" and it gave me this:

appointments = []

def add_appointment(patient_name, practitioner_name, appointment_time):
    # Basic validation to ensure all details are provided
    if not patient_name or not practitioner_name or not appointment_time:
        raise ValueError("All appointment details are required")

    # Create a dictionary to store one appointment
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    # Store the appointment in the list
    appointments.append(appointment)

    return appointment

AI suggested:
Checking that appointment details are not blank.
Using a list to store appointments.
Using a dictionary to store each appointment.
Using a function to add appointments.

I accepted the validation of the patient name, practitioner name and appointment time because it helps prevent incomplete appointments. I did not add complex features such as a database or GUI because they were outside the requirements for Stage 1.

I read through the AI-generated code and compared it with my human version. I ran the code to make sure it worked and tested the appointment function with normal and unusual inputs. I also checked that the AI version only used features required by the task.