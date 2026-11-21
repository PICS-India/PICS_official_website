import { useParams } from 'react-router-dom';
import Button from '../components/Button.jsx';
import { getEventById } from '../data/events.js';
import { registerLinkProps } from '../config/site.js';

function EventDetails() {
  const { eventId } = useParams();
  const event = getEventById(eventId);

  if (!event) {
    return (
      <section className="container page-section empty-state">
        <h1>Event not found</h1>
        <p>We could not find that event. It may have been removed or the link may be incorrect.</p>
        <Button to="/events">Back to events</Button>
      </section>
    );
  }

  const meta = [
    ['Date', event.dateLabel],
    ['Duration', event.duration],
    ['Mode', event.mode],
  ].filter(([, value]) => value);

  return (
    <article className="container container--narrow page-section event-details">
      <Button to="/events" variant="outline" className="event-details__back">
        Back to events
      </Button>
      {event.statusLabel && (
        <span className={`status status--${event.statusTone || 'green'}`}>{event.statusLabel}</span>
      )}
      <h1 className="page-title">{event.title}</h1>
      {meta.length > 0 && (
        <dl className="event-details__meta">
          {meta.map(([label, value]) => (
            <div key={label}><dt>{label}</dt><dd>{value}</dd></div>
          ))}
        </dl>
      )}
      {event.description && (
        <>
          <h2 className="event-details__subtitle">About this event</h2>
          <p className="event-details__text">{event.description}</p>
        </>
      )}
      {event.cta?.register && <Button {...registerLinkProps()}>Register for this event</Button>}
    </article>
  );
}

export default EventDetails;
