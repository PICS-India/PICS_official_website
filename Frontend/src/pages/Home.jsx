import Hero from '../sections/Hero.jsx';
import About from '../sections/About.jsx';
import Programme from '../sections/Programme.jsx';
import WhyJoin from '../sections/WhyJoin.jsx';
import EventsSection from '../sections/EventsSection.jsx';
import Updates from '../sections/Updates.jsx';
import Faq from '../sections/Faq.jsx';
import RegisterCta from '../sections/RegisterCta.jsx';

function Home() {
  return (
    <>
      <Hero />
      <About />
      <Programme />
      <WhyJoin />
      <EventsSection />
      <Updates />
      <Faq />
      <RegisterCta />
    </>
  );
}

export default Home;
