import { faq } from '../data/home.js';

function Faq() {
  return (
    <section className="section" id="faq" aria-labelledby="faq-heading">
      <div className="container container--narrow">
        <h2 id="faq-heading" className="section__title">{faq.title}</h2>
        <div className="faq">
          {faq.items.map((item, index) => (
            <details key={item.q} open={index === 0}>
              <summary>{item.q}</summary>
              <p>{item.a}</p>
            </details>
          ))}
        </div>
      </div>
    </section>
  );
}

export default Faq;
