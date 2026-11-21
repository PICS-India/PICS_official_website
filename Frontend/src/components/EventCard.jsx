import Button from './Button.jsx';
import { registerLinkProps } from '../config/site.js';

function EventCard({ event, headingLevel = 3 }) {
  const { title, statusLabel, statusTone, dateLabel, duration, mode, shortDescription, cta } = event;
  const Heading = `h${headingLevel}`;
  const ctaProps = cta?.register ? registerLinkProps() : { to: cta?.to };

  return (
    <article className="card event-card">
      {statusLabel && <span className={`status status--${statusTone || 'green'}`}>{statusLabel}</span>}
      <Heading className="event-card__title">{title}</Heading>
      <div className="meta">
        {dateLabel && <span>{dateLabel}</span>}
        {duration && <span>{duration}</span>}
        {mode && <span>{mode}</span>}
      </div>
      {shortDescription && <p className="event-card__text">{shortDescription}</p>}
      {cta && (
        <Button variant={cta.variant || 'primary'} aria-label={`${cta.label}: ${title}`} {...ctaProps}>
          {cta.label}
        </Button>
      )}
    </article>
  );
}

export default EventCard;
