# SmartCare v0.2 - Requirements Specification

## 1. Problem and Scope

SmartCare currently uses spreadsheets, paper records and manual
processes to manage patients and appointments. This has caused duplicate
bookings, difficulty finding patient records, inconsistent appointment
status information, limited practitioner availability, manual
cancellations, unreliable appointment history and difficulty producing
basic reports.

The first version will focus on a small, maintainable system for
patient, practitioner and appointment management. Complex hospital
functions such as diagnosis, treatment recommendations, online payments
and facial recognition are out of scope.

## 2. Stakeholders

  -----------------------------------------------------------------------
  Stakeholder             Need                    Evidence
  ----------------------- ----------------------- -----------------------
  Clinic staff            Manage patient records, The case study
                          appointments and        describes manual
                          cancellations.          patient and appointment
                                                  processes.

  Patients                Have accurate patient   The case study
                          and appointment         identifies patient
                          information.            information and
                                                  appointment management.

  Healthcare              Have their availability The case study
  practitioners (GPs)     and appointments        identifies limited
                          managed.                visibility of
                                                  practitioner
                                                  availability.

  Clinic management       Access reliable         The case study
                          appointment information identifies difficulty
                          and basic operational   producing basic
                          reports.                operational reports.
  -----------------------------------------------------------------------

## 3. Functional Requirements

-   FR-01: The system shall allow staff to create a patient record.
-   FR-02: The system shall allow staff to search for a patient record.
-   FR-03: The system shall allow staff to create and manage
    practitioner records.
-   FR-04: The system shall record practitioner availability.
-   FR-05: The system shall allow staff to create an appointment.
-   FR-06: The system shall prevent duplicate appointment bookings for
    the same practitioner and time.
-   FR-07: The system shall allow staff to update an appointment status.
-   FR-08: The system shall allow staff to cancel an appointment.
-   FR-09: The system shall retain appointment history, including
    cancelled appointments.
-   FR-10: The system shall provide basic operational appointment
    reports.

## 4. Non-Functional Requirements

-   NFR-01: The system should be simple and usable for clinic staff.
-   NFR-02: The system should remain responsive for the course-scale
    dataset.
-   NFR-03: The system should maintain accurate and consistent patient
    and appointment data.
-   NFR-04: The system should be maintainable so future stages can be
    added without rewriting the whole application.
-   NFR-05: Core business logic should be independently testable.
-   NFR-06: The system should handle invalid input without corrupting
    stored data.

## 5. User Stories

-   US-01: As a clinic staff member, I want to create a patient record,
    so that patient information can be stored.
-   US-02: As a clinic staff member, I want to search for a patient, so
    that I can find patient information quickly.
-   US-03: As a clinic staff member, I want to book an appointment, so
    that a patient can see a practitioner.
-   US-04: As a clinic staff member, I want to cancel an appointment, so
    that appointment status stays accurate.
-   US-05: As a practitioner, I want my availability recorded, so that
    appointments can be scheduled correctly.
-   US-06: As clinic management, I want basic operational reports, so
    that I can review clinic appointment activity.

## 6. Acceptance Criteria

### AC-01 - Create an appointment

**GIVEN** a valid patient and practitioner are available\
**WHEN** a staff member creates an appointment for an available time\
**THEN** the appointment is saved with the correct patient, practitioner
and time.

### AC-02 - Cancel an appointment

**GIVEN** an existing appointment is booked\
**WHEN** a staff member cancels the appointment\
**THEN** the appointment is marked as cancelled and remains in
appointment history.

### AC-03 - Duplicate booking failure

**GIVEN** a practitioner already has an appointment at a selected time\
**WHEN** a staff member tries to book another appointment for the same
practitioner and time\
**THEN** the system rejects the duplicate booking.

## 7. Assumptions and Open Questions

-   It is assumed that clinic staff will be the main users who create
    and manage appointments. This needs confirmation.
-   What exact patient and practitioner details must be stored?
-   What appointment statuses are required besides booked and cancelled?
-   What specific operational reports does management need?
-   How should practitioner availability be entered and updated?

## 8. AI Requirements Review Record

  ---------------------------------------------------------------------------
  AI suggestion   Evidence?      Decision       Reason         Verification
  --------------- -------------- -------------- -------------- --------------
  Clarify who is  Partial        Unverified     Appointment    Confirm with
  allowed to                                    management is  client.
  create                                        confirmed, but 
  appointments.                                 the user role  
                                                is not         
                                                explicitly     
                                                stated.        

  Make patient    Question       Accepted       The            Ask client for
  search response                               requirement    acceptable
  time                                          "fast" would   response time.
  measurable.                                   be ambiguous   
                                                without a      
                                                measurable     
                                                target.        

  Add SMS         No             Rejected       SMS reminders  Not included.
  appointment                                   are not stated 
  reminders.                                    in the case    
                                                study.         

  Add online      No             Rejected       Payments are   Not included.
  payment.                                      outside the    
                                                stated scope.  

  Clarify which   Yes            Accepted       The reporting  Keep as an
  reports                                       problem is     open question.
  management                                    confirmed, but 
  needs.                                        exact reports  
                                                are not        
                                                defined.       
  ---------------------------------------------------------------------------
