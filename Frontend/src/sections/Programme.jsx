import Button from '../components/Button.jsx';
import { programme } from '../data/home.js';

function Programme() {
  return (
    <section className="section" id="levels" aria-labelledby="levels-heading">
      <div className="container">
        <h2 id="levels-heading" className="section__title">{programme.title}</h2>
        <div className="grid grid--2">
          {programme.levels.map((level) => (
            <div className={`card card--top card--${level.tone}`} key={level.title}>
              <span className={`tag tag--${level.tone}`}>{level.tag}</span>
              <h3 className="level__title">{level.title}</h3>
              <p>{level.text}</p>
              <Button variant={level.variant} to="/#events">{level.cta}</Button>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

export default Programme;
