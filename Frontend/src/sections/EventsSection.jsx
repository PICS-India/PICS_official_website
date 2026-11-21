import { useState } from 'react';
import EventCard from '../components/EventCard.jsx';
import { events, eventTabs } from '../data/events.js';

function EventsSection() {
  const [tab, setTab] = useState('upcoming');
  const visible = tab === 'all' ? events : events.filter((event) => event.category === tab);

  return (
    <section className="section" id="events" aria-labelledby="events-section-heading">
      <div className="container">
        <h2 id="events-section-heading" className="section__title">Events</h2>
        <div className="tabs" role="group" aria-label="Filter events">
          {eventTabs.map((t) => (
            <button
              key={t.id}
              type="button"
              className={`tabs__btn${tab === t.id ? ' tabs__btn--on' : ''}`}
              aria-pressed={tab === t.id}
              onClick={() => setTab(t.id)}
            >
              {t.label}
            </button>
          ))}
        </div>
        {visible.length > 0 ? (
          <div className="grid grid--2">
            {visible.map((event) => <EventCard key={event.id} event={event} />)}
          </div>
        ) : (
          <p className="empty-note" role="status">No events in this category right now.</p>
        )}
      </div>
    </section>
  );
}

export default EventsSection;
