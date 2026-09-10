# Assignment 2 - Case Study Lab

## Stage 2 Lab Activities - SmartCare Requirements Engineering

## Part A - Client Brief: AI OFF

SmartCare currently uses spreadsheets, paper records and manual
processes. Current problems include duplicate bookings, difficulty
finding patient information, inconsistent appointment status and limited
appointment history. Management wants a small and maintainable system
focused on patients, practitioners and appointments.

## Part B - Stakeholders and Scope: AI OFF

### Stakeholders

-   Clinic staff - need to manage patient records and appointments.
-   Patients - need accurate patient and appointment information.
-   Healthcare practitioners (GPs) - need their appointments and
    availability managed.
-   Clinic management - need reliable information and basic operational
    reporting.

### In Scope

-   Patient management.
-   Practitioner management.
-   Appointment management.
-   Searching for patient information.
-   Preventing duplicate appointment bookings.
-   Updating appointment status.
-   Cancelling appointments and retaining appointment history.
-   Basic operational reports.

### Out of Scope

-   AI diagnosis or treatment recommendations.
-   Facial-recognition login.
-   Online payment.
-   A complex hospital information system.

### Provisional / Needs Confirmation

-   Exactly which staff role creates and manages appointments.
-   How practitioner availability should be entered or displayed.
-   The exact reports management requires.

## Part C - Functional Requirements: AI OFF

-   FR-01: The system shall allow staff to create a patient record.
-   FR-02: The system shall allow staff to search for patient
    information.
-   FR-03: The system shall allow practitioner information to be
    recorded and managed.
-   FR-04: The system shall record practitioner availability.
-   FR-05: The system shall allow staff to create an appointment.
-   FR-06: The system shall prevent duplicate bookings for the same
    practitioner and appointment time.
-   FR-07: The system shall allow appointment status information to be
    updated.
-   FR-08: The system shall allow an appointment to be cancelled.
-   FR-09: The system shall retain appointment history, including
    cancelled appointments.
-   FR-10: The system shall provide basic operational appointment
    reports.

## Part D - Non-Functional Requirements: AI OFF

-   NFR-01: The system should be simple and usable for clinic staff.
-   NFR-02: The system should remain responsive for the course-scale
    dataset.
-   NFR-03: The system should maintain accurate and consistent patient
    and appointment data.
-   NFR-04: The system should be maintainable so later stages can be
    added without rewriting the whole application.
-   NFR-05: Core business logic should be independently testable.
-   NFR-06: Invalid input should not corrupt stored patient or
    appointment data.

## Part E - User Stories and Acceptance Criteria: AI OFF

### User Stories

-   US-01: As a clinic staff member, I want to create a patient record,
    so that patient information can be stored.
-   US-02: As a clinic staff member, I want to search for a patient, so
    that I can find patient information quickly.
-   US-03: As a clinic staff member, I want to create an appointment, so
    that a patient can be booked with a practitioner.
-   US-04: As a clinic staff member, I want to cancel an appointment, so
    that appointment status remains accurate.
-   US-05: As a practitioner, I want my availability recorded, so that
    appointments can be scheduled correctly.
-   US-06: As clinic management, I want basic operational reports, so
    that I can review appointment activity.

### Acceptance Criteria

**AC-01**\
GIVEN a valid patient and practitioner are available\
WHEN a staff member creates an appointment for an available time\
THEN the appointment is saved with the correct details.

**AC-02**\
GIVEN an existing appointment is booked\
WHEN a staff member cancels the appointment\
THEN it is marked as cancelled and remains in appointment history.

**AC-03 - Failure scenario**\
GIVEN a practitioner already has an appointment at a selected time\
WHEN another appointment is attempted for the same practitioner and
time\
THEN the system rejects the duplicate booking.

## Part F - AI Requirements Review: AI ON

-   Clarify which staff role is allowed to create and manage
    appointments - assumption requiring validation.
-   Make vague words such as "fast" or "easy to use" measurable -
    clarification needed before making a specific target.
-   Clarify what basic operational reports management needs - supported
    by the reporting problem, but the exact reports are not specified.
-   SMS appointment reminders could be suggested by AI, but there is no
    client evidence for them.
-   Online payment could be suggested by AI, but it is outside the
    stated scope.

## Part G - VERIFY the AI Review

-   **Clarify staff role - Unverified.** Appointment management is
    confirmed, but the exact user role is not stated.
-   **Make vague requirements measurable - Accepted.** Requirements
    should be clear and testable, but the actual measurement still needs
    client confirmation.
-   **Clarify operational reports - Accepted.** Reporting is a confirmed
    problem, but the exact report types are unknown.
-   **Add SMS reminders - Rejected.** There is no evidence that the
    client requested SMS reminders.
-   **Add online payment - Rejected.** Payments are not part of the
    stated patient, practitioner and appointment scope.

## Part H - Finalise SmartCare v0.2

### Assumptions and Open Questions

-   Assumption: clinic staff will be the main users who manage
    appointments. This must be confirmed.
-   What exact patient information must be stored?
-   What exact practitioner information must be stored?
-   What appointment statuses are required?
-   How should practitioner availability be entered and updated?
-   What specific operational reports does management require?

The final SmartCare v0.2 requirements include the stakeholder analysis,
scope, 10 functional requirements, 6 non-functional requirements, 6 user
stories, 3 acceptance criteria, assumptions/open questions and verified
AI review evidence.

## Reflection

AI helped me notice that some of my requirements were still too vague to
test properly. For example, words such as "fast" and "easy to use" sound
reasonable but do not explain how the requirement would be measured. AI
also highlighted that the exact staff role responsible for creating
appointments and the exact reports required by management still need
clarification. However, AI could also overreach by suggesting features
such as SMS reminders or online payments. These may sound useful, but
they are not supported by the SmartCare client brief, so I rejected them
rather than treating them as requirements. After the review, I changed
the reporting requirement so that it only says the system should provide
basic operational appointment reports, while the exact report types
remain an open question. This avoids inventing details that the client
has not confirmed. Requirements need evidence because the software
should be based on real client and stakeholder needs. Without evidence,
assumptions can increase the scope and lead to building features that
the client did not request.
