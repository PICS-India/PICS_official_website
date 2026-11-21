import { about } from '../data/home.js';

function About() {
  return (
    <section className="section section--alt" id="about" aria-labelledby="about-heading">
      <div className="container">
        <span className="tag">{about.tag}</span>
        <h2 id="about-heading" className="section__title">{about.title}</h2>
        <p className="lead">{about.intro}</p>
        <div className="grid grid--4">
          {about.stats.map((stat) => (
            <div className="card" key={stat.label}>
              <div className={`stat stat--${stat.tone}`}>{stat.value}</div>
              <p>{stat.label}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}

export default About;
