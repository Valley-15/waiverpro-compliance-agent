# WaiverPro AI Compliance Report

Generated: 2026-06-12 17:46:33

## Summary

- Pages Checked: 9
- Compliant Pages: 9
- Needs Review: 0
- Pass Rate: 100.0%

---

## Detailed Results


### action-items.json
- Page URL: /dashboard/action-items
- Status: ✅ PASS
- Guideline Reference: Action Items
- Retrieved At: 2026-06-12T12:11:43.426272
- Screenshot: data/screenshots/action-items.png
- AI Finding: The UI displays the Action Items page at the specified URL, with a table showing ID, Name, Status, Priority, and Due Date columns. There are filter controls for Status and Priority. The Status and Priority values align with the guideline. While an explicit doughnut chart is not shown, a summary of total action items broken down by priority is presented with 'High', 'Low', and 'Medium' counts, which is equivalent to a summary doughnut chart. The '12 Total' next to the priority breakdown reflects the outstanding count, matching the concept of a notification badge even if it's not explicitly called a badge within the extracted UI data description.

### announcements.json
- Page URL: /dashboard/announcements
- Status: ✅ PASS
- Guideline Reference: Announcements
- Retrieved At: 2026-06-12T12:11:46.626802
- Screenshot: data/screenshots/announcements.png
- AI Finding: The page URL is /dashboard/announcements. The text 'Stay up to date with important system and program updates.' is present. Each announcement clearly shows a title, status badge (Expired), optional priority badge (Medium, Low, High), and a date. A search box is present via an input with a 'Search' placeholder.

### contact.json
- Page URL: /dashboard/contact
- Status: ✅ PASS
- Guideline Reference: Support — FAQs, Tickets & Contact
- Retrieved At: 2026-06-12T12:11:48.803215
- Screenshot: data/screenshots/contact.png
- AI Finding: The UI data for the /dashboard/contact page aligns with the guideline requirements. It includes the expected URL, a message form with fields for Name, Email, Subject, and Message, a 'Send Message' button, and displays support contact details for Email, Phone, Address, and Business Hours. The quick response information is also present, consistent with the guideline.

### facilities.json
- Page URL: /dashboard/facilities
- Status: ✅ PASS
- Guideline Reference: Facilities
- Retrieved At: 2026-06-12T12:11:51.553058
- Screenshot: data/screenshots/facilities.png
- AI Finding: The Facilities page is present at the specified URL. It contains status filters (All Facilities, Due Soon, Upcoming, Scheduled, Overdue, No Status), filters by Role and Type, and a search by name input field. The facilities table includes the columns Name, Type, License Number, License Exp Date, and Status. The Facilities Status Overview is also present below the table, and paging controls are evident ('Rows per page', 'Page 1 of 500').

### faqs.json
- Page URL: /dashboard/faqs
- Status: ✅ PASS
- Guideline Reference: Support — FAQs, Tickets & Contact
- Retrieved At: 2026-06-12T12:11:55.229878
- Screenshot: data/screenshots/faqs.png
- AI Finding: The page URL '/dashboard/faqs' matches the guideline. The main heading 'FAQs' is present. The page correctly lists FAQs that can be expanded to show answers, as indicated by the 'expandable_content_detected' and 'expanded_content' data, and the presence of questions that are also buttons, implying they toggle content. The description 'The FAQs page answers common questions about WaiverPro. Click any question to expand its answer.' is fully supported by the UI data.

### my-applications.json
- Page URL: /dashboard/my-applications
- Status: ✅ PASS
- Guideline Reference: My Applications
- Retrieved At: 2026-06-12T12:12:04.109069
- Screenshot: data/screenshots/my-applications.png
- AI Finding: The UI contains all the specified Waiver-type tabs (All, Patient Needs Waiver (PNW) Request, Program Flexibility (PF) Request, Workforce Shortage Waiver (WSW) Request) and Status chips (All Applications, Draft, Submitted, Reopen, In Review, Rejected, Approved, Evaluator Review, Manager Review, Revoked, and Expired). The applications table includes all required columns (Waiver ID, Name, Facility, Type, Status, and Created on). Both summary charts, 'Applications by Type' and 'Applications Overview', are present and depict the specified breakdowns.

### settings.json
- Page URL: /dashboard/settings
- Status: ✅ PASS
- Guideline Reference: Settings
- Retrieved At: 2026-06-12T12:12:07.062543
- Screenshot: data/screenshots/settings.png
- AI Finding: The Settings page displays an 'Organisation' heading, 'Profile Information' with first name, last name, email (read-only), and phone number fields, and a 'Save Changes' button. 'Notifications' section has toggles for Email Notifications, Status Updates, and Action Items. The 'Security' section allows password changes with a new password field stating 'At least 6 characters'. The 'Features' section includes toggles for 'Facilities Status Tracking' and 'FAQ Assistant Chatbot'.

### tickets.json
- Page URL: /dashboard/tickets
- Status: ✅ PASS
- Guideline Reference: Support — FAQs, Tickets & Contact
- Retrieved At: 2026-06-12T12:12:09.658580
- Screenshot: data/screenshots/tickets.png
- AI Finding: The UI data shows a '/dashboard/tickets' page with the heading 'Support Tickets', and a '+ New Ticket' button, consistent with the guideline's description of the Tickets page where users can 'Track and manage your support tickets.' and 'Click + New Ticket to raise one.' It also lists tickets as cards showing ticket number ('TICK-XXX'), status ('open', 'in-progress'), and priority ('medium') badges, and created/updated times, and 'View Details' buttons, all aligning with the guideline.

### user-management.json
- Page URL: /dashboard/user-management
- Status: ✅ PASS
- Guideline Reference: User Management
- Retrieved At: 2026-06-12T12:12:13.159783
- Screenshot: data/screenshots/user-management.png
- AI Finding: The User Management page is present with the correct URL. It has tabs for 'Member' and 'Pending Invites' showing counts, a table with 'Name', 'Email', 'Associated Facilities', 'Last Updated', and 'Actions' columns.  An 'Invite User' button and a search input are also visible. Paging controls are indicated by 'Rows per page' and 'Page 1 of 1'.

---

## Notes

- Analysis performed using Gemini 2.5 Flash.
- Guideline sections retrieved using ChromaDB.
- Results should be manually reviewed before final compliance decisions.