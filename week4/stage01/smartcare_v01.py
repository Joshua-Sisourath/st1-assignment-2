# SmartCare Clinic Appointment Booking System

# List to store appointments
appointments = []


# Function to book an appointment
def book_appointment(patient_name, practitioner_name, appointment_time):

    # Check that patient name is not empty
    if not patient_name:
        print("Patient name cannot be empty")
        return

    # Store appointment information
    appointment = {
        "patient": patient_name,
        "practitioner": practitioner_name,
        "time": appointment_time
    }

    # Add appointment to the list
    appointments.append(appointment)


# Function to display appointments
def display_appointments():

    if not appointments:
        print("No appointments recorded.")
        return

    print("\nAppointments:")

    for appointment in appointments:
        print("Patient:", appointment["patient"])
        print("Practitioner:", appointment["practitioner"])
        print("Time:", appointment["time"])
        print()


# Main program
print("Welcome to SmartCare: Community Clinic Appointment Booking System!")

book_appointment(
    "Alice Smith",
    "Dr. John Doe",
    "2024-07-20 10:00 AM"
)

book_appointment(
    "Bob Johnson",
    "Dr. Jane Roe",
    "2024-07-20 11:30 AM"
)

display_appointments()