import { useEffect, useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import Button from './Button.jsx';
import Logo from './Logo.jsx';
import ColorBar from './ColorBar.jsx';
import { registerLinkProps } from '../config/site.js';

const links = [
  { to: '/#about', label: 'About' },
  { to: '/#levels', label: 'Programme' },
  { to: '/events', label: 'Events' },
  { to: '/#updates', label: 'Updates' },
  { to: '/#faq', label: 'FAQ' },
];

function Navbar() {
  const [isOpen, setIsOpen] = useState(false);
  const location = useLocation();

  useEffect(() => {
    setIsOpen(false);
  }, [location.pathname, location.hash]);

  useEffect(() => {
    const onKeyDown = (event) => {
      if (event.key === 'Escape') setIsOpen(false);
    };
    document.addEventListener('keydown', onKeyDown);
    return () => document.removeEventListener('keydown', onKeyDown);
  }, []);

  return (
    <header className="navbar">
      <ColorBar />
      <div className="container navbar__inner">
        <Link to="/" className="navbar__brand" aria-label="PICS home">
          <Logo />
        </Link>

        <nav
          id="primary-navigation"
          className={`navbar__menu${isOpen ? ' navbar__menu--open' : ''}`}
          aria-label="Primary"
        >
          <ul className="navbar__list">
            {links.map((link) => (
              <li key={link.label}>
                <Link
                  to={link.to}
                  className={`navbar__link${
                    link.to === '/events' && location.pathname.startsWith('/events') ? ' navbar__link--active' : ''
                  }`}
                >
                  {link.label}
                </Link>
              </li>
            ))}
          </ul>
        </nav>

        <div className="navbar__actions">
          <Button className="navbar__cta" {...registerLinkProps()}>
            Register
          </Button>
          <button
            type="button"
            className="navbar__toggle"
            aria-expanded={isOpen}
            aria-controls="primary-navigation"
            aria-label={isOpen ? 'Close menu' : 'Open menu'}
            onClick={() => setIsOpen((open) => !open)}
          >
            <span className="navbar__toggle-bar" />
            <span className="navbar__toggle-bar" />
            <span className="navbar__toggle-bar" />
          </button>
        </div>
      </div>
    </header>
  );
}

export default Navbar;
