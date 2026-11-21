import Button from '../components/Button.jsx';
import { registerLinkProps } from '../config/site.js';
import { heroSlides, heroTagline, heroContent } from '../data/home.js';

function Hero() {
  return (
    <header className="container hero" aria-labelledby="hero-heading">
      <div>
        <span className="tag">{heroContent.tag}</span>
        <h1 id="hero-heading" className="hero__title">
          Start your <em>policy</em> journey.
        </h1>
        <p className="lead">{heroContent.lead}</p>
        <div className="hero__actions">
          <Button variant="red" {...registerLinkProps()}>Register for PICS I</Button>
          <Button variant="outline" to="/#levels">Explore the programme</Button>
        </div>
      </div>
      <div>
        <div className="stage" role="img" aria-label={heroTagline}>
          {heroSlides.map((slide, index) => (
            <div
              key={slide.id}
              className="stage__slide"
              style={{
                background: slide.bg,
                '--c': slide.glowA,
                '--d': slide.glowB,
                '--t': slide.text,
                animationDelay: `${index * 4}s`,
              }}
            >
              <b>
                {slide.lines[0]}
                <br />
                {slide.lines[1]}
              </b>
            </div>
          ))}
        </div>
        <p className="stage__caption">{heroTagline}</p>
      </div>
    </header>
  );
}

export default Hero;
