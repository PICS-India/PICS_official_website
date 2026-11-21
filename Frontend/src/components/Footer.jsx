import { Link } from 'react-router-dom';
import Logo from './Logo.jsx';
import { SITE, registerLinkProps } from '../config/site.js';

function Footer() {
  const register = registerLinkProps();
  const hasConnect = SITE.linkedinUrl || SITE.contactEmail;

  return (
    <footer className="footer">
      <div className="container">
        <div className="footer__grid">
          <div>
            <Logo className="logo--light" />
            <p className="footer__about">
              {SITE.fullName}. An initiative of {SITE.organisation}, GPPRC.
            </p>
          </div>
          <nav aria-label="Explore">
            <h2 className="footer__heading">Explore</h2>
            <ul>
              <li><Link to="/#about">About</Link></li>
              <li><Link to="/#levels">Programme</Link></li>
              <li><Link to="/events">Events</Link></li>
            </ul>
          </nav>
          <nav aria-label="Support">
            <h2 className="footer__heading">Support</h2>
            <ul>
              <li><Link to="/#faq">FAQ</Link></li>
              <li>
                {register.href ? (
                  <a href={register.href} target="_blank" rel="noopener noreferrer">Register</a>
                ) : (
                  <Link to={register.to}>Register</Link>
                )}
              </li>
            </ul>
          </nav>
          {hasConnect && (
            <nav aria-label="Connect">
              <h2 className="footer__heading">Connect</h2>
              <ul>
                {SITE.linkedinUrl && (
                  <li><a href={SITE.linkedinUrl} target="_blank" rel="noopener noreferrer">LinkedIn</a></li>
                )}
                {SITE.contactEmail && <li><a href={`mailto:${SITE.contactEmail}`}>Email</a></li>}
              </ul>
            </nav>
          )}
        </div>
        <p className="footer__copy">© {new Date().getFullYear()} {SITE.organisation}</p>
      </div>
    </footer>
  );
}

export default Footer;
