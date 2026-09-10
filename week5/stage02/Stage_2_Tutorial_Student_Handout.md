# Stage 2 Tutorial - From Problems to Requirements

## Activity 1 - Stakeholder Map

  -----------------------------------------------------------------------
  Stakeholder             Need                    Potential conflict
  ----------------------- ----------------------- -----------------------
  Clinic staff            Manage patient records  Need a simple system
                          and appointments.       while management may
                                                  want more reporting.

  Patients                Accurate patient and    Their needs may differ
                          appointment             from clinic staff
                          information.            processes.

  Healthcare              See their appointments  Availability may
  practitioners (GPs)     and availability.       conflict with requested
                                                  appointment times.

  Clinic management       Reliable records and    May want more features
                          basic operational       while the first version
                          reports.                must stay simple.

  Junior software         Clear requirements to   Unclear requirements
  engineer                build and test the      may lead to incorrect
                          system.                 assumptions.
  -----------------------------------------------------------------------

## Activity 2 - Functional or Non-Functional?

-   **Functional:** The system shall allow staff to cancel an
    appointment.
-   **Non-functional:** The system should remain responsive for the
    course-scale dataset.
-   **Functional:** The system shall retain cancelled appointments.
-   **Non-functional:** Core business logic should be independently
    testable.
-   **Functional:** The system shall search for a patient by ID.

## Activity 3 - Repair Ambiguous Requirements

### The system should be easy to use

**Problem:** "Easy to use" is vague and cannot be measured.\
**Clarification question:** What tasks should staff be able to complete
easily?

### Patient search should be fast

**Problem:** "Fast" is not measurable.\
**Clarification question:** What is the maximum acceptable search
response time?

### The system should securely manage data

**Problem:** "Securely" is too broad and does not define security
controls.\
**Clarification question:** What security requirements are needed for
patient data?

### Appointments should normally be easy to cancel

**Problem:** "Normally" and "easy" are unclear.\
**Clarification question:** Who can cancel appointments and what steps
should cancellation require?

## Activity 4 - AI Requirements Audit

  -----------------------------------------------------------------------
  AI suggestion           Classification          Evidence / reason
  ----------------------- ----------------------- -----------------------
  Patients receive SMS    Unsupported             SMS reminders are not
  reminders.                                      stated in the client
                                                  case study.

  Facial recognition      Out of scope            Facial recognition is
  login.                                          not requested for the
                                                  small SmartCare system.

  Receptionists create    Assumption requiring    Appointment management
  appointments.           validation              is confirmed, but the
                                                  case study does not
                                                  specifically state that
                                                  receptionists create
                                                  them.

  Online payment.         Out of scope            Payments are not part
                                                  of the stated patient,
                                                  practitioner and
                                                  appointment scope.

  Practitioners view      Assumption requiring    Practitioner
  schedules.              validation              availability is a
                                                  problem, but a
                                                  practitioner schedule
                                                  view is not explicitly
                                                  confirmed.

  AI recommends           Out of scope            Treatment
  treatments.                                     recommendations are not
                                                  part of the requested
                                                  system.

  Cancelled appointments  Confirmed               The case study
  remain in history.                              identifies cancellation
                                                  and appointment-history
                                                  problems.
  -----------------------------------------------------------------------

## Exit Question

**Why is "AI suggested it" not sufficient evidence for a requirement?**

AI suggestions are not sufficient evidence because AI can make
assumptions or suggest features the client did not ask for. Requirements
should be supported by client needs, the case study, stakeholders or
other verified evidence.
