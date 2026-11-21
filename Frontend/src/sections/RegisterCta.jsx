import Button from '../components/Button.jsx';
import { registerLinkProps } from '../config/site.js';
import { registerCta } from '../data/home.js';

function RegisterCta() {
  return (
    <section className="container register" id="register" aria-labelledby="register-heading">
      <div className="register__panel">
        <div>
          <h2 id="register-heading">{registerCta.title}</h2>
          <p>{registerCta.text}</p>
        </div>
        <Button variant="light" {...registerLinkProps()}>{registerCta.cta}</Button>
      </div>
    </section>
  );
}

export default RegisterCta;
