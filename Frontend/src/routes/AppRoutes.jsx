import { useEffect } from 'react';
import { Routes, Route, useLocation } from 'react-router-dom';
import Home from '../pages/Home.jsx';
import Events from '../pages/Events.jsx';
import EventDetails from '../pages/EventDetails.jsx';
import Button from '../components/Button.jsx';

/* Scrolls to a #hash target (e.g. /#about) or to the top on page change. */
function ScrollManager() {
  const { pathname, hash } = useLocation();

  useEffect(() => {
    if (hash) {
      const target = document.getElementById(hash.slice(1));
      if (target) {
        target.scrollIntoView();
        return;
      }
    }
    window.scrollTo(0, 0);
  }, [pathname, hash]);

  return null;
}

function NotFound() {
  return (
    <section className="page-section container empty-state">
      <h1>Page not found</h1>
      <p>The page you are looking for does not exist or has moved.</p>
      <Button to="/">Go to home</Button>
    </section>
  );
}

function AppRoutes() {
  return (
    <>
      <ScrollManager />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/events" element={<Events />} />
        <Route path="/events/:eventId" element={<EventDetails />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </>
  );
}

export default AppRoutes;
