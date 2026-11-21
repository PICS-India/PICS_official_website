import { Link } from 'react-router-dom';

/**
 * Reusable button. Renders:
 *  - a router <Link> when `to` is given
 *  - an <a> when `href` is given
 *  - a <button> otherwise
 * Variants: primary (blue) | red | outline | outline-red | light
 */
function Button({
  children,
  variant = 'primary',
  to,
  href,
  className = '',
  type = 'button',
  ...rest
}) {
  const classes = `btn btn--${variant} ${className}`.trim();

  if (to) {
    return (
      <Link to={to} className={classes} {...rest}>
        {children}
      </Link>
    );
  }

  if (href) {
    return (
      <a href={href} className={classes} {...rest}>
        {children}
      </a>
    );
  }

  return (
    <button type={type} className={classes} {...rest}>
      {children}
    </button>
  );
}

export default Button;
