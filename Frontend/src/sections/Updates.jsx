import { updates } from '../data/home.js';

function Updates() {
  return (
    <section className="section section--alt" id="updates" aria-labelledby="updates-heading">
      <div className="container">
        <h2 id="updates-heading" className="section__title">{updates.title}</h2>
        <div className="grid grid--3">
          {updates.items.map((item) => (
            <div className="card" key={item.title}>
              <span className="tag">{item.tag}</span>
              <h3 className="card__title card__title--spaced">{item.title}</h3>
              <p>{item.text}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

export default Updates;
