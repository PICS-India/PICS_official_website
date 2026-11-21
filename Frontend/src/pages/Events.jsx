import { events } from '../data/events.js';
import EventCard from '../components/EventCard.jsx';

function Events() {
  return (
    <section className="container page-section" aria-labelledby="events-heading">
      <h1 id="events-heading" className="page-title">Events</h1>
      {events.length > 0 ? (
        <div className="grid grid--2">
          {events.map((event) => <EventCard key={event.id} event={event} headingLevel={2} />)}
        </div>
      ) : (
        <p className="empty-note" role="status">No events are currently listed.</p>
      )}
    </section>
  );
}

export default Events;
