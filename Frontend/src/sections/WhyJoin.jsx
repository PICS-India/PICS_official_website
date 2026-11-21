import { whyJoin } from '../data/home.js';

function WhyJoin() {
  return (
    <section className="section section--alt" aria-labelledby="why-heading">
      <div className="container">
        <h2 id="why-heading" className="section__title">{whyJoin.title}</h2>
        <div className="grid grid--3">
          {whyJoin.items.map((item) => (
            <div className="card" key={item.title}>
              <h3 className="card__title">{item.title}</h3>
              <p>{item.text}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

export default WhyJoin;
