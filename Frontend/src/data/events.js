// Events shown on the home page and the /events page.
// `category` drives the tabs: 'upcoming' | 'ongoing' | 'completed'.
// `statusTone` picks the badge colour: 'green' | 'amber'.

export const events = [
  {
    id: 'pics-i-insight-fourth-cohort',
    title: 'PICS I – Insight · Fourth Cohort',
    category: 'upcoming',
    statusLabel: 'Registration open',
    statusTone: 'green',
    dateLabel: '11–17 Nov 2026',
    duration: '7 days',
    mode: 'Online',
    shortDescription: 'A seven-day public policy challenge for beginners.',
    description:
      'A seven-day public policy challenge for beginners. Seven themes and tasks introduce public policy, governance systems and contemporary issues, with roughly 60 minutes of engagement each day. Successful participants receive a GPPRC Certificate of Completion.',
    cta: { label: 'Register', register: true },
  },
  {
    id: 'pics-ii-inquiry',
    title: 'PICS II – Inquiry',
    category: 'upcoming',
    statusLabel: 'Dates to be announced',
    statusTone: 'amber',
    dateLabel: 'Dates TBA',
    duration: '14 days',
    mode: '',
    shortDescription: 'Second stage for PICS I graduates.',
    description:
      'A deeper, research-oriented exploration of governance issues for PICS I graduates, building informed perspectives over 14 days.',
    cta: { label: 'Get notified', to: '/events/pics-ii-inquiry', variant: 'outline' },
  },
];

export const eventTabs = [
  { id: 'all', label: 'All' },
  { id: 'upcoming', label: 'Upcoming' },
  { id: 'ongoing', label: 'Ongoing' },
  { id: 'completed', label: 'Completed' },
];

export function getEventById(id) {
  return events.find((event) => event.id === id);
}
